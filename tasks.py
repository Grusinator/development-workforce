from pathlib import Path

from invoke import task, Collection

from src.util_tools.map_dir import DirectoryStructure

docker_path = Path("devops/docker")


@task
def docker_run(ctx, env=""):
    """run docker dompose with build arg"""
    base_compose = docker_path / "docker-compose.yml"
    # env_compose = docker_path / f"docker-compose.{env}.yml"
    ctx.run(f"docker-compose -f {base_compose} up --build")


@task
def start_worker(ctx):
    ctx.run("celery -A development_workforce worker --loglevel=info -E --pool=solo")


@task
def start_flower(ctx):
    ctx.run("celery -A development_workforce flower --port=5555")

@task
def map_dir(ctx, path="."):
    struct = DirectoryStructure(path).get_formatted_directory_structure()
    print(struct)
    return struct
