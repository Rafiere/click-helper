import logging
import os
import subprocess

from typing import List

from src.click_helper.config.logging_config import log_5w1h

def handle_open_process(value: List[str]):

    log_5w1h(
        who="handle_open_process",
        what=f"Opening process: {' '.join(value)}",
        where=os.path.basename(__file__),
        why="To execute an external command",
        how="Using subprocess.Popen()",
        log_level="debug",
    )

    try:
        subprocess.Popen(value)
    except FileNotFoundError:
        log_5w1h(
            who="handle_open_process",
            what=f"File not found: {value}",
            where=os.path.basename(__file__),
            why="The specified file or command does not exist",
            how="Check the file path or command name",
            log_level="error",
        )