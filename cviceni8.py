import json


class InvalidData(Exception):
    pass


class Osoba:
    def __init__(self, jmeno, telefon, email):
        self.__jmeno = jmeno
        self.__telefon = telefon
        self.__email = email

    @property
    def jmeno(self):
        return self.__jmeno

    @jmeno.setter
    def jmeno(self, hodnota):
        if hodnota.isalpha():
           self.__jmeno = hodnota
        else:
            raise InvalidData("Jmeno musí obsahovat jen písmena")

    @property
    def telefon(self):
        return self.__telefon

    @telefon.setter
    def telefon(self, hodnota):
        if hodnota.isnumeric():
           self.__telefon = hodnota
        else:
             raise InvalidData("Telefon musí obsahovat pouze čísla!")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, hodnota):
        if "@" not in hodnota:
            raise InvalidData("musí obsahovat @")
        if "." not in hodnota:
            raise InvalidData("Musí obsahovat tečku")
        if hodnota.replace("@", "").replace (".", "").isalnum():
            self.__email = hodnota
        else:
            raise InvalidData("Email může použivat jen čísla a písmena")

    def __str__(self):
        return f"Osoba: {self.jmeno}, {self.telefon}, {self.email}"

    def __repr__(self):
        return f"Osoba: {self.jmeno}, {self.telefon}, {self.email}"

    @classmethod
    def load_json_data(cls, data):
         if 'jmeno' not in data or 'telefon' not in data or 'email' not in data:
            return None
        return cls(data['jmeno'], data['telefon'], data['email'])

if __name__ == "__main__":
    
    o = Osoba("Jan Novak", "004225877845", "jan@novak.cz")
    print(o)
    o.jmeno = "4357253"
    o.telefon = "asjkdfhbasikfh"
    o.email = "xxx1"
    osoby = []

    with open("osoby.json") as fp:
        data = json.loads(fp.read())
        for record in data:
            osoby.append(osoba.load_data(record))

    print(osoby)