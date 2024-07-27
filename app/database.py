from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# db_user = "postgres"
# db_password = "atypicalesper"
# db_name = "shoonyaLife"
# SQLALCHEMY_DATABASE_URL = f"postgresql://${db_user}:{db_password}@localhost/{db_name}"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:atypicalesper@localhost/shoonyaLife"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def init_db():
    Base.metadata.create_all(bind=engine)
