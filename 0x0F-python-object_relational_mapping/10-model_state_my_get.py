#!/usr/bin/python3
"""
All states via SQLAlchemy
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    data = session.query(State).filter(State.name == argv[4]).one_or_none()
    if data is None:
        print("Not found")
    else:
        print("{}".format(data.id))
    session.close()
