import re

class CalculadoraHorasTrabalhadas:

    def __init__(self):
        self.intervalo = 0

    def inserir_intervalo(self, duracao_intervalo):
        if self.validar_formato_intervalo(duracao_intervalo):
            self.intervalo = self.parse_intervalo(duracao_intervalo)
        else:
            raise ValueError("Formato de duração de intervalo inválido")

    def calcular_horas_trabalhadas(self, entrada):
        horas = 0
        for entrada in entrada:
            hora_entrada, hora_saida = entrada
            if self.validar_formato_hora(hora_entrada) and self.validar_formato_hora(hora_saida):
                horas += self.calcular_diferenca_horas(hora_entrada, hora_saida)
            else:
                raise ValueError("Formato de hora inválido")
        return horas - self.intervalo

    def calcular_diferenca_horas(self, hora_entrada, hora_saida):
        hora_entrada = self.parse_hora(hora_entrada)
        hora_saida = self.parse_hora(hora_saida)
        return hora_saida - hora_entrada

    def parse_hora(self, hora):
        horas, minutos = map(int, hora.split(':'))
        return horas + minutos / 60.0

    def validar_formato_hora(self, hora):
        formato_hora = re.compile(r'^\d{2}:\d{2}$')
        return formato_hora.match(hora) is not None

    def validar_formato_intervalo(self, duracao_intervalo):
        formato_intervalo = re.compile(r'^\d{2}-\d{3}$')
        return formato_intervalo.match(duracao_intervalo) is not None

    def parse_intervalo(self, duracao_intervalo):
        horas, minutos = map(int, duracao_intervalo.split('-'))
        return horas + minutos / 60.0

    def inverter_horarios(self, entrada):
        return [(saida, entrada) for entrada, saida in entrada]
