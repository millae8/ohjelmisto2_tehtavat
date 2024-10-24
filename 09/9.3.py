# tehtävä 3

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

a1 = Auto('ABC-123', 142, 60, 2000)

a1.kulje(1.5)
print(f'Auton kulkema matka on {a1.matka} km.')