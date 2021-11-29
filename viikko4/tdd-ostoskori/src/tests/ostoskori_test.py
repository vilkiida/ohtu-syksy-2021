import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.tuote = Tuote("maito", 3)
        self.tuote2 = Tuote("leipä", 4)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        tyhjia = True
        if self.kori.hinta() != 0:
            tyhjia = False
        if self.kori.tavaroita_korissa() != 0:
            tyhjia = False
        self.assertEqual(tyhjia, True)
    
    def test_tuotteen_lisaamisen_jalkeen_korissa_on_1_tavara(self):
        self.kori.lisaa_tuote(self.tuote)
        self.assertEqual(self.kori.tavaroita_korissa(),1)
    
    def test_1_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.tuote)
        self.assertEqual(self.kori.hinta(), 3)
    def test_2_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_2_tavaraa(self):
        self.kori.lisaa_tuote(self.tuote)
        self.kori.lisaa_tuote(self.tuote2)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    def test_2_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_tuotteiden_hintojen_summa(self):
        self.kori.lisaa_tuote(self.tuote)
        self.kori.lisaa_tuote(self.tuote2)
        yhteishinta = self.tuote.hinta() + self.tuote2.hinta()
        self.assertEqual(self.kori.hinta(), yhteishinta)
    def test_2_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_2_tavaraa(self):
        self.kori.lisaa_tuote(self.tuote)
        self.kori.lisaa_tuote(self.tuote)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    def test_2_saman_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_2x_ostoksen_hinta(self):
        self.kori.lisaa_tuote(self.tuote)
        self.kori.lisaa_tuote(self.tuote)
        yhteishinta = 2*self.tuote.hinta()
        self.assertEqual(self.kori.hinta(), yhteishinta)
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_yhden_ostoksen(self):
        self.kori.lisaa_tuote(self.tuote)
        ostosten_maara = len(self.kori.ostokset())
        self.assertEqual(ostosten_maara, 1)
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_ostoksen_jolla_sama_nimi_kuin_tuotteella_ja_lukumaara_1(self):
        self.kori.lisaa_tuote(self.tuote)
        ostokset = self.kori.ostokset()
        oikein = True
        if ostokset[0].tuotteen_nimi() != self.tuote.nimi():
            oikein = False
        if ostokset[0].lukumaara() != 1:
            oikein = False
        self.assertEqual(oikein, True)
    def test_kahden_eri_tuoteen_lisaamisen_jalkeen_ostoskori_sisaltaa_2_ostosta(self):
        self.kori.lisaa_tuote(self.tuote)
        self.kori.lisaa_tuote(self.tuote2)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_1_ostoksen(self):
        self.kori.lisaa_tuote(self.tuote)
        self.kori.lisaa_tuote(self.tuote)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_ostoksen_jolla_sama_nimi_kuin_tuotteella_ja_lukumaara_on_2(self):
        self.kori.lisaa_tuote(self.tuote)
        self.kori.lisaa_tuote(self.tuote)
        ostokset = self.kori.ostokset()
        virhe = False
        if ostokset[0].tuotteen_nimi() != self.tuote.nimi():
            virhe = True
        if ostokset[0].lukumaara() != 2:
            virhe = True
        self.assertEqual(virhe, False)
    
    def test_jos_korissa_on_2_samaa_tuotetta_ja_toinen_poistetaan_jaa_koriin_ostos_jossa_on_tuotetta_1(self):
        self.kori.lisaa_tuote(self.tuote)
        self.kori.lisaa_tuote(self.tuote)
        self.kori.poista_tuote(self.tuote)
        ostokset = self.kori.ostokset()
        self.assertEqual(ostokset[0].lukumaara(), 1)