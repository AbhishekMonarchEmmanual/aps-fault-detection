from setuptools import find_packages,setup
from typing import List 


Requirement_file_name = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_reuqirements()-> List[str]:
    with open(Requirement_file_name) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list 



  

setup( 
    name = "sensor",
    version ="0.0.1",
    author = "abhishek", 
    author_email= "abhimonarch60@gmail.com", 
    packages = find_packages(),
    install_requires = get_requirements() 
    )


