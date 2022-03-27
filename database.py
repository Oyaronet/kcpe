from sqlalchemy import MetaData, create_engine
from sqlalchemy import Table, Column, String, Integer, ForeignKey
 
meta = MetaData()
engine = create_engine('postgres://epmswlywsgfgec:a471edc1aa9d0338b9cb4de98802af9a10189f6a\
576b1311fa17300dbc26bf7a@ec2-44-194-92-192.compute-1.\
amazonaws.com:5432/deramp098sjfju')

users = Table('users', meta,
    Column('id', Integer, primary_key=True),
    Column('username', String(20), nullable=False),
    Column('email', String(60), nullable=False, unique=True),
    Column('password', String(20), nullable=False)
)