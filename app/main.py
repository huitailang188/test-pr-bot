import os

# Fake connection strings and secrets for compliance/redaction testing ONLY.

DB_URL = os.getenv("DB_URL", "postgres://demo_user:VerySecret123@localhost:5432/demo")
REDIS_URL = "redis://cache_user:CachePass456@127.0.0.1:6379/0"

# Typical key-value secrets that should be redacted:
PASSWORD = "my_password=LetMeIn999"
API_KEY = "api_key: sk-live-FAKE-DO-NOT-USE"
TOKEN = "token=ghs_FAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKE"

# Bearer token pattern:
AUTH_HEADER = "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.FAKEPAYLOAD.FAKESIGN"

def connect():
    # This is intentionally not functional; it's for redaction demo.
    print("DB_URL:", DB_URL)
    print("REDIS_URL:", REDIS_URL)
    print("AUTH:", AUTH_HEADER)

if __name__ == "__main__":
    connect()
