from .base import Base, db


class Vaccination(Base):

    __tablename__ = "vaccinations"

    rut = db.Column(db.String(15), unique=False, nullable=False)
    dose = db.Column(db.Float, unique=False, nullable=False)
    date = db.Column(db.DateTime, unique=False, nullable=False)
    drug = db.Column(db.String(255), unique=False, nullable=False)

    @classmethod
    def check_rut(cls, rut):
        dv = rut[-1:]
        digitos = map(int, reversed(str(rut[:-1])))
        serie = range(2, 8)
        suma = 0
        for i, d in enumerate(digitos):
            suma += d * serie[i] if i < len(serie) else d * serie[i - len(serie)]
        calculated_dv = (-suma) % 11
        if dv == str(calculated_dv) or dv == "K" and calculated_dv == 10:
            return True
        return False

