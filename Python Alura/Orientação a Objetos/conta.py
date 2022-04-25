# Função __init__ cria o objeto dentro da classe. Ela também pode ter parâmetros padrão. Por exemplo, se
# o limite é geralmente 1000.0 quando contas são criadas, pode-se incluir o parâmetro limite=1000.0.

# self é o parâmetro referência para o objeto criado. É "o próprio objeto".

# Para acessar qualquer atributo dentro de um objeto dentro de uma classe, deve-se colocar o nome do objeto
# mais '.<atributo_desejado>'. Por exemplo, se eu criei um objeto da classe Conta chamado 'conta' e quero
# acessar seu atributo 'saldo', digito 'conta.saldo'.

# Colocar dois "_" antes do nome de um atributo torna-o privado (Exemplo: self.__titular). Isso não significa que
# não se têm mais acesso direto a ele, mas que o python o reconhece como privado e o exibe como atributo privado,
# que só deve ser acessado por métodos da classe a qual pertence. O mesmo se dá para métodos, colocando-se dois "_"
# antes de um método, ele se torna privado.

# Quando se tenta modificar o valor de um atributo que não existe detro de uma classe, o python adiciona esse
# atributo e o inicializa com o valor que se tentou modificar. Por exemplo, se temos o atributo '__titular' e eu
# tentar digitar "conta.titular = 'João'", o python cria um atributo 'titular' com o valor inicial 'João'. O atributo
# original '__titular' não sofre alterações.

# Para acessar métodos de uma classe sem ter um objeto criado (método estático, ou seja, método relacionado à classe),
# usa-se o decorator '@staticmethod'.

# Podem ser definidos ainda atributos estáticos (atributo relacionado à classe). Para isso, depois de se declarar a
# classe, deve-se declarar esse atributo da mesma forma que se inicializa uma variável. Por convenção, usa-se letras
# maiúsculas para atributos estáticos. Por exemplo:
#
# class Circulo:
#     PI = 3.14

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo objeto... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo {self.__saldo} do titular {self.__titular}.')

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} passou o limite!')

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
