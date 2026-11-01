# Ansel

Test automation for [automationexercise.com](https://automationexercise.com): UI tests with Selenium and API tests with requests, run with pytest.

## Tech
- Python, pytest
- Selenium WebDriver (Page Object Model)
- requests
- pytest-html
- GitHub Actions

## Tests
- UI: register, login, logout, products, search, cart, checkout and payment, invoice
- API: products, brands, search, login, create/update/delete account
- E2E: products on the UI compared with the API

## Setup
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run
```
pytest              # all
pytest -m ui        # ui only
pytest -m api       # api only
pytest -m e2e
```
Headless: set `HEADLESS=1`

Report: `reports/report.html`
