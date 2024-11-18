#moduuli 11, tehtävä 2

autot = []

class Auto:

    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def print_info(self):
        print(f'Auton rekisteritunnus on {self.rekisteritunnus}, huippunopeus on {self.huippunopeus}, tämänhetkinen nopeus on {self.nopeus} ja sen kuljettu matka on {self.matka}.')
        return

    def kiihdytä(self, muutos):
        self.nopeus = self.nopeus + muutos
        if self.nopeus <= 0:
            self.nopeus = 0
        if self.nopeus >= self.huippunopeus:
            self.nopeus = self.huippunopeus
        return

    def kulje(self, tunti):
        self.matka = self.matka + self.nopeus * tunti
        return
#--------------------------------------------------11.2---------------------------------------------------------
class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti, nopeus):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus, nopeus)

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki, nopeus):
        self.bensatankki = bensatankki
        super().__init__(rekisteritunnus, huippunopeus, nopeus)

autot.append(Sähköauto("ABC-15", "180km/h", "52.5kWh", 69))
autot.append(Polttomoottoriauto("ACD-123", "165km/h", "32.3l", 87))

autot[0].kulje(3)
autot[1].kulje(3)

for each in autot:
    each.print_info()