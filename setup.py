'''
This will install all the packages inside requirments.txt
and it will treat our project as a package
'''
from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="RAG Medcial Chatbot",
    version="0.1",
    author="Rakesh Kumar",
    packages=find_packages(),
    install_requires = requirements,
)