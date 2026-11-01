from datetime import datetime


def make_user():
    ts = datetime.now().strftime("%Y%m%d%H%M%S%f")
    return {
        "name": "Test User",
        "email": f"testuser_{ts}@mailinator.com",
        "password": "Test@12345",
        "title": "Mr",
        "birth_date": "10",
        "birth_month": "5",
        "birth_year": "1995",
        "firstname": "Test",
        "lastname": "User",
        "company": "QA Labs",
        "address1": "12 Test Street",
        "address2": "Block B",
        "country": "India",
        "zipcode": "201301",
        "state": "Uttar Pradesh",
        "city": "Noida",
        "mobile_number": "9876543210",
    }


def card_details():
    return {"name": "Test User", "number": "4111111111111111", "cvc": "123",
            "month": "12", "year": "2030"}
