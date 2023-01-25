# Função INSERTION SORT que recebe como parametro uma lista
def insertionSort(vetor):
  
   # verificando se o vetor possui mais de um elemento
   if len(vetor) > 1: 

    # rodando a partir do segundo elemento da lista até o ultimo index da mesma
    for index in range(1,len(vetor)):

      # marcando o elemento que será comparado com os anteriores a ele
      marcador = vetor[index]

      # elemento que será comparado com o marcador
      comparacao = index -1

      # enquanto o index da comparação for maior ou igual a 0
      # e o marcador for menor que  a comparação
      while comparacao >= 0 and marcador < vetor[comparacao]:

        # afastando a comparação para o proximo index
        vetor[comparacao+1] = vetor[comparacao]

        #atualizando o valor da comparação
        comparacao -= 1
      # quando a comparação for menor que o marcador 
      # o marcador será inserido depois da comparação
      vetor[comparacao+1] = marcador
    
    # retorna o vetor
    return vetor
   