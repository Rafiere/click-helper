import logging
import pyautogui

from typing import List

def handle_hotkey(value: List[str]):
    logging.info(f"Pressing hotkey: {' + '.join(value)}")
    pyautogui.hotkey(*value)

def handle_write(value: str):
    logging.info(f"Typing: '{value}'")
    pyautogui.write(value)