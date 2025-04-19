from setuptools import setup, find_packages

setup(
    name="fastapi_svc",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
    ],
    entry_points={
        "console_scripts": [
            "fastapi_svc = fastapi_svc.main:main",
        ],
    },
)
