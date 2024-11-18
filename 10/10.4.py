# moduuli 10 tehtävä 4
import random

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

#--------------------------------------------------------10.4-------------------------------------------------------
class Kilpailu:
    def __init__(self, nimi, pituus):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = []

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        for each in self.autot:
            each.print_info()

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= 8000:
                print("Kilpailu on ohi.")
                return True
        return False

kilpailu = Kilpailu("Suuri romuralli", 8000)

for i in range(1, 11):
    auto = Auto(f'ABC-{i}', random.randint(100, 200))
    kilpailu.autot.append(auto)

while kilpailu.kilpailu_ohi() == False:
    kilpailu.tunti_kuluu()
    kilpailu.tulosta_tilanne()

kilpailu.tulosta_tilanne()