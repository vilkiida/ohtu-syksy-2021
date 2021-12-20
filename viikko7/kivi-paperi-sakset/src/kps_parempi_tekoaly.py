from tekoaly_parannettu import TekoalyParannettu
from kps import KPS

class KPSParempiTekoaly(KPS):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)
    
    def pelaa(self):
        super().pelaa()

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        return tokan_siirto