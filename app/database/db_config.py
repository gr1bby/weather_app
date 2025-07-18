from sqlalchemy.ext.declarative import declarative_base

from app.core.config import settings


class DBVars:
    DATABASE_URL: str = (
        f"postgresql://{settings.DB_USER}:{settings.DB_PASS}@"
        f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
    )
    
    Base = declarative_base()


db_config = DBVars()
