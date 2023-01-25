# Função BUCKET SORT que recebE como parametro uma lista
def bucketSort(array):
    # Pegando o maior valor da lista
    largest = max(array)
    # Pegando a quantidade de elementos da lista
    length = len(array)
    # Pegando a quantidade de elementos que cada balde deve ter 
    size = largest/length
 
    # Criando os 'Baldes'
    buckets = [[] for i in range(length)]
 
    # Organizando os Baldes  
    for i in range(length):
        
        index = int(array[i]/size)
        if index != length:
            buckets[index].append(array[i])
        else:
            buckets[length - 1].append(array[i])
 
    # Ordenando Baldes Individuais(dentro de cada balde)
    for i in range(len(array)):
        
        buckets[i] = sorted(buckets[i])
 
 
    # Achatando e juntando os Baldes
    result = []
    for i in range(length):
        result = result + buckets[i]
    
    # retornando a lista ordenada  
    return result