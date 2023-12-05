def soma(numeros):
    """ A função soma realiza a soma dos números 
    que são passados por parametro. E ao final, retorna
    o resultado da soma.
    Obs.: Você deve passar por parametro uma lista com 
    números """
    rs = 0
    for n in numeros:
        rs += n
    return rs

# Usando a função soma
v = [10,5,4,8,1]
print(soma(v))
