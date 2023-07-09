from setuptools import find_packages,setup
from typing import List
def get_requirmnets(file_path:str)->List[str]:
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[i.replace("\n","") for i in requirments]

        return requirments
    
setup(name="project",
      version="0.0.1",
      author="ram",
      author_email="@gmail.com",
      install_requires=get_requirmnets("requirment.txt"),
      packages=find_packages()
      )