from Cliente import Cliente

class PessoaFisica(Cliente):
    def __init__(self,nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        
    @staticmethod
    def verificar_cpf_existe(cpf, lista_clientes):
        '''Verifica se o CPF já foi cadastrado anteriormente'''
        for cliente in lista_clientes:
            if cliente.cpf == cpf:
                return True
        return False
    
    @staticmethod
    def criar_novo_usuario(lista_clientes):
        '''Cria um novo usuário pessoa física'''
        print('---Cadastro de novo usuário - Pessoa Física')
        var_strNomeNovoUsuario = input('Informe seu nome: ')
        var_strNascNovoUsuario = input('Informe sua data de nascimento: ')
        var_strCpfNovoUsuario = input('Informe seu CPF: ')
        var_strEnderecoNovoUsuario = input('Informe seu endereço: ')
        
        if PessoaFisica.verificar_cpf_existe(var_strCpfNovoUsuario, lista_clientes):
            print('CPF já foi cadastro. Não é possível criar um novo usuário com este CPF')
            return
        
        # Cria o novo cliente Pessoa Física
        var_objNovoCliente = PessoaFisica(nome=var_strNomeNovoUsuario, data_nascimento=var_strNascNovoUsuario, cpf=var_strCpfNovoUsuario, endereco=var_strEnderecoNovoUsuario)
        
        lista_clientes.append(var_objNovoCliente)
        
        print(f"Novo usuário cadastrado com sucesso!\nNome: {var_strNomeNovoUsuario}\nCPF: {var_strCpfNovoUsuario}")
        