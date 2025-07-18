from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from sqlalchemy.engine.base import Engine
from sqlalchemy_utils import create_database, database_exists

from db_config import db_config


class DatabaseSetup:
    def __init__(self):
        pass

    def create_tables(self, engine: Engine):
        """
        Create tables with engine of submitted database.

        Args:
            engine (Engine): Engine of submitted databse.
        """
        db_config.Base.metadata.create_all(engine)

    def create_engine(self) -> Engine:
        """
        Create Database and Engine.

        Returns:
            Engine: Engine of database.
        """
        url = db_config.DATABASE_URL
        if not database_exists(url):
            create_database(url)
        return create_engine(url, echo=True)

    def create_session(self, engine: Engine) -> scoped_session[Session]:
        """
        Create Session.

        Args:
            engine (Engine): Engine of submitted database.

        Returns:
            scoped_session[Session]: Current Session object.
        """
        return scoped_session(sessionmaker(bind=engine))
