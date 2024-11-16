# moduuli 10, tehtävä 2

class Hissi:
    def __init__(self, nimi, kerros=1, alin_kerros=1, ylin_kerros=10):
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

# --------------------------------------------------TALO----------------------------------------------------

class Talo:
    def __init__(self, hissit, alin_kerros=1, ylin_kerros=10):
        self.hissit = hissit
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

    def aja_hissiä(self, hissin_numero, kohdekerros):
        self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)

t1 = Talo([Hissi("h1"), Hissi("h2")])
t1.aja_hissiä(0, 6)
print(f'{t1.hissit[0].nimi} on kerroksessa {t1.hissit[0].kerros}.')