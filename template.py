import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')
project_name = "Holiday Management"


list_of_files = [
    
    # Config
    f"{project_name}/agents/__init__.py",
    f"{project_name}/config/settings.py",

    #Agents
    f"{project_name}/agents/__init__.py",
    f"{project_name}/agents/planner.py",
    f"{project_name}/agents/researcher.py",

    # Teams
    f"{project_name}/teams/__init__.py",
    f"{project_name}/teams/holiday_team.py",

    # Utils
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/utils.py",

    # Tests
    f"{project_name}/tests/__init__.py",
    f"{project_name}/tests/test_agents.py",

    # Root files inside the project folder
    "app.py"

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory : {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating file : {filepath}")
    else:
        logging.info(f"File Already Exists: {filepath}")