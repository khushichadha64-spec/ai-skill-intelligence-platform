from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = "hackathon-secret-change-later"  # fine for demo, don't ship this to prod
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 120

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# Mock users for the demo — swap for a real DB later if there's time
FAKE_USERS = {
    "admin1": {"password": "admin123", "role": "admin"},
    "learner1": {"password": "learner123", "role": "learner", "employee_id": "EMP001"},
}

def authenticate_user(username: str, password: str):
    user = FAKE_USERS.get(username)
    if not user or user["password"] != password:
        return None
    return {"username": username, **user}

def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode["exp"] = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise credentials_exception

def require_role(required_role: str):
    def role_checker(user: dict = Depends(get_current_user)):
        if user.get("role") != required_role:
            raise HTTPException(status_code=403, detail="Not authorized for this action")
        return user
    return role_checker