import logging
import time

def handle_wait(value: float):
    logging.info(f"Waiting for {value} seconds...")
    time.sleep(value)