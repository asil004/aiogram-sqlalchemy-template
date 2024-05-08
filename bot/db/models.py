# from datetime import datetime
#
# from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, ForeignKey, Date, Time
#
# from sqlalchemy.orm import relationship
# from bot.db.base import Base
#
#
# class Company(Base):
#     __tablename__ = 'company'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     channel_id = Column(Integer, unique=True, autoincrement=False, nullable=False)
#
#
# class User(Base):
#     __tablename__ = "user"
#
#     user_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False, nullable=False)
#     full_name = Column(String)
#     role = Column(String, default='worker')  # also have "inspector"
#     company_id = Column(Integer, ForeignKey('company.id'))
#     company = relationship("Company", back_populates="user")
#
#
# class Came(Base):
#     __tablename__ = 'came'
#
#     id = Column(Integer, primary_key=True)
#     current_date = Column(Date, default=datetime.now().date)
#     came_date = Column(Time, default=datetime.now().time())
#     user_id = Column(BigInteger, ForeignKey('user.user_id'))
#     user = relationship("User", back_populates="user_came")
#
#
# class Left(Base):
#     __tablename__ = 'left'
#
#     id = Column(Integer, primary_key=True)
#     current_date = Column(Date, default=datetime.now().date)
#     left_date = Column(Time, default=datetime.now().time())
#     user_id = Column(BigInteger, ForeignKey('user.user_id'))
#     user = relationship("User", back_populates="user_left")
