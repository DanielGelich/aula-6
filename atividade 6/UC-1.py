import unittest
import re

class CalculadoraHorasTrabalhadas:

    def calcular_horas_trabalhadas(self, entrada):
        horas = 0
        for entrada in entrada:
            hora_entrada, hora_saida = entrada
            if self.validar_formato_hora(hora_entrada) and self.validar_formato_hora(hora_saida):
                horas += self.calcular_diferenca_horas(hora_entrada, hora_saida)
            else:
                raise ValueError("Formato de hora inválido")
        return horas

    def calcular_diferenca_horas(self, hora_entrada, hora_saida):
        hora_entrada = self.parse_hora(hora_entrada)
        hora_saida = self.parse_hora(hora_saida)
        return hora_saida - hora_entrada

    def parse_hora(self, hora):
        horas, minutos = map(int, hora.split(':'))
        return horas + minutos / 60.0

    def validar_formato_hora(self, hora):
        formato_hora = re.compile(r'^(?:[01]\d|2[0-3]):[0-5]\d$')
        return formato_hora.match(hora) is not None
