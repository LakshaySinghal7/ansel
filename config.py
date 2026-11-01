import os
from pathlib import Path

BASE_URL = os.getenv("BASE_URL", "https://automationexercise.com")
HEADLESS = os.getenv("HEADLESS", "0") == "1"
TIMEOUT = 15

ROOT = Path(__file__).parent
DATA_DIR = ROOT / "data"
REPORT_DIR = ROOT / "reports"

AD_URLS = [
    "*googlesyndication*", "*doubleclick*", "*googleadservices*",
    "*adservice.google*", "*fundingchoicesmessages*",
]
