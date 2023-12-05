class Usuario:
    def __init__(self, nome_usuario, senha, nivel_acesso):
        self.nome_usuario = nome_usuario
        self.senha = senha
        self.nivel_acesso = nivel_acesso

    def login(self,nome_usuario, senha):
        if self.nome_usuario == nome_usuario and self.senha == senha:
            print("Você está logado\nSeja bem vindo")
        else:
            print("Nome de usuário ou senha incorreto")
    
    def alterar_senha(self,nome_usuario, nova_senha):
        if self.nome_usuario == nome_usuario:
            self.senha = nova_senha
            print("Senha alterada")
        else:
            print("Usuário inexistente")
    
    def logout(self):
        self.nome_usuario = ""
        self.senha = ""
        self.nivel_acesso = ""
        print("Você saiu do sistema")
