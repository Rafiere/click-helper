import os

from src.click_helper.config.logging_config import log_5w1h

def handle_log(value: str):

    log_5w1h(
        who="handle_log",
        what=f"Logging message: {value}",
        where=os.path.basename(__file__),
        why="To log a custom message",
        how="Using structlog logger",
        log_level="debug",
    )
