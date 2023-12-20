from asyncio import futures
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

connection_string = "cockroachdb://root@127.0.0.1:26257/investor_bulletin?sslmode=disable"
engine = create_engine(connection_string, connect_args={}, future=True)

# Create a configured "Session" class
Session = sessionmaker(bind=engine,future=True,autocommit=False,autoflush=False)
Base = declarative_base()


# DB Utils
def get_session():
    db = Session()
    try:
        yield db
    finally:
        db.close()
