# Obter o número de dígitos no maior item
def _num_digits(arr):
    # Guardar o digito de maior valor
    maxDigit = 0
    # entrando em cada item 
    for num in arr:
        # comparando o numero atual com o maxDigit anterior
        maxDigit = max(maxDigit, num)
    # retornando o número de digitos do maior item  
    return len(str(maxDigit))
 
 
# Compactando uma lista de listas em apenas uma
from functools import reduce
def _flatten(arr):
    return reduce(lambda x, y: x + y, arr)
 
# Função RADIX SORT
def radixSort(arr):
    # quantidade de digitos do maior item
    digits = _num_digits(arr)
    
    # rodando em cada digito do maior item
    for digit in range(0, digits):
        # Criando 10 baldes de 0 a 9
        bucket = [[] for i in range(10)]
        # percorrendo todos os itens da lista
        for item in arr:
            # pegando em qual balde esse item será armazenado
            num = (item // (10 ** digit)) % 10
            bucket[num].append(item)
        
        # compactando a matriz em apenas uma lista
        arr = _flatten(bucket)
    # retornando a lista ordenada 
    return arr