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
                pass
                
            case '4':
                Conta.nova_conta(var_clssMenu.clientes)
                
                
            case '6':
                PessoaFisica.criar_novo_usuario(var_clssMenu.clientes)
                
               
            case _:
                print("Opção inválida!")
                
                




    
                
if __name__ == '__main__':
    main()