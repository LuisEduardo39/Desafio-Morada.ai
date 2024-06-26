import unittest
from app import app, calcular_cedulas


class TestCaixaEletronico(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_calcular_cedulas(self):
        self.assertEqual(
            calcular_cedulas(380), {"100": 3, "50": 1, "20": 1, "10": 1, "5": 0, "2": 0}
        )

    def test_saque_valido(self):
        response = self.app.post("/api/saque", json={"valor": 380})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json(), {"100": 3, "50": 1, "20": 1, "10": 1, "5": 0, "2": 0}
        )

    def test_saque_invalido(self):
        response = self.app.post("/api/saque", json={"valor": -10})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.get_json(),
            {"erro": "Valor invalido. Por favor, insira um numero inteiro positivo."},
        )


if __name__ == "__main__":
    unittest.main()
