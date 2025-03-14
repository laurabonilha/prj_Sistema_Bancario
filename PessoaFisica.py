from Cliente import Cliente

class PessoaFisica(Cliente):
    def __init__(self,nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
    
    def __str__(self):
        '''Padroniza a apresentação dos dados do usuário cadastrado - PF'''
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nData de Nascimento: {self.data_nascimento}\nEndereço: {self.endereco}"

    @staticmethod
    def verificar_cpf_existe(cpf, lista_clientes):
        '''Verifica se o CPF já foi cadastrado anteriormente'''
        for cliente in lista_clientes:
            if cliente.cpf == cpf:
                return True
        return False
    
    @classmethod
    def criar_novo_usuario(cls, lista_clientes):
        '''Cria um novo usuário pessoa física'''
        print('---Cadastro de novo usuário - Pessoa Física')
        var_strNomeNovoUsuario = input('Informe seu nome: ')
        var_strNascNovoUsuario = input('Informe sua data de nascimento: ')
        var_strCpfNovoUsuario = input('Informe seu CPF: ')
        var_strEnderecoNovoUsuario = input('Informe seu endereço: ')
        
        if PessoaFisica.verificar_cpf_existe(var_strCpfNovoUsuario, lista_clientes):
            print('CPF já foi cadastro. Não é possível criar um novo usuário com este CPF')
            return
        
        var_objNovoUsuario = cls(nome=var_strNomeNovoUsuario, data_nascimento=var_strNascNovoUsuario, cpf=var_strCpfNovoUsuario, endereco=var_strEnderecoNovoUsuario)
        lista_clientes.append(var_objNovoUsuario)
        
        print("Novo usuário cadastrado com sucesso!\n", var_objNovoUsuario)
        

    