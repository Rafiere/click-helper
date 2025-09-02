import sys
import yaml
import os

from typing import List, Dict

from src.click_helper.config.logging_config import configure_logging, log_5w1h
from src.click_helper.domain.command_map import COMMAND_MAP


def get_script_path(relative_path: str):
    """
    Get the absolute path to a script file given its relative path.
    """

    log_5w1h(
        who="get_script_path",
        what=f"Getting script path for: {relative_path}",
        where=os.path.basename(__file__),
        why="To locate the script file",
        how="Using os.path functions",
        log_level="info",
    )

    base_dir = os.path.dirname(os.path.abspath(__file__))

    root_dir = os.path.dirname(base_dir)

    return os.path.join(root_dir, relative_path)


def load_script_from_file() -> List[Dict]:
    """Load an automation script from a YAML file."""

    try:
        with open(get_initial_configuration_files(), 'r', encoding='utf-8') as file:

            log_5w1h(
                who="load_script_from_file",
                what=f"Loading script from file: {get_initial_configuration_files()}",
                where=os.path.basename(__file__),
                why="To read the automation commands",
                how="Using yaml.safe_load()",
                log_level="info",
            )

            script_data = yaml.safe_load(file)
            if not isinstance(script_data, list):
                log_5w1h(
                    who="load_script_from_file",
                    what="YAML content is not a list",
                    where=os.path.basename(__file__),
                    why="The script must be a list of commands",
                    how="Check the YAML file format",
                    log_level="error",
                )
                return []

            return script_data

    except FileNotFoundError:
        log_5w1h(
            who="load_script_from_file",
            what=f"File not found: {get_initial_configuration_files()}",
            where=os.path.basename(__file__),
            why="The specified YAML file does not exist",
            how="Check the file path",
            log_level="error",
        )

        sys.exit(1)

    except yaml.YAMLError as e:

        log_5w1h(
            who="load_script_from_file",
            what=f"YAML parsing error: {e}",
            where=os.path.basename(__file__),
            why="The YAML file is malformed",
            how="Check the YAML syntax",
            log_level="error",
        )
        sys.exit(1)


def run_automation_script(script: List[Dict]):
    """
    Execute a series of commands defined in a DSL script.
    """

    log_5w1h(
        who="run_automation_script",
        what="Running automation script",
        where=os.path.basename(__file__),
        why="To perform the defined automation tasks",
        how="Iterating through commands and executing handlers",
        log_level="info",
    )

    for command in script:

        action = next(iter(command))
        value = command[action]

        handler = COMMAND_MAP.get(action)

        if handler:
            handler(value)
        else:
            log_5w1h(
                who="run_automation_script",
                what=f"Unknown command: {action}",
                where=os.path.basename(__file__),
                why="The command is not recognized",
                how="Check the command name",
                log_level="debug",
            )

def get_initial_configuration_files():
    YAML_RELATIVE_FILE_PATH = 'click_helper/files/command_script.yaml'

    YAML_FILE_PATH = get_script_path(YAML_RELATIVE_FILE_PATH)

    log_5w1h(
        who="get_initial_configuration_files",
        what=f"Retrieving initial configuration file: {YAML_FILE_PATH}",
        where=os.path.basename(__file__),
        why="To load the automation script",
        how="Using get_script_path()",
        log_level="info",
    )

    return YAML_FILE_PATH


def initial_configuration():

    configure_logging()

    log_5w1h(
        who="initial_configuration",
        what="Starting initial configuration",
        where=os.path.basename(__file__),
        why="To set up logging and load the script",
        how="Calling configure_logging() and load_script_from_file()",
        log_level="info",
    )

    script_content = load_script_from_file()

    log_5w1h(
        who="initial_configuration",
        what="Loaded script content",
        where=os.path.basename(__file__),
        why="To verify the loaded commands",
        how="Printing the script content",
        log_level="debug",
    )

    run_automation_script(script_content)


initial_configuration()