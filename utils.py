from datetime import datetime
import hashlib

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()