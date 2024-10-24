# tehtävä 2

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
            print(f'Auton nopeus on tällä hetkellä {self.nopeus} km/h, auto on pysähtynyt.')
        if self.nopeus >= self.huippunopeus:
            print('Huippunopeus ylitetty, ei mahdollinen.')
        return

a1 = Auto('ABC-123', 142)

a1.kiihdytä(30)
a1.kiihdytä(70)
a1.kiihdytä(50)
print(f'Auton tämänhetkinen nopeus on: {a1.nopeus} km/h')
a1.kiihdytä(-200)