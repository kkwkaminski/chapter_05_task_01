from faker import Faker

class Wizytowka:
    def __init__(self, imie, nazwisko, firma, stanowisko, email, telefon):
        self.imie = imie
        self.nazwisko = nazwisko
        self.firma = firma
        self.stanowisko = stanowisko
        self.email = email
        self.telefon = telefon

    @property
    def dlugosc_imienia_nazwiska(self):
        return len(self.imie) + len(self.nazwisko)
    
    def contact(self):
        print(f"Kontaktuję się z {self.imie} {self.nazwisko}, {self.stanowisko}, e-mail: {self.email}")

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


moja_wizytowka = generuj_wizytowke()
moja_wizytowka.contact()
print(f"Długość imienia i nazwiska: {moja_wizytowka.dlugosc_imienia_nazwiska}")