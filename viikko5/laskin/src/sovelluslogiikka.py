class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen = 0

    class Summa:
        def __init__(self, sovellus, syote):
            self.sovellus = sovellus
            self.syote = syote

        def suorita(self):
            self.sovellus.edellinen = self.sovellus.tulos
            self.sovellus.tulos += int(self.syote())

    class Erotus:
        def __init__(self, sovellus, syote):
            self.sovellus = sovellus
            self.syote = syote

        def suorita(self):
            self.sovellus.edellinen = self.sovellus.tulos
            self.sovellus.tulos -= int(self.syote())

    class Nollaus:
        def __init__(self, sovellus):
            self.sovellus = sovellus

        def suorita(self):
            self.sovellus.tulos = 0

    class Kumoa:
        def __init__(self, sovellus, edellinen):
            self.sovellus = sovellus
            self.edellinen = edellinen

        def suorita(self):
            self.sovellus.tulos = self.sovellus.edellinen