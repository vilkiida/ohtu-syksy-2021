from kps import KPS

class KPSPelaajaVsPelaaja(KPS):
    def pelaa(self):
        super().pelaa()

    def _toisen_siirto(self, ensimmaisen_siirto):
        toisen_siirto = input("Toisen pelaajan siirto: ")
        return toisen_siirto