from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
  """This function will return the list of requiremnts"""
  requirements_list: List[str] = []
  try:
    with open('requirements.txt',"r") as file:
      lines = file.readlines()
      for line in lines:
        requirement = line.strip()

        if requirement and requirement!="-e .":
          requirements_list.append(requirement)

  except FileNotFoundError:
    print("Hey! requirements.txt file not found")

  return requirements_list


setup(
  name="NetworkSecurity",
  version="0.0.1",
  author="Nitish",
  author_email="nitishkathuria33@gmail.com",
  packages=find_packages(),
  install_requires = get_requirements()
)
