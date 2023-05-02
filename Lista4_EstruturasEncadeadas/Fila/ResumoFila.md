## Resumo Fila

Uma fila é uma estrutura de dados linear que segue a regra FIFO (First-In, First-Out), ou seja, o primeiro elemento a ser inserido é o primeiro a ser removido. As filas podem ser implementadas utilizando-se estruturas encadeadas, que são formadas por uma série de nós conectados, onde cada nó contém um elemento da fila e um ponteiro para o próximo nó.


### O que é uma fila?
Uma fila é uma estrutura de dados que armazena elementos em ordem linear, onde a inserção de novos elementos é feita no final da fila e a remoção é feita no início da fila.

### Quais são as principais operações em uma fila?
Resposta: As principais operações em uma fila são: enfileirar (inserir um elemento no final da fila), desenfileirar (remover um elemento do início da fila) e consultar o elemento que está no início da fila.

### Como implementar uma fila usando um vetor?
 Para implementar uma fila usando um vetor, é necessário manter um índice para o início da fila e outro para o final da fila. A inserção de novos elementos é feita no final da fila, incrementando o índice do final, e a remoção é feita no início da fila, incrementando o índice do início. É importante tomar cuidado com a fila cheia e vazia.

### Como implementar uma fila usando uma lista encadeada?
Para implementar uma fila usando uma lista encadeada, é necessário criar uma estrutura que represente um nó da lista, contendo um ponteiro para o próximo nó e o valor do elemento armazenado. Além disso, é necessário manter um ponteiro para o início da fila e outro para o final da fila. A inserção de novos elementos é feita no final da fila, criando um novo nó e atualizando o ponteiro do final, e a remoção é feita no início da fila, atualizando o ponteiro do início e liberando o nó removido.

### Quais são as vantagens e desvantagens de se utilizar uma fila?
Uma vantagem de se utilizar uma fila é que ela é uma estrutura simples e eficiente para se implementar algoritmos que envolvem processamento de dados em ordem linear. Além disso, ela pode ser utilizada em diversos problemas, como simulação de filas de espera, processamento de requisições em sistemas, entre outros. Uma desvantagem é que a remoção de elementos no meio da fila não é possível, o que pode ser um problema em alguns casos. Além disso, a inserção de novos elementos no final da fila pode ser lenta em listas encadeadas grandes, pois é necessário percorrer toda a lista.

### As principais operações em uma fila encadeada são:

* Enfileirar (push): insere um elemento no final da fila.
* Desenfileirar (pop): remove o elemento do início da fila.
* Verificar se a fila está vazia (empty): retorna verdadeiro se a fila está vazia e falso caso contrário.
* Obter o elemento do início da fila (front): retorna o elemento do início da fila sem removê-lo.
* Obter o elemento do fim da fila (back): retorna o elemento do fim da fila sem removê-lo.
* As vantagens de se utilizar uma fila encadeada incluem a capacidade de adicionar ou remover elementos do início ou do final da fila em tempo constante (O(1)), sem necessidade de realocação de memória. No entanto, a desvantagem é que o acesso aos elementos intermediários da fila é menos eficiente do que em outras estruturas de dados, como os vetores.

### Utilização da Classe Node em Fila:

Assim como em outras estruturas de dados encadeadas, a classe Node também é utilizada na implementação de filas encadeadas. Ela é responsável por armazenar o valor do elemento da fila e um ponteiro para o próximo elemento da fila.
A classe Node é utilizada para representar cada nó da fila, e possui duas variáveis: uma para armazenar o elemento da fila e outra para o ponteiro para o próximo nó. A fila é representada por um ponteiro para o primeiro nó (início) e um ponteiro para o último nó (fim).
