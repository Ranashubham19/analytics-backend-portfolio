import time
from app.client import fetch_api_data
from app.alert_service import check_threshold

def run_scheduler():
    while True:
        data = fetch_api_data()
        if data:
            check_threshold(data)
        time.sleep(300)  # every 5 minutes

if __name__ == "__main__":
    run_scheduler()
