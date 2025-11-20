import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_URI = "sqlite:///names.db"
Base = declarative_base()
engine = create_engine(DB_URI, future=True)
Session = sessionmaker(bind=engine, future=True)

class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

def init_db():
    Base.metadata.create_all(engine)

def add_name(name):
    with Session() as s:
        p = Person(name=name)
        s.add(p)
        s.commit()
        s.refresh(p)
        return p.id

def list_names():
    with Session() as s:
        return [(p.id, p.name) for p in s.query(Person).order_by(Person.id).all()]

def main():
    if len(sys.argv) < 2:
        print("Usage: python mini2ai.py init | add <name> | list")
        return
    cmd = sys.argv[1].lower()
    if cmd == "init":
        init_db()
        print("DB initialized")
    elif cmd == "add" and len(sys.argv) >= 3:
        name = " ".join(sys.argv[2:])
        print(f"Inserted id={add_name(name)} name={name!r}")
    elif cmd == "list":
        for id_, name in list_names():
            print(id_, name)
    else:
        print("Usage: python mini2ai.py init | add <name> | list")

if __name__ == "__main__":
    main()
