from tekoaly import Tekoaly
from kps import KPS


class KPSTekoaly(KPS):
    def __init__(self):
        self.tekoaly = Tekoaly()
    def pelaa(self):
        super().pelaa()

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto