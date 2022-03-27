from sqlalchemy import MetaData, create_engine
from sqlalchemy import Table, Column, String, Integer, ForeignKey
 
meta = MetaData()
engine = create_engine('sqlite:///site.db')

users = Table('users', meta,
    Column('id', Integer, primary_key=True),
    Column('username', String(20), nullable=False),
    Column('email', String(60), nullable=False, unique=True),
    Column('password', String(20), nullable=False)
)