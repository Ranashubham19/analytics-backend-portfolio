import logging
from app.config import ALERT_THRESHOLD

def check_threshold(data):
    try:
        price = float(data["bitcoin"]["usd"])

        if price > ALERT_THRESHOLD:
            logging.warning(f"ALERT! Price crossed threshold: {price}")
            return True

        logging.info(f"Price checked: {price}")
        return False

    except (KeyError, ValueError, TypeError) as e:
        logging.error(f"Data processing error: {e}")
        return False
