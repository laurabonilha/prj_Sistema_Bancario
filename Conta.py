from Historico import Historico

import random

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()
    
    @staticmethod
    def verifica_cpf_cadastrado(cpf, lista_clientes):
        '''Verifica se o usuário está cadastrado e apto a abrir uma nova conta'''
        for cliente in lista_clientes:
            if cliente.cpf == cpf:
                return True
        return False
    
    @classmethod
    def nova_conta(cls, lista_clientes):
        print('---Criando nova conta---')
        var_strCpfInformado = input('Informe seu CPF para cadastrar nova conta: ')
        var_objCliente = Conta.verifica_cpf_cadastrado(cpf=var_strCpfInformado, lista_clientes=lista_clientes)
        if var_objCliente:
            print('Seu CPF está regularizado! Seguindo com a criação da sua conta...')
            var_intNumConta = random.randint(10000, 99999)
            var_objNovaConta = cls(var_intNumConta, var_objCliente)
            print(f'Nova conta {var_intNumConta} criada com sucesso!')
            return var_objNovaConta
        else:
            print('Não foi possível encontrar nenhum cadastro com esse CPF. Favor cadastrar-se primeiro!')
            return
        
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print('Operação falhou. Não há saldo suficiente')
        elif valor > 0:
            self._saldo -= valor
            print('Saque realizado com sucesso')
            return True
        else:
            print('Operação falhou. O valor informado é inválido')
            
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('Depósito realizado com sucesso')
        else:
            print('Operação falhou. Valor informado é inválido')
            return False
        
        return True
        