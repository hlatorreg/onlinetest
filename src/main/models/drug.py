from .base import Base, db


class Drug(Base):

    __tablename__ = "drugs"

    name = db.Column(db.String(255), unique=False, nullable=False)
    code = db.Column(db.String(10), unique=True)
    description = db.Column(db.String(255), unique=False, nullable=False)
