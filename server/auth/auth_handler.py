import time
from typing import Dict
import jwt


JWT_SECRET = "THIS_IS_SECRET"
JWT_ALGORITHM = "HS256"

def token_response(token: str):
    return {
        "access_token": token
    }

def sing_in(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 1200
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

def decode_token(token: str) -> dict:
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        return decoded if decoded["expires"] >= time.time() else None
    except Exception:
        return {}
