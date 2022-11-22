import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

        self.maito = Tuote("Maito", 3)
        self.mehu = Tuote("Mehu", 4)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)


    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)


    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(), 3)


    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.mehu)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)


    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_hinta_tuotteiden_yhteishinta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.mehu)
        self.assertEqual(self.kori.hinta(), 7)


    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)


    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_hinta_tuotteiden_yhteishinta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(), 6)


    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)


    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.maito)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(self.maito.nimi(), ostos.tuotteen_nimi())
        self.assertEqual(ostos.lukumaara(), 1)


    def test_kahden_eri_tuotteen_lisäämisen_jälkeen_ostoskori_sisältää_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.mehu)

        ostos = self.kori.ostokset()
        self.assertEqual(len(ostos), 2)


    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskori_sisältää_yhden_ostoksen(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        ostos = self.kori.ostokset()

        self.assertEqual(len(ostos), 1)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)


    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskorissa_tuote_oikealla_nimella_ja_maaralla(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(self.maito.nimi(), ostos.tuotteen_nimi())
        self.assertEqual(self.kori.tavaroita_korissa(), 2)


    def test_poistetaan_toinen_kahdesta_samasta_tuotteesta_toinen_jää(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.kori.poista_tuote(self.maito)

        ostos = self.kori.ostokset()

        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.assertEqual(len(ostos), 1)


    def test_korista_poistetaan_ainoa_tuote_kori_jää_tyhjäksi(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.poista_tuote(self.maito)

        ostos = self.kori.ostokset()

        self.assertEqual(len(ostos), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)


    def test_metodi_tyhjenna_tyhjentaa_korin(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.mehu)
        self.kori.tyhjenna()

        ostos = self.kori.ostokset()

        self.assertEqual(len(ostos), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)