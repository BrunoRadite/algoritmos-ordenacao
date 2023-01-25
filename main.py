import random
from bucketSort import *
from InsertionSort import *
from quickSort import *
from radixSort import *
from mergeSort import *

vetor = []

for i in range(0,100):
  vetor.append(random.randint(0,100))
  
bucket = bucketSort(vetor)
insertion = insertionSort(vetor)
quick = quickSort(vetor, 0, len(vetor)-1)
radix = radixSort(vetor)
merge = mergeSort(vetor)

print('bucket : ',bucket)
print('insertion : ',insertion)
print('quick : ',quick)
print('radix : ',radix)
print('merge : ',merge)

