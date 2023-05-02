# Lista encadeada


#### Pergunta: O que é uma lista encadeada?
Uma lista encadeada é uma estrutura de dados linear na qual cada elemento (nó) contém um valor e um ponteiro (referência) para o próximo nó da lista. Esses nós são organizados em sequência, formando a lista. O primeiro nó da lista é chamado de cabeça (head) e o último nó é chamado de cauda (tail) e aponta para um nó vazio ou nulo. A lista encadeada permite inserir e remover elementos de forma eficiente, pois a inserção e remoção ocorrem apenas modificando os ponteiros que ligam os nós.


#### Pergunta: O que é uma lista duplamente encadeada?

Uma lista duplamente encadeada (ou lista duplamente ligada) é uma estrutura de dados que permite armazenar uma sequência de elementos em que cada elemento é ligado aos seus elementos adjacentes por meio de dois ponteiros: um para o elemento anterior e outro para o elemento seguinte. Esses ponteiros permitem que a lista seja percorrida tanto em direção ao início quanto em direção ao fim.

Cada elemento da lista, conhecido como nó, contém um campo de dados e dois ponteiros: um para o nó anterior e outro para o próximo nó. O primeiro nó da lista é chamado de cabeça e o último nó é chamado de cauda.

Uma lista duplamente encadeada oferece algumas vantagens em relação a uma lista simplesmente encadeada, como a capacidade de percorrer a lista em ambas as direções e a facilidade de remoção de um nó.

Abaixo está um exemplo de implementação de uma lista duplamente encadeada em Python:

    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    class DoublyLinkedList:
        def __init__(self):
            self.head = None
            self.tail = None

        def append(self, data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node

        def delete(self, data):
            current = self.head
            while current:
                if current.data == data:
                    if current.prev is None:
                        self.head = current.next
                    else:
                        current.prev.next = current.next
                    if current.next is None:
                        self.tail = current.prev
                    else:
                        current.next.prev = current.prev
                    return True
            current = current.next
        return False


#### Pergunta: O que é um nó em uma lista encadeada?
Em uma lista encadeada, um nó é uma estrutura de dados que contém dois elementos principais: um valor (também chamado de dado ou informação) e um ponteiro que aponta para o próximo nó na lista. O valor do nó armazena a informação que se deseja guardar e o ponteiro aponta para o próximo nó da lista ou pode ser nulo se o nó for o último da lista encadeada. A estrutura de nó é utilizada para construir uma lista encadeada, que é uma estrutura de dados dinâmica que permite armazenar e manipular uma sequência de elementos de maneira flexível.

#### Pergunta: Como criar uma lista encadeada?
Para criar uma lista encadeada, é preciso primeiro definir a classe do nó que será utilizado. Essa classe deve conter dois atributos: o dado a ser armazenado no nó e uma referência ao próximo nó na lista. Em seguida, é preciso definir a classe da lista encadeada, que deve conter um atributo para o nó inicial (ou cabeça da lista) e métodos para adicionar, remover e percorrer os elementos da lista. 

#### Como inserir um elemento em uma lista encadeada?
Para inserir um novo elemento em uma lista encadeada, é necessário seguir os seguintes passos:

Alocar espaço em memória para um novo nó;
Atribuir o valor do novo elemento ao campo de dado do nó;
Atribuir o ponteiro do próximo nó ao campo próximo do novo nó;
Atribuir o ponteiro do novo nó ao campo próximo do nó anterior.
A inserção pode ser realizada no início, no final ou em qualquer posição da lista encadeada, dependendo da lógica de implementação escolhida. Em geral, o tempo de inserção em uma lista encadeada é O(1), ou seja, constante, desde que se tenha o ponteiro para o nó onde a inserção será realizada.

#### Pergunta: Como remover um elemento de uma lista encadeada?

Para remover um elemento de uma lista encadeada, é preciso identificar o nó que contém o elemento a ser removido e ajustar os ponteiros dos nós anterior e posterior a ele. O processo de remoção pode variar de acordo com a posição do nó a ser removido na lista.

#### Pergunta: Quais são as principais operações em uma lista encadeada?

Por exemplo, para remover o primeiro nó da lista, basta atualizar o ponteiro "head" da lista para o próximo nó. Já para remover o último nó da lista, é necessário percorrer a lista até o penúltimo nó e ajustar o seu ponteiro "next" para None.

Em geral, o processo de remoção de um elemento em uma lista encadeada pode ser resumido nos seguintes passos:

1) Percorrer a lista para encontrar o nó que contém o elemento a ser removido
2) Atualizar os ponteiros do nó anterior e posterior ao nó que será removido
3) Liberar a memória ocupada pelo nó que foi removido

As principais operações em uma lista encadeada incluem:

* Inserir um novo elemento no início da lista
* Inserir um novo elemento no final da lista
* Inserir um novo elemento em uma posição específica da lista
* Remover um elemento do início da lista
* Remover um elemento do final da lista
* Remover um elemento em uma posição específica da lista
* Buscar um elemento na lista
* Percorrer a lista e imprimir ou processar seus elementos.

#### Pergunta: Quais são as principais operações em uma lista encadeada?

As principais vantagens de utilizar uma lista encadeada são:

Flexibilidade no tamanho: ao contrário de um array, que tem um tamanho fixo, uma lista encadeada pode ser expandida ou reduzida dinamicamente.
Inserção e remoção de elementos: em uma lista encadeada, a inserção e remoção de elementos são operações eficientes, pois não é necessário deslocar elementos adjacentes, como em um array.
Eficiência em algumas operações: dependendo da operação a ser realizada, uma lista encadeada pode ser mais eficiente que um array.
Já as principais desvantagens são:

Acesso sequencial: uma lista encadeada não permite acesso direto aos seus elementos, sendo necessário percorrê-la sequencialmente para chegar a um determinado elemento.
Uso de memória: uma lista encadeada requer mais espaço de memória do que um array para armazenar os mesmos elementos, devido à necessidade de armazenar ponteiros para os próximos elementos.
Desempenho em operações de busca: operações que envolvem busca de elementos em uma lista encadeada, como encontrar um determinado elemento, podem ser menos eficientes do que em um array, pois requerem percorrer a lista sequencialmente.

### Clase Node

A classe Node é uma classe fundamental na implementação de uma lista encadeada, pois ela define a estrutura básica de cada nó da lista, contendo um atributo de valor e outro de referência para o próximo nó. Ela é utilizada para criar um nó, que armazena um dado (data) e uma referência para o próximo nó (next). A classe Lista possui um atributo head que é uma referência para o primeiro nó da lista.


## Método inserir(), remover() e buscar()

classe Lista possui três métodos: inserir(), remover() e buscar().

O método inserir() recebe um dado como argumento e cria um novo nó com esse dado. Se a lista estiver vazia, o novo nó é definido como a cabeça da lista; caso contrário, o novo nó é adicionado ao final da lista.

O método remover() recebe um dado como argumento e remove o nó correspondente da lista, caso exista. Se a lista estiver vazia, não há nada a ser removido. Se o nó a ser removido for a cabeça da lista, o método atualiza a cabeça da lista para o próximo nó. Caso contrário, o método percorre a lista até encontrar o nó a ser removido e atualiza o ponteiro next do nó anterior para apontar para o próximo nó.

O método buscar() recebe um dado como argumento e percorre a lista procurando por um nó que contenha esse dado. Se encontrar o nó, o método retorna True; caso contrário, retorna False.
