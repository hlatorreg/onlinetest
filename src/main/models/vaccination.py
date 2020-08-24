from .base import Base, db


class Vaccination(Base):

    __tablename__ = "vaccinations"

    rut = db.Column(db.String(15), unique=False, nullable=False)
    dose = db.Column(db.Float, unique=False, nullable=False)
    date = db.Column(db.DateTime, unique=False, nullable=False)
    drug = db.Column(db.Integer, db.ForeignKey("drugs.id"), nullable=False)

    def check_rut(self):
        try:
            self.__clean_rut()
            print(self.rut)
            dv = self.rut[-1:]
            digitos = map(int, reversed(str(self.rut[:-1])))
            serie = range(2, 8)
            suma = 0
            for i, d in enumerate(digitos):
                suma += d * serie[i] if i < len(serie) else d * serie[i - len(serie)]
            calculated_dv = (-suma) % 11
            if dv == str(calculated_dv) or dv == "K" and calculated_dv == 10:
                return True
            return False
        except Exception:
            return False

    def check_dose(self):
        return self.dose >= 0.15 and self.dose <= 1.0

    def save(self):
        if not self.check_rut():
            return False, "Rut is invalid"
        if not self.check_dose():
            return False, "Dose is outside permited range"
        try:
            db.session.add(self)
            db.session.commit()
            return self, None
        except Exception as exc:
            return False, "The drug you are referencing doesn't exist"

    def __clean_rut(self):
        self.rut = self.rut.replace(".", "")
        self.rut = self.rut.replace("-", "")
