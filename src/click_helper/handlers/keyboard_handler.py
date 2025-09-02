import os

import pyautogui

from typing import List

from src.click_helper.config.logging_config import log_5w1h

def handle_hotkey(value: List[str]):

    log_5w1h(
        who="handle_hotkey",
        what=f"Pressing hotkey: {' + '.join(value)}",
        where=os.path.basename(__file__),
        why="To simulate a keyboard hotkey combination",
        how="Using pyautogui.hotkey()",
        log_level="debug",
    )

    pyautogui.hotkey(*value)

def handle_write(value: str):

    log_5w1h(
        who="handle_write",
        what=f"Writing text: {value}",
        where=os.path.basename(__file__),
        why="To simulate typing text",
        how="Using pyautogui.write()",
        log_level="debug",
    )

    pyautogui.write(value)