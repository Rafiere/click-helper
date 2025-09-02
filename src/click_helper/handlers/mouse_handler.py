import os

import pyautogui

from typing import List

from src.click_helper.config.logging_config import log_5w1h


def handle_move_to(value: List[int]):

    log_5w1h(who="handle_move_to",
             what=f"Moving mouse to X={value[0]}, Y={value[1]}",
             where=os.path.basename(__file__),
             why="To position the mouse cursor",
             how="Using pyautogui.moveTo()",
             log_level="info",
    )

    pyautogui.moveTo(value[0], value[1])

def handle_click(value: List[int]):
    if isinstance(value, list) and len(value) == 2:

        log_5w1h(
            who="handle_click",
            what=f"Clicking at X={value[0]}, Y={value[1]}",
            where=os.path.basename(__file__),
            why="To perform a mouse click at a specific position",
            how="Using pyautogui.click()",
            log_level="debug",
        )

        pyautogui.click(value[0], value[1])
    else:

        log_5w1h(
            who="handle_click",
            what="Clicking at the current mouse position",
            where=os.path.basename(__file__),
            why="To perform a mouse click at the current position",
            how="Using pyautogui.click()",
            log_level="debug",
        )

        pyautogui.click()