from datetime import date

class Kunde:
    def __init__(self, vorname, nachname, guthaben=0):
        self.vorname = vorname
        self.nachname = nachname
        self.guthaben = guthaben
        self.reg_datum = date.today()
        self.alle_attribute = vorname, nachname, guthaben

    def einzahlen(self, betrag):
        self.guthaben = self.guthaben + betrag

    def auszahlen(self, betrag):
        if betrag > self.guthaben:
            raise ValueError("Nicht genügend Guthaben!")
        self.guthaben = self.guthaben - betrag

kunde1 = Kunde("Max", "Mustermann", 2000)
kunde2 = Kunde("Martina", "Musterfrau")

print(kunde1.alle_attribute)
print(kunde2.reg_datum)
#print(kunde1.__dict__)

kunde1.einzahlen(500)
print(kunde1.guthaben) # 2500
#kunde1.auszahlen(3000) # ValueError: Nicht genügend Guthaben!
#print(kunde1.guthaben) # 2500
kunde1.auszahlen(200)
print(kunde1.guthaben) # 2300   