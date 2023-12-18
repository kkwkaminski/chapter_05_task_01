from faker import Faker

class BaseContact:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email
        self._label_length = None

    def contact(self):
        print(f"Wybieram numer {self.telefon} i dzwonię do {self.imie} {self.nazwisko}")

    @property
    def label_length(self):
        if self._label_length is None:
            self._label_length = len(f"{self.imie} {self.nazwisko}")
        return self._label_length

class BusinessContact(BaseContact):
    def __init__(self, stanowisko, firma, telefon_sluzbowy, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stanowisko = stanowisko
        self.firma = firma
        self.telefon_sluzbowy = telefon_sluzbowy

    def contact(self):
        print(f"Wybieram numer {self.telefon_sluzbowy} i dzwonię do {self.imie} {self.nazwisko} w firmie {self.firma}")

    @property
    def label_length(self):
        if self._label_length is None:
            self._label_length = len(f"{self.imie} {self.nazwisko}")
        return self._label_length

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
            contact = BusinessContact(stanowisko=stanowisko, firma=firma, telefon_sluzbowy=telefon_sluzbowy, imie=imie, nazwisko=nazwisko, telefon=telefon, email=email)

        contacts.append(contact)

    return contacts

if __name__ == "__main__":
    base_contacts = create_contacts('base')
    business_contacts = create_contacts('business')

    for contact in base_contacts:
        contact.contact()
        print(f"Długość imienia i nazwiska: {contact.label_length}")

    for contact in business_contacts:
        contact.contact()
        print(f"Długość imienia i nazwiska: {contact.label_length}")