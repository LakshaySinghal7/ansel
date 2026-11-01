import requests


class ApiClient:
    def __init__(self, base_url):
        self.url = f"{base_url}/api"
        self.s = requests.Session()

    def send(self, method, endpoint, **kwargs):
        return self.s.request(method, f"{self.url}/{endpoint}", timeout=30, **kwargs)

    def get_products(self, method="GET"):
        return self.send(method, "productsList")

    def get_brands(self, method="GET"):
        return self.send(method, "brandsList")

    def search_product(self, name=None):
        payload = {"search_product": name} if name is not None else {}
        return self.send("POST", "searchProduct", data=payload)

    def verify_login(self, email=None, password=None, method="POST"):
        payload = {}
        if email is not None:
            payload["email"] = email
        if password is not None:
            payload["password"] = password
        return self.send(method, "verifyLogin", data=payload)

    def create_account(self, user):
        return self.send("POST", "createAccount", data=user)

    def update_account(self, user):
        return self.send("PUT", "updateAccount", data=user)

    def delete_account(self, email, password):
        return self.send("DELETE", "deleteAccount", data={"email": email, "password": password})

    def get_user(self, email):
        return self.send("GET", "getUserDetailByEmail", params={"email": email})
