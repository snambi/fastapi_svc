from invoke import task
import os

@task
def clean(c):
    """removes generated files"""
    c.run("rm -rf build dist")
    for root, _, files in os.walk('gptsvc'):
        if '__pycache__' in root:
            print(f"Removing: {os.path.join(root, '__pycache__')}")
            c.run(f"rm -rf {os.path.join(root, '__pycache__')}")