from .base import Base, db


class Drug(Base):

    __tablename__ = "drugs"

    name = db.Column(db.String(255), unique=False, nullable=False)
    code = db.Column(db.String(10), unique=True)
    description = db.Column(db.String(255), unique=False, nullable=False)

    def __repr__(self):
        return f"<id={self.id}, name={self.name}, code={self.code}, description={self.description}>"
