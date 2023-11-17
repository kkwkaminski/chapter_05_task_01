from faker import Faker

class Wizytowka:
    def __init__(self, imie, nazwisko, firma, stanowisko, email, telefon):
        self.imie = imie
        self.nazwisko = nazwisko
        self.firma = firma
        self.stanowisko = stanowisko
        self.email = email
        self.telefon = telefon

def generuj_wizytowke():
    fake = Faker()
    imie = fake.first_name()
    nazwisko = fake.last_name()
    firma = fake.company()
    stanowisko = fake.job()
    email = fake.email()
    telefon = fake.phone_number()

    wizytowka = Wizytowka(imie, nazwisko, firma, stanowisko, email, telefon)
    return wizytowka

# Przykład użycia
moja_wizytowka = generuj_wizytowke()
print(f"Imię: {moja_wizytowka.imie}")
print(f"Nazwisko: {moja_wizytowka.nazwisko}")
print(f"Firma: {moja_wizytowka.firma}")
print(f"Stanowisko: {moja_wizytowka.stanowisko}")
print(f"Email: {moja_wizytowka.email}")
print(f"Telefon: {moja_wizytowka.telefon}")