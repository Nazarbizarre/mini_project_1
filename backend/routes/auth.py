from typing import Annotated
from datetime import timedelta

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from ..schemas import Token, AuthorData
from ..utils import authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from ..db import AsyncDB, Author


auth_router = APIRouter(prefix="/auth")


@auth_router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Annotated[Session, Depends(AsyncDB.get_session)],
) -> Token:
    user = authenticate_user(form_data.username, form_data.password, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.name}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@auth_router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    data: AuthorData, session: Annotated[Session, Depends(AsyncDB.get_session)]
):
    user = Author(**data.model_dump())
    session.add(user)
    return user