# moduuli 11, tehtävä 1

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f'Julkaisun nimi on {self.nimi}.')

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Sen kirjoittaja on {self.kirjoittaja} ja sivumäärä on {self.sivumäärä}.')

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Sen päätoimittaja on {self.päätoimittaja}.')

k = Kirja('Hytti n:o 6', 'Rosa Liksom', 200)
l = Lehti('Aku Ankka', 'Aki Hyyppä')

k.tulosta_tiedot()
l.tulosta_tiedot()