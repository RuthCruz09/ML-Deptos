from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='ML-Deptos',
    version="0.1.0",
    author="Ruth Cruz",
    author_email="ruthn.cruz09@gmail.com",
    description="Machine Learning Prediccion ",
    url="https://github.com/RuthCruz09/ML-Deptos",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')


)