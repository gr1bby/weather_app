from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from sqlalchemy.engine.base import Engine
from sqlalchemy_utils import create_database, database_exists

from app.database.db_config import db_config
from app.core.logger import logger


class DatabaseSetup:
    def __init__(self):
        pass

    def create_tables(self, engine: Engine):
        """
        Create tables with engine of submitted database.

        Args:
            engine (Engine): Engine of submitted databse.
        """
        logger.info("Creating database tables...")
        db_config.Base.metadata.create_all(engine)
        logger.info("Tables created successfully.")

    def create_engine(self) -> Engine:
        """
        Create Database and Engine.

        Returns:
            Engine: Engine of database.
        """
        url = db_config.DATABASE_URL

        if not database_exists(url):
            logger.info("Database does not exist. Creating...")
            create_database(url)
            logger.info("Database created.")
        else:
            logger.info("Database already exists.")
        
        engine = create_engine(url, echo=True)
        logger.info("Database engine created.")
        return engine

    def create_session(self, engine: Engine) -> scoped_session[Session]:
        """
        Create Session.

        Args:
            engine (Engine): Engine of submitted database.

        Returns:
            scoped_session[Session]: Current Session object.
        """
        logger.info("Creating database session...")
        session = scoped_session(sessionmaker(bind=engine))
        logger.info("Session created.")
        return session
