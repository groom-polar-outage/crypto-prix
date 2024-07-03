from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from fastapi import Depends
from fastapi_users import UUIDIDMixin, BaseUserManager, FastAPIUsers
from fastapi_users.authentication import (
    BearerTransport,
    JWTStrategy,
    AuthenticationBackend,
)

from app.auth.db import get_user_db
from app.config import CONFIG


class _UserManager(UUIDIDMixin, BaseUserManager):
    reset_password_token_secret = CONFIG.FASTAPI_USERS_SECRET
    verification_token_secret = CONFIG.FASTAPI_USERS_SECRET


async def _get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield _UserManager(user_db)


_bearer_transport = BearerTransport(tokenUrl="/login")


def _get_jwt_strategy():
    return JWTStrategy(secret=CONFIG.FASTAPI_USERS_SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt", transport=_bearer_transport, get_strategy=_get_jwt_strategy
)
fastapi_users = FastAPIUsers(_get_user_manager, [auth_backend])
active_user = fastapi_users.current_user(active=True)
