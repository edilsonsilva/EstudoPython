#!/usr/bin/python3
nome = input("Digite o seu nome: ")
anonas = input("Digite o ano do seu nascimento:")
#Para realizar o cálculo da idade, foi necessário converter
#a variável anoanas para inteiro, pois o comando input
#sempre retorna o valor como texto.
idade = 2023 - int(anonas)
#para converter um valor numérico em texto, usamos o comando str
print("Olá sr(a). "+nome+" você tem ou terá este ano: "+str(idade)+" anos")