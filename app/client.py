import requests
import logging
from app.config import API_URL

def fetch_api_data():
    try:
        response = requests.get(API_URL, timeout=10)

        if response.status_code == 429:
            logging.error("Rate limit exceeded")
            return None

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return None
