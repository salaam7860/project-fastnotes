from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from os import path

# CREATE PATH 
BASE_DIR = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

db_path = path.join(BASE_DIR, "sqlite.db")


DATABASE_URL = f"sqlite+aiosqlite:///{db_path}"

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = async_sessionmaker(bind=engine, expire_on_commit=False)