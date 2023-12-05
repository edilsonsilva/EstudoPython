# Se a nota for maior ou igual a 6 -> Aprovado
# Se a nota for menor ou igual a 4 -> Reprovado
# Se a nota for maior que 4 e menor que 6 -> Recuperação
media = input("Digite a nota do aluno: ")

media = float(media)
if media >= 7:
    print("Aluno aprovado")
elif media <= 4:
    print("Aluno reprovado")
else:
    print("Aluno em recuperação")