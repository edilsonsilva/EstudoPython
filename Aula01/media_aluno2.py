'''
Crie um programa para mostrar se o alunos está
aprovado, reprovado ou em recuperação.
O programa deve pedir 4 notas e realizar o 
cálculo da média. 
Se a media do alunos for:

    >= 6 -> Aprovado
    <= 4 -> Reprovado
    >4 e <6 ->Recuperação


'''
n1 = input("Digite a primeira nota: ")
n2 = input("Digite a segunda nota: ")
n3 = input("Digite a terceira nota: ")
n4 = input("Digite a quarta nota: ")

media = (float(n1)+float(n2)+float(n3)+float(n4))/4

if media >= 6:
    print("Aluno aprovado")
elif media <= 4:
    print("Aluno reprovado")
else:
    print("Aluno em recuperação")
    