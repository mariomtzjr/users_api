from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "github_users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    avatar_url = Column(String)
    type = Column(String(50))
    url = Column(String)
    
    def __init__(self, username, avatar_url, type, url):
        self.username = username
        self.avatar_url = avatar_url
        self.type = type
        self.url = url

    def __repr__(self):
        return f'User({self.username})'

    def __str__(self):
        return f'{self.username}'