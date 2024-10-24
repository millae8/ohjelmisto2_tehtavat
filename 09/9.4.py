# tehtävä 4
import random

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

for i in range(1, 11):
    auto = Auto(f'ABC-{i}', random.randint(100, 200))
    autot.append(auto)

race = True

while race:
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)
        if auto.matka >= 10000:
            race = False

for each in autot:
    each.print_info()