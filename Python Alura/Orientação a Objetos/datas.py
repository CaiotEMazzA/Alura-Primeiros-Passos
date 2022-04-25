# Desafio Opcional:

# Você não precisa fazer este exercício para continuar no treinamento, mas é bom praticar, certo?
# Lançamos o seguinte desafio: para ajudar na formatação de datas você deve criar uma nova classe auxiliar.
# Essa classe deve representar uma Data (sem hora) que sabe imprimir uma data formatada.
# Ela deve funcionar dessa forma:

# from datas import Data
# d = Data(21,11,2007)
# d.formatada()

# Imprime:
# 21/11/2007

# Crie e implemente essa classe dentro de uma arquivo datas.py. Mãos à obra!

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print('{:02}'.format(self.dia), '{:02}'.format(self.mes), '{}'.format(self.ano), sep = '/')
