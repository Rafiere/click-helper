import logging
import subprocess

from typing import List

def handle_open_process(value: List[str]):
    logging.info(f"Opening process: {value}")
    try:
        subprocess.Popen(value)
    except FileNotFoundError:
        logging.error(f"Error: Process '{value[0]}' not found.")