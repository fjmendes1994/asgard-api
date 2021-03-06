#encoding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from hollowman.conf import HOLLOWMAN_DB_URL, HOLLOWMAN_DB_ECHO

engine = create_engine(HOLLOWMAN_DB_URL, echo=HOLLOWMAN_DB_ECHO)
HollowmanSession = sessionmaker(bind=engine)

BaseModel = declarative_base()

from .user import User
from .account import Account
from .user_has_account import UserHasAccount
