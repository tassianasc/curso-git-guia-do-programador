#main.py

from conta import Conta
from cliente import Cliente
from banco import Banco

if __name__ == '__main__':
    banco = Banco('UniBank', 'Rua General Castro 171', '1234')
    cliente1 = Cliente('Fabricio', 'Dias', '154456987-09',banco)
    conta1 = Conta('1234', cliente1, 50)
    cliente2 = Cliente('João','Victor','000123321-45',banco)
    conta2 = Conta('2345',cliente2,100)

    print(conta1.transfere_para(40,conta2))
    print(conta2.saldo)
    print('=================')
    conta1.saque(10)
    conta1.deposito(20)
    conta1.historico.imprime_transacoes()
    print("==================")
    print(conta1.titular)
    print('===================')
    print("Banco")

    banco.adicionar_clientes(cliente1)
    banco.adicionar_clientes(cliente2)
    banco.listar_cliente()
    print("="*10)
    print(cliente2.banco.agencia)

#historico.py
from datetime import datetime

class Historico():
    def __init__(self):
        self.data_de_abertura = datetime.today()
        self.transacoes = []

    def imprime_transacoes(self):
        print("A data de abertura é: {}".format(self.data_de_abertura))
        print("- Transações -")
        for t in self.transacoes:
            print('-',t)

#cliente.py

class Cliente():
    proximo_id = 1
    def __init__(self,nome,sobrenome,cpf,banco):
        self.id = Cliente.proximo_id
        Cliente.proximo_id += 1
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.banco = banco

    def __str__(self):
        return (f'O id do cliente é: {self.id} \n'
                f'O nome completo do cliente é: {self.nome} {self.sobrenome}\n'
                f'E o seu cpf tem o número: {self.cpf}\n'
                f'---------------------------------------------')

#conta.py

from historico import Historico
class Conta():
    def __init__(self,numero, cliente,saldo):
        self.agencia = cliente.banco.agencia
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.historico = Historico()

    def saque(self, valor):
        if self.saldo < valor:
            print('Tu não tem saldo')
        else:
            self.saldo -= valor
            #print(f'Fiz um saque de: {valor} e o meu saldo atual é de: {self.saldo}')
            self.historico.transacoes.append("Saque de: {} e o saldo atual é de: {}".format(valor,self.saldo))


    def deposito(self, valor):
        self.saldo += valor
        #print(f'Fiz um deposito de: {valor} e o meu saldo atual é de: {self.saldo}')
        self.historico.transacoes.append("Depósito de: {} e o saldo atual é de: {}".format(valor,self.saldo))

    def transfere_para(self,valor,destino):
        self.saldo -= valor
        destino.saldo += valor
        return(f'O valor transferido foi de: {valor} \n'
              f'O número da conta de destino foi: {destino.numero}')

    def extrato(self):
        print(f'O titular da conta é: {self.titular} \n'
              f'Número da conta: {self.numero} \n'
              f'Com o saldo atual de: {self.saldo}')

#banco.py

class Banco():
    def __init__(self,nome,endereco,agencia):
        self.nome = nome
        self.endereco = endereco
        self.agencia = agencia
        self.clientes = []

    def imprime_nome_banco(self):
        print(f'O nome do banco é: {self.nome} \n'
              f'O endereço do banco é: {self.endereco} \n'
              f'A agencia do banco é: {self.agencia}')

    def adicionar_clientes(self,cliente):
        self.clientes.append(cliente)

    def listar_cliente(self):
        for cliente in self.clientes:
            print(cliente)
