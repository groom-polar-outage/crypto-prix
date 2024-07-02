from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from auth.db import User

from os import remove
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from fastapi_users.schemas import BaseUser, BaseUserCreate, BaseUserUpdate
from pendulum import now

from app.config import CONFIG
from app.auth.users import auth_backend, fastapi_users, active_user
from app.auth.db import create_db_and_tables
from app.connectors.tsdb import get_data


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield
    remove("test.db")

app = FastAPI(lifespan=lifespan,root_path="/api/v1")

app.include_router(fastapi_users.get_auth_router(auth_backend),
                   tags=["auth"])
app.include_router(fastapi_users.get_register_router(BaseUser, BaseUserCreate),
                   tags=["auth"])
app.include_router(fastapi_users.get_reset_password_router(),
                   tags=["auth"])
app.include_router(fastapi_users.get_verify_router(BaseUser),
                   tags=["auth"])
app.include_router(fastapi_users.get_users_router(BaseUser, BaseUserUpdate),
                   tags=["users"],
                   prefix="/users")


@app.get("/price")
async def price(user: User = Depends(active_user)):
    return {
        "req_time": now(CONFIG.TIMEZONE).to_rfc3339_string(),
        "data": get_data()
    }
