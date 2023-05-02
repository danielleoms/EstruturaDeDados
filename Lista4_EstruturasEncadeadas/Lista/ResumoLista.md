Este é um exemplo de implementação de lista encadeada com as funções de inserção, remoção e busca definidas como métodos da classe Lista.

A classe Node é utilizada para criar um nó, que armazena um dado (data) e uma referência para o próximo nó (next). A classe Lista possui um atributo head que é uma referência para o primeiro nó da lista.

O método inserir insere um novo nó no final da lista. Se a lista estiver vazia, o novo nó é atribuído como head. Caso contrário, percorre a lista até encontrar o último nó e atribui o novo nó como o próximo do último nó.

O método remover remove o nó que contém o dado especificado. Se o dado estiver no primeiro nó (head), o head é atualizado para o próximo nó. Caso contrário, percorre a lista até encontrar o nó anterior ao nó que contém o dado e atualiza a referência next deste nó para pular o nó que será removido.

O método buscar percorre a lista até encontrar o nó que contém o dado especificado. Se encontrar, retorna True, caso contrário, retorna False.


## Método inserir(), remover() e buscar()

Nesse exemplo, a classe Lista possui três métodos: inserir(), remover() e buscar().

O método inserir() recebe um dado como argumento e cria um novo nó com esse dado. Se a lista estiver vazia, o novo nó é definido como a cabeça da lista; caso contrário, o novo nó é adicionado ao final da lista.

O método remover() recebe um dado como argumento e remove o nó correspondente da lista, caso exista. Se a lista estiver vazia, não há nada a ser removido. Se o nó a ser removido for a cabeça da lista, o método atualiza a cabeça da lista para o próximo nó. Caso contrário, o método percorre a lista até encontrar o nó a ser removido e atualiza o ponteiro next do nó anterior para apontar para o próximo nó.

O método buscar() recebe um dado como argumento e percorre a lista procurando por um nó que contenha esse dado. Se encontrar o nó, o método retorna True; caso contrário, retorna False.
