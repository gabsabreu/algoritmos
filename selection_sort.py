#fonte estudo 1: https://www.youtube.com/watch?v=ZT_dT8yn48s&list=PL5TJqBvpXQv4l7nH-08fMfyl7aDFNW_fC

# #lista desordenada
# lista = [7, 5, 1, 8, 3, 6, 45, 0]

# tamanhodalista = len(lista)
# valor_min = lista[0]

# print('o tamanho da lista é: ', tamanhodalista)

# #descobrindo o menor valor da lista

# for x in range(tamanhodalista):
#     if lista[x] < valor_min:
#         valor_min = lista[x]
# print('o valor minimo encontrado é: ', valor_min)

# #criando função

# def  selection_sort(lista):
#     tamanhodalista = len(lista)
    
#     for posicao in range(tamanhodalista):

#         indice_min = 0

#         for x in range(tamanhodalista):
#             if lista[x] < lista [indice_min]:
#                 valor_min = x
#         if lista[posicao] > lista[indice_min]:
#                 aux = lista[posicao]
#                 lista[posicao] = lista[indice_min]
#                 lista[indice_min] = aux

#fonte estudo 2: https://henriquebraga92.medium.com/algoritmos-de-ordena%C3%A7%C3%A3o-ii-selection-sort-8ee4234deb10

def selection_sort(items): 
    for index, item in enumerate(items[:-1]): #Não é necessário #iterar no último item (items[:-1] ignora o último elemento do array)
        smallest_index = index #considera o valor do índice mais 
# baixo o índice item que está iterando no primeiro loop
        for index_to_compare, item_to_compare in enumerate(
                items[index::], index #itera somente os itens à #direita do índice
        ): 
            if item_to_compare < items[smallest_index]: 
                smallest_index = index_to_compare
        items[index], items[smallest_index] = (
                items[smallest_index],
                items[index]
        ) #Por fim, faz a troca de posição dos itens: o menor #encontrado com o item que está sendo iterado.
    print(items)
if __name__ == '__main__':
    selection_sort([7, 5, 1, 8, 3, 6, 45, 0])