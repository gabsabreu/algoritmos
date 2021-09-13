lista_desordenada = [2,5,3,-8]
lista_frutas = ['banana','tomate','abacate','melancia','maça','laranja']
tamanho_lista = len(lista_desordenada)

def insertion_sort(lista): #criando função
    n = len(lista) #tamanho da lista
    for i in range(1, n): #iterando passando por cada elemento ignorando o 1* pq lista formada pelo 1* elemento ja ta ordenada
        chave = lista[i] #chave elemento corrente - pegando elemento para comparar com outros existentes
        j = i - 1 #j representa a sublista que ja esta ordenada 
        while j >= 0 and lista[j] > chave: #avança uma posição até inserir a chave
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = chave

# print('lista não ordenada', lista_frutas)
# insertion_sort(lista_frutas)
# print('lista ordenada',lista_frutas)

print('tamanho da lista: ',tamanho_lista)
print('lista não ordenada: ', lista_desordenada)
insertion_sort(lista_desordenada)
print('lista ordenada: ',lista_desordenada)