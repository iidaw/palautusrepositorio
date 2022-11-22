from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        pass
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.tuotteet = {}

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        maara = 0
        
        for tuote in self.tuotteet.values():
            maara += tuote.lukumaara()
        return maara


    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        hinta = 0
        
        for tuote in self.tuotteet.values():
            hinta += tuote.hinta()

        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        if not lisattava.nimi in self.tuotteet:
            self.tuotteet[lisattava.nimi] = Ostos(lisattava)
        else: 
            self.tuotteet[lisattava.nimi].muuta_lukumaaraa(1) 

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
