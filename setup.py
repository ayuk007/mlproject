from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(file_path: str)->List[str]:
    '''
    Returns a list of requirements
    
    '''
    requirements = []

    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', ' ') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements


# MetaData
setup(
    name = "ML Project",
    version = "0.0.1",
    author = "Ayush",
    author_email = "ayush.nashine4807@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')                 #['pandas', 'numpy', 'seaborn']
)