#! /usr/bin/env python3

import sqlalchemy as sql
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.orm as orm

import os.path

Base = declarative.declarative_base()

class Track(Base):
    __tablename__ = 'tracks'

    id              = sql.Column(sql.Integer, primary_key = True)
    title           = sql.Column(sql.Text, nullable = False)
    artist          = sql.Column(sql.Text, nullable = False)
    album           = sql.Column(sql.Text, nullable = False)
    tracknumber     = sql.Column(sql.Integer, nullable = False)
    nickname        = sql.Column(sql.Text)
    opus_number     = sql.Column(sql.Integer)
    work_number     = sql.Column(sql.Integer)
    catalog_id      = sql.Column(sql.Text)
    key             = sql.Column(sql.Text)
    movement        = sql.Column(sql.Integer)
    movement_name   = sql.Column(sql.Text)
    composer        = sql.Column(sql.Text)

session = None
def init():
    create_new = os.path.isfile('tracks.db')
    print(create_new)

    engine = sql.create_engine('sqlite:///tracks.db')

    if create_new:
        Base.metadata.create_all(engine)

    Base.metadata.bind = engine

    DBSession = orm.sessionmaker(bind = engine)

    global session
    session = DBSession()
