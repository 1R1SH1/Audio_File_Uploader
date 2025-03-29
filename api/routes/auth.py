from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from core.security import create_access_token, get_current_user, ACCESS_TOKEN_EXPIRE_MINUTES
from core.yandex_auth import YandexAuth
import os

from models.user import User

router = APIRouter()

@router.post("/auth/yandex/callback", response_model=User)
async def yandex_callback(code: str):
    yandex_auth = YandexAuth()
    user_data = await yandex_auth.authorize(code)
    return user_data

@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_current_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}