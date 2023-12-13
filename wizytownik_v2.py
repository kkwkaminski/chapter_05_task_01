from faker import Faker

class Wizytowka:
    def __init__(self, imie, nazwisko, firma, stanowisko, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.firma = firma
        self.stanowisko = stanowisko
        self.email = email

    def contact(self):
        print(f"Kontaktuję się z {self.imie} {self.nazwisko}, {self.stanowisko}, e-mail: {self.email}")

    @property
    def dlugosc_imienia_nazwiska(self):
        return len(self.imie) + len(self.nazwisko)

def generuj_wizytowki(ilosc=5):
    fake = Faker()
    wizytowki = []

    for _ in range(ilosc):
        imie = fake.first_name()
        nazwisko = fake.last_name()
        firma = fake.company()
        stanowisko = fake.job()
        email = fake.email()

        wizytowka = Wizytowka(imie, nazwisko, firma, stanowisko, email)
        wizytowki.append(wizytowka)

    return wizytowki

def wyswietl_wizytowki(wizytowki):
    for wizytowka in wizytowki:
        print(f"{wizytowka.imie} {wizytowka.nazwisko} - {wizytowka.email}")


lista_wizytowek = generuj_wizytowki()


wyswietl_wizytowki(lista_wizytowek)


for wizytowka in lista_wizytowek:
    wizytowka.contact()
    print(f"Długość imienia i nazwiska: {wizytowka.dlugosc_imienia_nazwiska}\n")