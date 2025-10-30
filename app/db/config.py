from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from os import path
from fastapi import Depends
from typing import Annotated

# VARIABLES

BASE_DIR        = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

DATABASE_NAME   = "sqlite.db"

DB_PATH         = path.join(BASE_DIR, DATABASE_NAME)

DATABASE_URL    = f"sqlite+aiosqlite:///{DB_PATH}"



# DATABASE CONNECTION 
engine          = create_async_engine(DATABASE_URL, echo=True)

async_session   = async_sessionmaker(bind=engine, expire_on_commit=False)



# # CREATE SESSION
# async def get_db():
#     async with async_session() as session:
#         yield session

# SessionDep      = Annotated[AsyncSession, Depends(get_db)] 


# FOR NON-PROD CODE -- DEBBUGING
async def get_db():
    session = async_session()
    print(f'creating new asyncSession: {id(session)}')

    try: 
        async with session:
            yield session
        print(f"session committed and closed: {id(session)}")
    except Exception as e: 
        print(f"Error in session: {id(session)}, rolling back: {str(e)}")
        await session.rollback()
        raise
    finally:
        await session.close()
        print(f"session explicitly closed: {id(session)}")



SessionDep      = Annotated[AsyncSession, Depends(get_db)] 