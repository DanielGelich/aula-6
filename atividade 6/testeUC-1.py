import unittest
from main import CalculadoraHorasTrabalhadas

class TestCalculadoraHorasTrabalhadas(unittest.TestCase):

    def setUp(self):
        self.calculadora = CalculadoraHorasTrabalhadas()

    def test_calcular_diferenca_horas(self):
        self.assertEqual(self.calculadora.calcular_diferenca_horas('08:00', '16:30'), 8.5)
        self.assertEqual(self.calculadora.calcular_diferenca_horas('09:15', '17:45'), 8.5)
        self.assertEqual(self.calculadora.calcular_diferenca_horas('12:00', '14:30'), 2.5)

    def test_calcular_horas_trabalhadas(self):
        entrada = [('08:00', '16:30'), ('09:15', '17:45'), ('12:00', '14:30')]
        self.assertEqual(self.calculadora.calcular_horas_trabalhadas(entrada), 19.5)

    def test_validar_formato_hora(self):
        self.assertTrue(self.calculadora.validar_formato_hora('08:00'))
        self.assertTrue(self.calculadora.validar_formato_hora('12:45'))
        self.assertFalse(self.calculadora.validar_formato_hora('8:00'))
        self.assertFalse(self.calculadora.validar_formato_hora('0800'))
        self.assertFalse(self.calculadora.validar_formato_hora('08:60'))

if __name__ == '__main__':
    unittest.main()
