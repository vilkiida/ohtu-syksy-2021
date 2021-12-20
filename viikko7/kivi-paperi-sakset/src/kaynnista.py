from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_tekoaly import KPSTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
def kaynnista(tyyppi):
    if tyyppi == "kaksinpeli":
        peli = KPSPelaajaVsPelaaja()
    elif tyyppi == "yksinpeli":
        peli = KPSTekoaly()
    elif tyyppi == "haastava_yksinpeli":
        peli = KPSParempiTekoaly()
    else:
        return
    peli.pelaa()


