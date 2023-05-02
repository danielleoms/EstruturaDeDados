
### O que é uma lista em Python?
Uma lista em Python é uma coleção ordenada de elementos, onde cada elemento pode ser de um tipo diferente, como inteiros, strings, booleanos, outras listas, etc. As listas são mutáveis, ou seja, os elementos podem ser adicionados, removidos ou modificados.

### Como criar uma lista em Python?
Para criar uma lista em Python, basta utilizar colchetes [] e separar os elementos por vírgulas. Exemplo:

  minha_lista = [1, 2, 3, 'texto', True]

### Como acessar elementos de uma lista em Python?
Os elementos de uma lista em Python são acessados através de índices, que começam em zero. Para acessar um elemento, basta indicar o índice correspondente entre colchetes. Exemplo:

  minha_lista = [1, 2, 3, 'texto', True]
  print(minha_lista[2])  # imprime 3

### Como modificar elementos de uma lista em Python?
Para modificar um elemento de uma lista em Python, basta acessá-lo pelo índice e atribuir um novo valor a ele. Exemplo:

  minha_lista = [1, 2, 3, 'texto', True]
  minha_lista[3] = 'novo texto'
  print(minha_lista)  # imprime [1, 2, 3, 'novo texto', True]

### Como adicionar elementos a uma lista em Python?
Para adicionar elementos a uma lista em Python, existem vários métodos, como append(), que adiciona um elemento ao final da lista, e insert(), que adiciona um elemento em uma posição específica. Exemplo:

  minha_lista = [1, 2, 3, 'texto', True]
  minha_lista.append(4)
  print(minha_lista)  # imprime [1, 2, 3, 'texto', True, 4]

  minha_lista.insert(2, 'novo texto')
  print(minha_lista)  # imprime [1, 2, 'novo texto', 3, 'texto', True, 4]

### Como remover elementos de uma lista em Python?
Para remover elementos de uma lista em Python, também existem vários métodos, como remove(), que remove o primeiro elemento encontrado com o valor indicado, e pop(), que remove o elemento de uma posição específica e retorna seu valor. Exemplo:

  minha_lista = [1, 2, 3, 'texto', True]
  minha_lista.remove(3)
  print(minha_lista)  # imprime [1, 2, 'texto', True]

  valor_removido = minha_lista.pop(1)
  print(minha_lista)  # imprime [1, 'texto', True]
  print(valor_removido)  # imprime 2

### Como ordenar uma lista em Python?
Para ordenar uma lista em Python, basta utilizar o método sort(), que ordena a lista em ordem crescente. É possível também utilizar o parâmetro reverse=True para ordenar em ordem decrescente. Exemplo:
