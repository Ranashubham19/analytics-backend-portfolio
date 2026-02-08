from fastapi import FastAPI
import logging

from app.client import fetch_api_data
from app.alert_service import check_threshold
from app.config import LOG_FILE

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI(title="REST API Alert System")

@app.get("/health")
def health_check():
    return {"status": "running"}

@app.get("/check-alert")
def run_alert_check():
    data = fetch_api_data()
    if not data:
        return {"error": "Failed to fetch API data"}

    alert = check_threshold(data)

    return {
        "alert_triggered": alert,
        "current_price": data["bitcoin"]["usd"]
    }
