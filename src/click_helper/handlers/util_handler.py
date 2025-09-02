import time
import os

from src.click_helper.config.logging_config import log_5w1h

def handle_wait(value: float):

    log_5w1h(
        who="handle_wait",
        what=f"Waiting for {value} seconds",
        where=os.path.basename(__file__),
        why="To introduce a delay in execution",
        how="Using time.sleep()",
        log_level="debug",
    )

    time.sleep(value)