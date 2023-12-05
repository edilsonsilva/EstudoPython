# quantidade de anos bissextos
# de 1973 até 2023
qtd=0
for i in range(1973,2024):
    if i % 4 == 0:
        qtd+=1
print("A quantidade de anos bissextos de 1973 até 2023 é")
print(qtd)