#!/usr/bin/python3
"""
All states via SQLAlchemy
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    data = session.query(State.name, City.id, City.name)\
                  .select_from(State).join(City, City.state_id == State.id)\
                                     .order_by(City.id)\
                                     .all()

    for row in data:
        print("{}: ({}) {}".format(row[0], row[1], row[2]))
    session.close()
