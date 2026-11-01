def get_price(txt):
    num = "".join(c for c in txt if c.isdigit())
    return int(num) if num else 0
