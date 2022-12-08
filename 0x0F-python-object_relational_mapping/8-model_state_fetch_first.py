#!/usr/bin/python3
"""Uses SQLAlchemy. prints the first State object from the database \
hbtn_0e_6_usa from the database hbtn_0e_6_usa.
takes 3 arguments: mysql username, mysql password and database name.
"""

from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:\
                             3306/{}'.format(sys.argv[1], sys.argv[2],
                                             sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
    session.close()
