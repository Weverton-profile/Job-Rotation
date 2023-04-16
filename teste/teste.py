import json

with open("teste\\dados.json") as file:
    data = json.load(file)


menor = data[1]['valor']
maior = data[1]['valor']
for i in range(len(data)):
    if data[i]['valor'] > 0:
        if maior < menor:
            menor = maior
            maior = data[i]['valor']
        else:
            maior = data[i]['valor']
print(f'O menor valor de faturamento ocorrido em um dia do mês desconsiderando 0 é {menor}.')

menor = data[1]['valor']
maior = 0
for i in range(len(data)):
    if menor > maior:
        maior = menor
        menor = data[i]['valor']
    else:
        menor = data[i]['valor']
print(f'O maior valor de faturamento ocorrido em um dia do mês é {maior}.')

count = 0
media = 0
for i in range(len(data)):
    if data[i]['valor'] > 0:
        media += data[i]['valor']
        count += 1
media = media / count
print(f'Dias no mês em que o valor de faturamento diário foi superior à média mensal; Media mensal = {round(media, 4)}.')
for i in range(len(data)):
    if data[i]['valor'] > media:
        print(f'Dia: {data[i]["dia"]}, Faturamento: {data[i]["valor"]}')