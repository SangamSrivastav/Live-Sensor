#python setup.py install

from setuptools import setup, find_packages
from typing import List

def get_requirements() ->list[str]:
    """
    This function returns a list of requirements
    """
    # with open('requirements.txt') as f:
    #     requirements = f.readlines()
    
    # # Remove any leading/trailing whitespace characters
    # requirements = [req.strip() for req in requirements]
    
    # # Remove any empty strings from the list
    # requirements = [req for req in requirements if req]
    
    # return requirements

    requirements_list = list[str] = []
    return requirements_list



setup(
name='sensor',
version="0.0.1",
author='Sangam',
author_email="sangamsrivastav2002@gmail.com",
packages=find_packages(),
install_requires =   get_requirements() #['pymongo']
)