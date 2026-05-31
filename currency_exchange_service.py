import requests

URL = "https://api.frankfurter.dev/v1/2024-01-15?from=USD"

def fetch_rates(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

class Currency:
    def __init__(self, code, rate, base="USD"):
        self.code = code
        self.rate = rate
        self.base = base

    def __str__(self):
        return f"{self.code}: {self.rate:.4f} per {self.base}"

    def __eq__(self, other):
        return self.code == other.code

    def __hash__(self):
        return hash(self.code)

class RateBook():
    def __init__(self, currencies, base):
        self._by_code = {c.code: c for c in currencies}
        self.base = {c.code: base for c in currencies}

    @classmethod
    def from_json(cls, raw_data):
        pass

    def __getitem__(self, code):
        ...

    def __len__(self):
        ...

    def __contains__(self, code):
        ...

    def __iter__(self):
        ...

"""TESTING__________________________________"""

data = fetch_rates(URL)
book = RateBook.from_json(data)
