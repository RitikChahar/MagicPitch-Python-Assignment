import hashlib
import datetime
import hashlib
import jwt
from datetime import datetime, timedelta, timezone
from django.conf import settings
SECRET_KEY = settings.SECRET_KEY

def generate_unique_hash(name):
    current_datetime = datetime.now()
    combined_str = f"{name}-{current_datetime}"
    hash_object = hashlib.sha256(combined_str.encode())
    return hash_object.hexdigest()

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_password

def verify_password(input_password, hashed_password):
    return hashed_password == hash_password(input_password)

def generate_jwt_token(email):
    payload = {
        'email': email,
        'exp': datetime.now(timezone.utc) + timedelta(days=1)  # Token expiration time
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def verify_jwt_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None