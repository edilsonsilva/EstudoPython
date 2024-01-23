import os
class Cliente:
    def __init__(self):
        self.__nome = ""
        self.__email = ""
        self.__cpf = ""
        self.__idade = 0
        self.__telefone = ""
    def gravarCliente(self, nome="",email="",cpf="",idade=0,telefone=""):
        
        if(nome=="" or email=="" or cpf=="" or idade < 18 or telefone == ""):
            print("DIGITE TODOS OS DADOS!")
        else:
            self.__nome = nome
            self.__email = email
            self.__cpf = cpf
            self.__idade = idade
            self.__telefone = telefone
            self.__gravar()

    def __gravar(self):
        arquivo = open("dados/infocliente.csv","a")
        arquivo.write("Nome: "+self.__nome+";\n")
        arquivo.write("E-Mail: "+self.__email+";\n")
        arquivo.write("CPF: "+self.__cpf+";\n")        
        arquivo.write("Idade: "+self.__idade+";\n")
        arquivo.write("Telefone: "+self.__telefone+";\n")
        arquivo.close()
        print("Cliente gravado com sucesso!")
    def obter(self):
        dt = open("dados/infocliente.csv")
        print(dt.read())
        dt.close()



