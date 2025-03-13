import textwrap
from Cliente import Cliente
from Conta import Conta
from ContaCorrente import ContaCorrente
from Deposito import Deposito
from Historico import Historico
from PessoaFisica import PessoaFisica
from Saque import Saque
from Transacao import Transacao

class Menu():
    def __init__(self):
        self.clientes = []  # Lista para armazenar clientes
        self.contas = []    # Lista para armazenar contas
    
    
    def criar_novo_usuario(self):
        '''Cria um novo usuário pessoa física'''
        print('---Cadastro de novo usuário - Pessoa Física')
        
        var_strNomeNovoUsuario = input('Informe seu nome: ')
        var_strNascNovoUsuario = input('Informe sua data de nascimento: ')
        var_strCpfNovoUsuario = input('Informe seu CPF: ')
        var_strEnderecoNovoUsuario = input('Informe seu endereço: ')
        
        var_objNovoCliente = PessoaFisica(nome=var_strNomeNovoUsuario, data_nascimento=var_strNascNovoUsuario, cpf=var_strCpfNovoUsuario, endereco=var_strEnderecoNovoUsuario)
        
        self.clientes.append(var_objNovoCliente)
        
        print(f"Novo usuário cadastrado com sucesso!\nNome: {var_strNomeNovoUsuario}\nCPF: {var_strCpfNovoUsuario}")

     
    def depositar(self):
            """Realiza um depósito em uma conta."""
            numero = input("Informe o número da conta: ")
            
            # Verifica se a conta existe
            for conta in self.contas:
                if numero == conta:
                    print(f'Conta de número {conta} encontrada com sucesso!')
                    conta_existe = True
                else:
                    print('Conta informada não existe! Cadastre-se primeiro')  
                    conta_exite = False
                    break
            
            if conta_existe:
                valor = input('Informe o valor a ser depositado: ')
                
                
                
                


def menu():
    opcoes = '''
    ============= MENU =============
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar Contas
    [6]\tNovo usuário
    [0]\tSair
    >>> '''
    return input(textwrap.dedent(opcoes))
    
    
def main():
    var_clssMenu = Menu()
    while True:
        opcao = menu()
        
        match(opcao):
            
            case '0':
                print('Saindo da aplicação...')
                return False
            
            case '1':
                print('---Depósito---')
                var_clssMenu.depositar()
                
            case '6':
                var_clssMenu.criar_novo_usuario()    
            
            
               
            case _:
                print("Opção inválida!")
                
                




    
                
if __name__ == '__main__':
    main()