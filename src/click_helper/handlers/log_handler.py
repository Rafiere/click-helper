import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def handle_log(value: str):
    logging.info(f"Message: {value}")