import os
from pathlib import Path
from logging import *

#configuring logging settings
basicConfig(level=INFO, format='[%(asctime)s]: %(message)s:')

project_name = "cnnClassifier"

# project structure
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

# creating directories and their respective files
for file in list_of_files:
    filepath = Path(file)
    dirname, filename = os.path.split(filepath)

    if dirname!="":
        os.makedirs(dirname,exist_ok = True)
        info(f"Creating directory; {dirname} for the file: {filename}")

    elif (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath , "w") as f:
            pass
        info(f"Creating file {filename} in the directory: {dirname}")

    else:
        info(f"{filename} already exists")