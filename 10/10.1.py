# moduuli 10, tehtävä 1

class Hissi:
    def __init__(self, nimi="h", kerros=1, alin_kerros=1, ylin_kerros=10):
        self.nimi = nimi
        self.kerros = kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

    def siirry_kerrokseen(self, kerros):
        while kerros != self.kerros:
            if kerros < self.kerros:
                self.kerros_alas()
            if kerros > self.kerros:
                self.kerros_ylös()

    def kerros_ylös(self):
        self.kerros += 1
        print(f'{self.nimi} on nyt kerroksessa {self.kerros}.')
        return

    def kerros_alas(self):
        self.kerros -= 1
        print(f'{self.nimi} on nyt kerroksessa {self.kerros}.')
        return

h1 = Hissi()
h1.siirry_kerrokseen(5)
h1.siirry_kerrokseen(1)