#base de arvore em pós ordem 
class Node:
  def __init__(self,data):
    self.data = data 
    self.left = None
    self.right = None

def Postorder(root):
  if root:
    Postorder(root.left)
    Postorder(root.right)
    print(root.data,end='')
#importação do primeiro arquivo 
from arvore_do_chat import Node, Postorder

#criar a arvore 
root = Node(1)
root.left = Node('a')
root.right = Node('y')

print('Árvore em pós ordem:', end='')
postorder(root)

#No percurso pós- ordem, a visitação dos nós segue a ordem: nó filho esquerdo, nó filho direito e por fim, o nó pai.



#HEAP mínimo e máximo 
#Lista A: gerar 50 numeros aleatorios entre 0 e 100 
import random 
a = []
for i in range(50):
    a.append(random.randint(0,100))
print('Conjunto A:',a)

#tamanho de b seja um número aleatório entre 21 e 25 
tamanho = random.randint(21, 24)
print('Nº de elementos no conjunto B:', tamanho)

#Lista B: 25 números da lista A. Sendo ao menos, 5 ímpares
b = []
count = 0 #contador começando em zero
for i in a:
    if count < 5 and i % 2 != 0: #a divisao de i por 2 resta um nº diferente de 0. Logo ímpar. Se i% 2 == 0 seria um nº par.
       b.append(i)
       count += 1 #contador recebe incremento. Recebe 1 

    elif len(b) < tamanho:
       b.append(i)
print('Conjunto B:',b)
 

def ajustar_heap(heap,comparacao):
  tamanho = len(heap)
  for i in range (tamanho//2 -1 ,-1,-1):
    comparacao(heap,i,tamanho)

def heap_minimo(heap,indice,tamanho):
  menor = indice
  esquerda, direita = 2 * indice +1 , 2 * indice + 2 
  menor = esquerda if esquerda < tamanho and heap [esquerda] < heap [menor] else menor
  menor = direita if direita < tamanho and heap[direita] < heap [menor] else menor 
  if menor != indice:
    heap[indice], heap[menor] =  heap[menor], heap[indice]
    heap_minimo(heap,menor,tamanho)


def heap_maximo(heap,indice,tamanho):
  maior = indice
  esquerda, direita = 2* indice + 1 , 2* indice +2
  maior = esquerda if esquerda < tamanho and heap[esquerda] > heap[maior] else maior 
  maior = direita if direita < tamanho and heap[direita] > heap [maior] else maior 
  if maior != indice:
    heap[indice], heap[maior] = heap[maior], heap[indice]
    heap_maximo(heap,maior,tamanho)

#imprimir heap_minimo e heap_maximo 
heap_min,heap_max = b.copy(), b.copy()

ajustar_heap(heap_min,heap_minimo)
ajustar_heap(heap_max,heap_maximo)
print('HEAP mínimo', heap_min)
print('HEAP máximo:', heap_max)

#Consuma 4 elementos do heap_minimo e mostre o heap atualizado a cada consumacao
for i in range(4):
   elemento_consumido = b.pop(0)
   print('Elemento consumido:', elemento_consumido)
   #mostre o heap_min atualizado 
   heap_min.remove(elemento_consumido)
   heap_minimo(heap_min, 0, len(heap_min))
   print('Árvore atual - HEAP mínimo: ', heap_min)

#Consuma 4 elementos do heap_máximo e mostre o heap atualizado a cada consumacao
for i in range(4):
   elemento_consumido = b.pop(0)
   print('Elemento consumido:', elemento_consumido)
   #mostre o heap_máximo atualizado 
   heap_max.remove(elemento_consumido)
   heap_maximo(heap_max, 0, len(heap_max))
   print('Árvore atual - HEAP MÁXIMO: ',heap_max)
