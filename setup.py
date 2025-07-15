from setuptools import setup, find_packages

setup(
    name="multi-agent-router",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "langgraph",
        "pytest",
        "httpx"
    ],
)