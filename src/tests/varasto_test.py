import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)


    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uudella_varastolla_on_negatiivinen_tilavuus(self):
        varasto2 = Varasto(-5, 0)
        self.assertAlmostEqual(varasto2.tilavuus, 0)

    def test_uudella_varastolla_on_negatiivinen_saldo(self):
        saldo_nolla = Varasto(-5, -5)
        self.assertAlmostEqual(saldo_nolla.saldo, 0)

    def test_lisaa_varastoon_liikaa(self):
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ota_negatiivinen_maara_varastosta(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-10), 0)

    def test_ota_yli_saldon_varastosta(self):
        uusi_varasto = Varasto(100, 10)
        self.assertAlmostEqual(uusi_varasto.ota_varastosta(20), 10)
        self.assertAlmostEqual(uusi_varasto.saldo, 0)

    def test_lisaa_negatiivinen_maara(self):
        uusi_varasto = Varasto(100, 10)
        uusi_varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(uusi_varasto.saldo(10), 10)

    def test_oikean_tekstin_palautus(self):
        uusi_varasto = Varasto(100, 10)
        self.assertEqual("saldo = 10, vielä tilaa 90", str(uusi_varasto))

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
