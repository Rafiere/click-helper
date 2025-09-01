import logging
import pyautogui

from typing import List, Any

def handle_move_to(value: List[int]):
    logging.info(f"Moving mouse to X={value[0]}, Y={value[1]}")
    pyautogui.moveTo(value[0], value[1])

def handle_click(value: Any):
    if isinstance(value, list) and len(value) == 2:
        logging.info(f"Clicking at X={value[0]}, Y={value[1]}")
        pyautogui.click(value[0], value[1])
    else:
        logging.info("Clicking at current mouse position.")
        pyautogui.click()