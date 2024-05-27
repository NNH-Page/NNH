from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

Base = declarative_base()
DB_ENGINE = create_engine("sqlite:///D:\\Users\\Marianela\\Desktop\\API ROL\\Database\\Database_Rol")
DB_ENGINE.connect()
Cursor = sessionmaker(bind = DB_ENGINE)
Cursor = Cursor()