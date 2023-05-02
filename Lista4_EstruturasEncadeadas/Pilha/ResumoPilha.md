## Resumo Pilha

Pilha é uma estrutura de dados em que os elementos são inseridos e removidos seguindo uma ordem específica de "último a entrar, primeiro a sair" (LIFO - Last In, First Out). A operação de inserção em uma pilha é chamada de "push" e a operação de remoção é chamada de "pop". A pilha possui ainda a operação "top" que retorna o elemento no topo da pilha sem removê-lo.

A implementação de pilha pode ser feita usando estruturas de dados encadeadas, onde cada elemento da pilha é um nó que contém um valor e um ponteiro para o próximo elemento. O primeiro elemento da pilha é chamado de topo da pilha e o último elemento é o fundo da pilha.

### Quais são as operações básicas de uma pilha?
As operações básicas de uma pilha são:

1) push: inserção de um elemento no topo da pilha;
2)pop: remoção do elemento do topo da pilha;
3) peek ou top: acesso ao elemento no topo da pilha, sem removê-lo;
4) isEmpty: verificação se a pilha está vazia.


### Como uma pilha pode ser implementada?
Uma pilha pode ser implementada de diversas maneiras, sendo as mais comuns por meio de um vetor ou por uma lista encadeada. Na implementação por vetor, utiliza-se um índice para indicar o topo da pilha, enquanto na implementação por lista encadeada, utiliza-se um ponteiro para o nó do topo.


### O que é uma pilha cheia e como evitá-la?
Uma pilha cheia ocorre quando não há mais espaço para adicionar novos elementos na pilha, geralmente na implementação por vetor. Para evitar essa situação, é possível aumentar o tamanho do vetor dinamicamente, ou utilizar uma implementação por lista encadeada, que não possui esse limite.

### Quais são as aplicações práticas de uma pilha?
Algumas aplicações práticas de uma pilha incluem: gerenciamento de memória, processamento de expressões matemáticas, histórico de navegação em navegadores web, desfazer e refazer ações em editores de texto, entre outras.

### Quais são as suas vantagens e desvantagens?
As principais vantagens de se utilizar uma pilha encadeada são:

* Flexibilidade na inserção e remoção de elementos, já que não é necessário realocar toda a estrutura;
* Possibilidade de implementar uma pilha com tamanho dinâmico;
* Possibilidade de utilização de recursão para solução de problemas que requerem a estrutura LIFO.


Já as principais desvantagens são:

* Custo em termos de memória para manter os ponteiros;
* Dificuldade em acessar um elemento arbitrário sem percorrer toda a pilha;
*Ineficiência na busca de um elemento em uma posição específica na pilha.







