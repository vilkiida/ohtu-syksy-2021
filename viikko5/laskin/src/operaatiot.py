class Summa:
    def __init__(self, sovellus, arvo):
        self.sovellus = sovellus
        self.arvo = arvo()
    def suorita(self):
        self.sovellus.plus(int(float(self.arvo)))

class Erotus:
    def __init__(self, sovellus, arvo):
        self.sovellus = sovellus
        self.arvo = arvo()
    def suorita(self):
        self.sovellus.miinus(int(float(self.arvo)))

class Nollaus:
    def __init__(self, sovellus, arvo):
        self.sovellus = sovellus
        self.arvo = arvo()
    def suorita(self):
        self.sovellus.nollaa()

class Kumoa:
    def __init__(self, sovellus, arvo):
        self.sovellus = sovellus
        self.arvo = arvo()
    def suorita(self):
        pass