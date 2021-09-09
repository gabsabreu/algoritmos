lista = [7, 5, 1, 8, 3, 6, 45, 0]

tamanhodalista = len(lista)
valor_min = lista[0]

print('o tamanho da lista é: ', tamanhodalista)

#descobrindo o menor valor da lista

for x in range(tamanhodalista):
    if lista[x] < valor_min:
        valor_min = lista[x]
print('o valor minimo encontrado é: ', valor_min)