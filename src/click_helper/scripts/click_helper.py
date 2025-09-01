import logging
import sys
import yaml
import os

from click_helper.domain.command_map import COMMAND_MAP


from typing import List, Dict

def get_script_path(relative_path: str):
    """
    Get the absolute path to a script file given its relative path.
    """

    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    root_dir = os.path.dirname(base_dir)

    return os.path.join(root_dir, relative_path)

def load_script_from_file() -> List[Dict]:
    """Load an automation script from a YAML file."""

    try:
        with open(YAML_FILE_PATH, 'r', encoding='utf-8') as file:

            script_data = yaml.safe_load(file)
            if not isinstance(script_data, list):
                logging.error("The yaml file must contain a list of commands.")
                return []
            
            return script_data
        
    except FileNotFoundError:
        logging.error(f"Error: File '{YAML_FILE_PATH}' not found.")
        sys.exit(1)
    
    except yaml.YAMLError as e:
        logging.error(f"Error reading YAML file: {e}")
        sys.exit(1)

def run_automation_script(script: List[Dict]):
    """
    Execute a series of commands defined in a DSL script.
    """

    for command in script:

        action = next(iter(command))
        value = command[action]

        handler = COMMAND_MAP.get(action)

        if handler:
            handler(value)
        else:
            logging.warning(f"Unknown command in DSL: '{action}'")


YAML_RELATIVE_FILE_PATH = 'files/command_script.yaml'

YAML_FILE_PATH = get_script_path(YAML_RELATIVE_FILE_PATH)

script_content = load_script_from_file()
run_automation_script(script_content)