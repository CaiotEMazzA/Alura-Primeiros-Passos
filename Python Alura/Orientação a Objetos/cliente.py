# @property permite que você chame um getter para o atributo em questão sem colocar parênteses depois do nome do
# método.
# Para usar um setter de jeito parecido, deve-se usar a seguinte sintaxe: "@nomedogetter.setter". Para chamar um setter,
# deve-se chamá-lo da mesma forma que um getter, mas atribuindo um valor ao atributo especificado.

class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print('Chamando @property nome()')
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print('Chamando setter nome()')
        self.__nome = nome
