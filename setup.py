from setuptools import find_packages,setup

from typing import List

REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readline()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]




setup(
    name="sensor",
    version="0.0.1",
    author="rahulmaurya1109",
    author_email="rahulmaurya751@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),
)
