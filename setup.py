from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        reuirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(name="Census-income",
      version = "0.0.1",
      Author = "Bikesh",
      authormail = "bikeshsingh023@gmail.com",
      packages = find_packages(),
      intall_requires = get_requirements('requirements.txt')
    )