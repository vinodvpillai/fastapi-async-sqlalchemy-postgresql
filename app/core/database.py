import contextlib
from typing import Any, AsyncIterator

from app.core.env_settings import settings
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)
#from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DatabaseSessionManager:
    def __init__(self, host: str):
        self._engine = create_async_engine(host, echo=True, future=True)
        self._sessionmaker = async_sessionmaker(autocommit=False, bind=self._engine)

    async def close(self):
        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized")
        await self._engine.dispose()

        self._engine = None
        self._sessionmaker = None

    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized")

        async with self._engine.begin() as connection:
            try:
                yield connection
            except Exception:
                await connection.rollback()
                raise

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        if self._sessionmaker is None:
            raise Exception("DatabaseSessionManager is not initialized")

        session = self._sessionmaker()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

DATABASE_URL = f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOSTNAME}:{settings.DATABASE_PORT}/{settings.POSTGRES_DB}"
sessionmanager = DatabaseSessionManager(DATABASE_URL)

async def get_db_session():
    async with sessionmanager.session() as session:
        yield session
        
async def get_db_connection():
    async with sessionmanager.connect() as connection:
        yield connection
        
# Ensure models are imported here
from app.model.article import Article