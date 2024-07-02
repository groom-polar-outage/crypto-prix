from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

_DATABASE_URL = "sqlite+aiosqlite:///./test.db"
_Base = declarative_base()


class User(SQLAlchemyBaseUserTableUUID, _Base):
    pass


_engine = create_async_engine(_DATABASE_URL)
_async_session_maker = sessionmaker(_engine, class_=AsyncSession, expire_on_commit=False)


async def create_db_and_tables():
    async with _engine.begin() as conn:
        await conn.run_sync(_Base.metadata.create_all)


async def _get_async_session():
    async with _async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(_get_async_session)):
    yield SQLAlchemyUserDatabase(session=session, user_table=User)
