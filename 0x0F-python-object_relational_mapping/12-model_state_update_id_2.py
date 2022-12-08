#!/usr/bin/python3
"""Uses SQLAlchemy. Adds the State object \
“Louisiana” to the database hbtn_0e_6_usa
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

    new_state = session.query(State).filter_by(id=2).first()
    new_state.name = "New Mexico"
    session.commit()
    session.close()
