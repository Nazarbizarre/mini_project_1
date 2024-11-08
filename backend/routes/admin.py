from typing import Annotated

from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import (APIRouter,
                     Depends,
                     HTTPException)

from ..db import (Author,
                  AsyncDB,
                  Role)
from ..utils import get_current_user
from ..loggers.middleware import request_logging_dependency


admin_router = APIRouter(prefix="/admin", tags=["admin"])


@admin_router.put("/grant_admin/{user_id}", summary = "Set admin", description = "Set admin role for user")
async def grant_admin(
    user_id: int,
    current_user: Annotated[Author, Depends(get_current_user)],
    session: Annotated[Session, Depends(AsyncDB.get_session)],
):
    if not current_user.is_admin():
        raise HTTPException(status_code=401, detail="Not enough permissions")

    user = session.scalar(select(Author).where(Author.id == user_id))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    admin_role = session.scalar(select(Role).where(Role.name == "admin"))
    if not admin_role:
        raise HTTPException(status_code=500, detail="Admin role not found")
    user.role = admin_role
    session.refresh(user)
    return {"user role updated to": admin_role}
