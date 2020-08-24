VALID_RUTS = [
    "6401601-6",
    "17983942-3",
    "24019664-6",
    "9687794-3",
    "9.703.243-2",
    "8340156-7",
    "19.884.657-0",
    "24347518-k",
    "18975463-9",
    "10855348-0",
]


INVALID_RUTS = [
    "0164192-9",
    "6003940-1",
    "15590559-I",
    "1631711-9",
    "18540949-8",
    "13149326*6",
    "220853-4",
    "12357051,0",
    "11167910-0",
    "5030089.2",
]

DOSE = 0.5
DATE = "2020-02-02T02:02:02"
DRUG_CODE = "test"


def test_valid_ruts_save(vaccination, drug):
    for rut in VALID_RUTS:
        vaccination.rut = rut
        vaccination.dose = DOSE
        vaccination.date = DATE
        vaccination.drug = drug.id
        result = vaccination.check_rut()
        assert result == True


def test_invalid_ruts_save(vaccination, drug):
    for rut in INVALID_RUTS:
        vaccination.rut = rut
        vaccination.dose = DOSE
        vaccination.date = DATE
        vaccination.drug = drug.id
        result = vaccination.check_rut()
        assert result == False
