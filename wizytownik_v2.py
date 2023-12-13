from faker import Faker

class BaseContact:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

    def contact(self):
        print(f"Wybieram numer {self.telefon} i dzwonię do {self.imie} {self.nazwisko}")

    @property
    def label_length(self):
        return len(f"{self.imie} {self.nazwisko}")

class BusinessContact(BaseContact):
    def __init__(self, imie, nazwisko, telefon, email, stanowisko, firma, telefon_sluzbowy):
        super().__init__(imie, nazwisko, telefon, email)
        self.stanowisko = stanowisko
        self.firma = firma
        self.telefon_sluzbowy = telefon_sluzbowy

    def contact(self):
        print(f"Wybieram numer {self.telefon_sluzbowy} i dzwonię do {self.imie} {self.nazwisko} w firmie {self.firma}")

def create_contacts(rodzaj, ilosc=5):
    fake = Faker()
    contacts = []

    for _ in range(ilosc):
        imie = fake.first_name()
        nazwisko = fake.last_name()
        telefon = fake.phone_number()
        email = fake.email()

        if rodzaj == 'base':
            contact = BaseContact(imie, nazwisko, telefon, email)
        elif rodzaj == 'business':
            stanowisko = fake.job()
            firma = fake.company()
            telefon_sluzbowy = fake.phone_number()
            contact = BusinessContact(imie, nazwisko, telefon, email, stanowisko, firma, telefon_sluzbowy)

        contacts.append(contact)

    return contacts

# Wywołanie
base_contacts = create_contacts('base')
business_contacts = create_contacts('business')

for contact in base_contacts:
    contact.contact()
    print(f"Długość imienia i nazwiska: {contact.label_length}")

for contact in business_contacts:
    contact.contact()
    print(f"Długość imienia i nazwiska: {contact.label_length}")