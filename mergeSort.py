# Função MERGE SORT que recebe como parametro uma lista
def mergeSort(vetor):


    # Verificando se o vetor possui mais de um elemento
    if len(vetor) > 1:
      

        # Pegando o número inteiro resultante da divisão do tamanho da lista por 2
        mid = len(vetor)//2

        # Pegando os números do vetor da metade para o index 0
        metade_esquerda = vetor[:mid]

        # Pegando os números do vetor da metade para o index de maior valor
        metade_direita = vetor[mid:]

        # Momento em que há recursividade da função, sendo aqui que começa o "DIVIDIR PARA CONQUISTAR"
        mergeSort(metade_esquerda)
        mergeSort(metade_direita)

        # Contadores de index ( Variáveis auxiliares)

        # Contador para o sub-vetor 1 ( Metade da Esquerda )
        index_virtual_esquerda = 0

         # Contador para o sub-vetor 2 ( Metade da Direita )
        index_virtual_direita = 0

         # Contador para o vetor real ( Vetor passado primeiramente )
        index_vetor_real = 0

        # Enquanto o index virtual da metade da esquerda for menor que a quantidade de elementos nesse mesmo vetor E
        # Enquanto o index virtual da metade da direita for menor que a quantidade de elementos nesse mesmo vetor
        while index_virtual_esquerda < len(metade_esquerda) and index_virtual_direita < len(metade_direita):


            # Se o elemento analisado do vetor virtual da esquerda for MENOR que o elemento analisado do vetor virtual da direita
            if metade_esquerda[index_virtual_esquerda] < metade_direita[index_virtual_direita]:


                # O elemento do vetor real passa a ser o elemento analisado do vetor virtual da esquerda
                vetor[index_vetor_real] = metade_esquerda[index_virtual_esquerda]

                # O index do vetor virtual da esquerda passa a ser incrementado em 1
                index_virtual_esquerda += 1


            # Se o elemento analisado do vetor virtual da esquerda for MAIOR que o elemento analisado do vetor virtual da direita
            else:

                # O elemento do vetor real passa a ser o elemento analisado do vetor virtual da direita
                vetor[index_vetor_real] = metade_direita[index_virtual_direita]

                # O index do vetor virtual da direita passa a ser incrementado em 1
                index_virtual_direita += 1
            
            # O index do vetor real passa a ser incrementado em 1
            index_vetor_real += 1


        # Enquanto o index virtual da metade da esquerda for menor que a quantidade de elementos nesse mesmo vetor
        while index_virtual_esquerda < len(metade_esquerda):

            # O elemento do vetor real passa a ser o elemento analisado do vetor virtual da esquerda
            vetor[index_vetor_real]= metade_esquerda[index_virtual_esquerda]

            # O index do vetor virtual da esquerda passa a ser incrementado em 1
            index_virtual_esquerda += 1

            # O index do vetor real passa a ser incrementado em 1
            index_vetor_real += 1


        # Enquanto o index virtual da metade da direita for menor que a quantidade de elementos nesse mesmo veto
        while index_virtual_direita < len(metade_direita):

            # O elemento do vetor real passa a ser o elemento analisado do vetor virtual da direita
            vetor[index_vetor_real] = metade_direita[index_virtual_direita]

            # O index do vetor virtual da direita passa a ser incrementado em 1
            index_virtual_direita += 1

            # O index do vetor real passa a ser incrementado em 1
            index_vetor_real += 1


    # Retornando o vetor real já após toda recursividade do código
    return vetor

