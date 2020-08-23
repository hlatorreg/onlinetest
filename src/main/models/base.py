from main import db


class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except Exception as exc:
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as exc:
            return False

    def update(self):
        try:
            db.session.commit()
            return True
        except Exception as exc:
            return False
