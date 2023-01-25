# Função para encontrar a posição da partição
def _partition(array, low, high):
 
    # escolha o elemento mais à direita como pivô
    pivo = array[high]
 
    # ponteiro para o elemento maior
    ponteiro = low - 1
 
    # percorrer todos os elementos
    # compare cada elemento com o pivô
    for index in range(low, high):
        if array[index] <= pivo:
 
            # Se for encontrado elemento menor que pivô
            # troque-o pelo elemento maior apontado pelo ponteiro
            ponteiro = ponteiro + 1
 
            # Trocando elemento no ponteiro com elemento em index
            (array[ponteiro], array[index]) = (array[index], array[ponteiro])
 
    # Troque o elemento pivô pelo elemento maior especificado pelo ponteiro
    (array[ponteiro + 1], array[high]) = (array[high], array[ponteiro + 1])
 
    # Retorna a posição de onde a partição é feita
    return ponteiro + 1
 
# Função QUICK SORT
def quickSort(array, low, high):

    if low < high:
 
        # Encontre o elemento pivô que
        # o elemento menor que pivô estão à esquerda
        # elemento maior que pivô estão à direita
        pi = _partition(array, low, high)
 
        # Chamada recursiva à esquerda do pivô
        quickSort(array, low, pi - 1)
 
        # Chamada recursiva à direita do pivô
        quickSort(array, pi + 1, high)

    # retorna a lista organizada
    return array
