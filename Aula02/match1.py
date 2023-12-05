dia = input("Digite um número entre 1 e 7 e, lhe diremos qual o dia da semana: ")

match dia:
    case '1':
        print("Domingo")
    case '2':
        print("Segunda-Feira")
    case '3':
        print("Terça-Feira")
    case '4':
        print("Quarta-Feira")
    case '5':
        print("Quinta-Feira")
    case '6':
        print("Sexta-Feira")
    case '7':
        print("Sábado")
    case _:
        print("Este dia da semana não existe ☺ ♥ ")
