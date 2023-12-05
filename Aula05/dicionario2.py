capitais = {
    "Acre":"Rio Branco",
    "Alagoas":"Maceió",
    "Amapá":"Macapá",
    "Amazonas":"Manaus",
    "Bahia":"Salvador",
    "Ceará":"Fortaleza",
    "Espírito Santo":"Vitória",
    "Goiás":"Goiânia",
    "Maranhão":"São Luís",
    "Mato Grosso":"Cuiabá",
    "Mato Grosso do Sul":"Campo Grande",
    "Minhas Gerais":"Belo Horizonte",
    "Pará":"Beém",
    "Paraíba":"João Pessoa",
    "Paraná":"Curitiba",
    "Pernambuco":"Recife",
    "Paiuí":"Teresina",
    "Rio de Janeiro":"Rio de Janeiro",
    "Rio Grande do Norte":"Natal",
    "Rio Grande do Sul":"Porto Alegre",
    "Rondônia":"Porto Velho",
    "Roraima":"Boa Vista",
    "Santa Catarina":"Florianópolis",
    "São Paulo":"São Paulo",
    "Sergipe":"Aracaju",
    "Tocantis":"Palmas",
    "Distro Federal":"Brasília"

}

# for i in capitais:
#     print(i)

# print(capitais[0:6])
# print(capitais["Acre"])
# Pegar os 6 primeiros itens
ps = 1
for i in capitais:
    if ps < 6:
        print(i+" a capital é "+capitais[i])
    else:
        break
    ps+=1
