import pytest
import os
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    async_scoped_session,
    AsyncSession,
)
from sqlalchemy.pool import NullPool
from httpx import AsyncClient, ASGITransport
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine
from src.config import settings
from src.models.base import Base
from asyncio import current_task


@pytest.fixture(scope="session", autouse=True)
def create_migrations():
    print("Running migrations")
    os.system(f"alembic upgrade head")


@pytest.fixture(scope="session")
def engine():
    engine = create_async_engine(
        url=settings.db.db_string_url,
        poolclass=NullPool,
    )
    yield engine
    engine.sync_engine.dispose()


@pytest.fixture(scope="session")
async def create(engine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.reflect)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="session")
async def db_session(engine, create) -> AsyncSession:

    sessionmaker = async_sessionmaker(
        bind=engine, autoflush=False, autocommit=False, expire_on_commit=False
    )
    session = async_scoped_session(
        sessionmaker,
        scopefunc=current_task,
    )
    return session


@pytest.fixture(scope="session")
async def override_session_dep(db_session) -> AsyncSession:

    async def _override_session_dep():
        async with db_session() as ses:
            yield ses

    return _override_session_dep


@pytest.fixture(scope="session")
def overriden_app(override_session_dep):
    from src.dependencies.session_dep import get_session
    from src.main import app

    app.dependency_overrides[get_session] = override_session_dep
    return app


@pytest.fixture(scope="session")
async def ac(overriden_app):
    app = overriden_app

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as async_test_client:
        yield async_test_client


@pytest.fixture(scope="function")
async def db_context_session(db_session):
    async with db_session() as ses:
        yield ses
