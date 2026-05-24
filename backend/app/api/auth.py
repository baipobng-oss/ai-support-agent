from fastapi import APIRouter
from pydantic import BaseModel

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter(prefix="/auth")

fake_db = {}

class AuthRequest(BaseModel):
    email: str
    password: str

@router.post("/register")
def register(req: AuthRequest):

    fake_db[req.email] = hash_password(
        req.password
    )

    return {
        "message": "User created"
    }

@router.post("/login")
def login(req: AuthRequest):

    hashed = fake_db.get(req.email)

    if not hashed:
        return {
            "error": "User not found"
        }

    valid = verify_password(
        req.password,
        hashed
    )

    if not valid:
        return {
            "error": "Invalid password"
        }

    token = create_access_token({
        "sub": req.email
    })

    return {
        "access_token": token
    }