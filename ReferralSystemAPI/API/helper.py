import hashlib
import datetime
import hashlib
import jwt
from datetime import datetime, timedelta, timezone
from django.conf import settings

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

def generate_jwt_token(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.now(timezone.utc) + timedelta(days=1),
        'iat': datetime.now(timezone.utc)
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token

def verify_jwt_token(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None