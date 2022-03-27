from sqlalchemy import MetaData
from sqlalchemy import Table, Column, String, Integer, ForeignKey
 
meta = MetaData()
users = Table('users', meta,
    Column('id', Integer, primary_key=True),
    Column('username', String(20), nullable=False),
    Column('email', String(60), nullable=False, unique=True),
    Column('password', String(20), nullable=False)
)