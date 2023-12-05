numero = input("Digite um número: ")
# O comando input sempre retorna um valor
#em formato texto. Não importa se foi digitado
#um número. Ele sempre retorna um texto
#Sendo assim, foi necessário converter a variável
#número para um valor inteiro. Utilizamos o 
#comando int(inteiro)


if int(numero) % 2 == 0:
    print("O número digitado é Par") 
else:
    print("O número digitado é Impar")
