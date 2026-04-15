import unittest
from Veiculo import Veiculo
from Pista import Pista


class TestVeiculo(unittest.TestCase):
    def test_andar_consumes_one_liter_and_updates_odometro(self):
        veiculo = Veiculo("TEST-001", "amarelo", 5, 100, 12, "o-o")
        distancia = veiculo.andar()

        self.assertEqual(distancia, 12)
        self.assertEqual(veiculo.tanque, 4)
        self.assertEqual(veiculo.odometro, 112)

    def test_andar_when_tank_empty_does_nothing(self):
        veiculo = Veiculo("TEST-002", "preto", 0, 50, 10, "o-o")
        distancia = veiculo.andar()

        self.assertEqual(distancia, 0)
        self.assertEqual(veiculo.tanque, 0)
        self.assertEqual(veiculo.odometro, 50)


class TestPista(unittest.TestCase):
    def test_correr_finishes_when_fuel_enough(self):
        veiculo = Veiculo("TEST-003", "branco", 2, 0, 6, "o-o")
        pista = Pista(10, [veiculo])

        resultados = pista.correr()

        self.assertTrue(resultados[0]["terminou"])
        self.assertEqual(resultados[0]["distancia_percorrida"], 10)
        self.assertEqual(veiculo.tanque, 0)
        self.assertEqual(veiculo.odometro, 12)

    def test_correr_stops_if_fuel_runs_out_before_finish(self):
        veiculo = Veiculo("TEST-004", "cinza", 1, 0, 5, "o-o")
        pista = Pista(10, [veiculo])

        resultados = pista.correr()

        self.assertFalse(resultados[0]["terminou"])
        self.assertEqual(resultados[0]["distancia_percorrida"], 5)
        self.assertEqual(veiculo.tanque, 0)
        self.assertEqual(veiculo.odometro, 5)


if __name__ == "__main__":
    unittest.main()
