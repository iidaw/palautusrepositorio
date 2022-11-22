from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.tuotteet = {}


    def tavaroita_korissa(self):
        maara = 0
        
        for tuote in self.tuotteet.values():
            maara += tuote.lukumaara()

        return maara


    def hinta(self):
        hinta = 0
        
        for tuote in self.tuotteet.values():
            hinta += tuote.hinta()

        return hinta


    def lisaa_tuote(self, lisattava: Tuote):
        if not lisattava.nimi in self.tuotteet:
            self.tuotteet[lisattava.nimi] = Ostos(lisattava)
        else: 
            self.tuotteet[lisattava.nimi].muuta_lukumaaraa(1) 


    def poista_tuote(self, poistettava: Tuote):
        if poistettava.nimi in self.tuotteet:
            self.tuotteet[poistettava.nimi].muuta_lukumaaraa(-1)

        if self.tuotteet[poistettava.nimi].lukumaara() == 0:
            self.tuotteet.pop(poistettava.nimi)


    def tyhjenna(self):
        self.tuotteet = {}


    def ostokset(self):
        ostos_oliot = []

        for tuote in self.tuotteet.values():
            ostos_oliot.append(tuote)

        return ostos_oliot
