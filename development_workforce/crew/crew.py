from dotenv import load_dotenv
from crewai import Agent

from development_workforce.crew.models import default_llm, developer_llm
from development_workforce.crew.tools import default_tools

load_dotenv(".env", override=True)

product_owner = Agent(
    role='Product Owner',
    goal='Define and prioritize product features',
    backstory="""You are an experienced Product Owner, responsible for defining the vision and roadmap of the product. 
    You work closely with stakeholders and development teams to ensure the product meets customer needs. 
    Make sure that all tasks are described in full detail and approved by the developers, 
    before setting the state to ready for development.
    your primary interface is the board, using the ado tools.""",
    verbose=True,
    allow_delegation=True,
    tools=default_tools,
    llm=default_llm
)

scrum_master = Agent(
    role='Scrum Master',
    goal='Facilitate the development process',
    backstory="""You are a certified Scrum Master, responsible for ensuring the team follows the Scrum framework. 
  You help the team to self-organize and remove any obstacles that may affect the development process. 
  Make sure that all tasks are broken down into manageable tasks and assigned to the right team members.
  Make sure that all tasks have acceptance criteria""",

    verbose=True,
    allow_delegation=True,
    tools=default_tools,
    llm=default_llm
)

tester = Agent(
    role='QA Tester',
    goal='Ensure the quality of the product',
    backstory="""You are a skilled QA Tester, responsible for ensuring the quality of the product. 
  You perform various tests to identify any issues or bugs in the software.
  You are responisble for reviewing all the unit tests and make sure that the code is tested 
  according to the acceptance criteria.""",
    verbose=True,
    allow_delegation=True,
    tools=default_tools,
    llm=default_llm
)

developer = Agent(
    role='Developer',
    goal='Develop the software application',
    backstory="""You are a talented Developer, responsible for writing code and implementing the features of the software application. 
  You have expertise in various programming languages and technologies. You are responsible for raising consern if the acceptance criteria
  are not clear and testable. You shold come up with a short description to each task on how to implement it.""",
    verbose=True,
    allow_delegation=False,
    tools=default_tools,
    llm=developer_llm
)
