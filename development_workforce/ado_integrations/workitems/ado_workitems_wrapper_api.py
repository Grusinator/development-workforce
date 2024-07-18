import os
from typing import List

from azure.devops.connection import Connection
from azure.devops.v7_1.work_item_tracking.models import JsonPatchOperation
from dotenv import load_dotenv
from msrest.authentication import BasicAuthentication

from development_workforce.ado_integrations.workitems.ado_workitem_models import CreateWorkItemInput, AdoWorkItem, \
    UpdateWorkItemInput
from development_workforce.ado_integrations.workitems.base_ado_workitems_api import BaseAdoWorkitemsApi

load_dotenv()


class ADOWorkitemsWrapperApi(BaseAdoWorkitemsApi):
    def __init__(self):
        self.organization_url = os.getenv("ADO_ORGANIZATION_URL")
        self.personal_access_token = os.getenv("ADO_PERSONAL_ACCESS_TOKEN")
        self.project_name = os.getenv("ADO_PROJECT_NAME")
        credentials = BasicAuthentication('', self.personal_access_token)
        self.connection = Connection(base_url=self.organization_url, creds=credentials)
        self.client = self.connection.clients.get_work_item_tracking_client()

    def create_work_item(self, work_item: CreateWorkItemInput) -> int:
        document = [
            JsonPatchOperation(op='add', path='/fields/System.Title', value=work_item.title),
            JsonPatchOperation(op='add', path='/fields/System.Description', value=work_item.description),
            JsonPatchOperation(op='add', path='/fields/System.WorkItemType', value=work_item.type),
            JsonPatchOperation(op='add', path='/fields/System.AssignedTo', value=work_item.assigned_to),
        ]
        created_work_item = self.client.create_work_item(document, self.project_name, work_item.type)
        return created_work_item.id

    def get_work_item(self, work_item_id: int) -> AdoWorkItem:
        work_item = self.client.get_work_item(work_item_id)
        return AdoWorkItem(
            id=work_item.id,
            title=work_item.fields['System.Title'],
            type=work_item.fields['System.WorkItemType'],
            description=work_item.fields.get('System.Description', None),
            assigned_to=work_item.fields.get('System.AssignedTo', {}).get('displayName') if work_item.fields.get(
                'System.AssignedTo') else None,
            tags=work_item.fields.get('System.Tags', '').split('; ') if work_item.fields.get('System.Tags') else [],
            state=work_item.fields.get('System.State', None)
        )

    def update_work_item(self, updates: UpdateWorkItemInput) -> None:
        document = []
        if updates.title:
            document.append(JsonPatchOperation(op='replace', path='/fields/System.Title', value=updates.title))
        if updates.description:
            document.append(
                JsonPatchOperation(op='replace', path='/fields/System.Description', value=updates.description))
        if updates.assigned_to:
            document.append(
                JsonPatchOperation(op='replace', path='/fields/System.AssignedTo', value=updates.assigned_to))
        if updates.state:
            document.append(JsonPatchOperation(op='replace', path='/fields/System.State', value=updates.state))
        if updates.tags:
            document.append(JsonPatchOperation(op='replace', path='/fields/System.Tags', value="; ".join(updates.tags)))
        self.client.update_work_item(document, updates.id)

    def delete_work_item(self, work_item_id: int) -> None:
        self.client.delete_work_item(work_item_id)

    def list_work_items(self, work_item_type: str = None, assigned_to: str = None) -> List[AdoWorkItem]:
        query = "SELECT [System.Id], [System.Title], [System.State], [System.AssignedTo], [System.WorkItemType], [System.Description] FROM WorkItems"
        conditions = []
        if work_item_type:
            conditions.append(f"[System.WorkItemType] = '{work_item_type}'")
        if assigned_to:
            conditions.append(f"[System.AssignedTo] = '{assigned_to}'")
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        query += " ORDER BY [System.CreatedDate] DESC"
        wiql = {'query': query}
        result = self.client.query_by_wiql(wiql)
        work_items = [self.get_work_item(work_item.id) for work_item in result.work_items]
        return work_items


# Example usage
if __name__ == "__main__":
    api = ADOWorkitemsWrapperApi()
    work_item_input = CreateWorkItemInput(title="Sample task", description="This is a sample task", type="Task")
    work_item_id = api.create_work_item(work_item_input)
    print(f"Work item created with ID: {work_item_id}")
