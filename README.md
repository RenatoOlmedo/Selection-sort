# Selection Sort

Algoritmo criado com base no desafio proposto pela DSA (Data Science Academy): Implementar o Algoritmo de Ordenação "Selection sort"

## Premissas
### As duplicatas são permitidas?
* Sim
### Podemos assumir que a entrada é válida?
* Não
### Podemos supor que isso se encaixa na memória?
* Sim

## Raciocínio de resolução
Existem diversas, talvez milhares de formas diferentes para resolver o mesmo problema, dessa forma, tentei resolver do jeito mais simples que encontrei.

Ao pesquisar a respeito do selection sort percebi que o algorítmo primeiro passa por todos os itens da lista e procura o menor deles, trocando-o de posição com o primeiro item da lista, a seguir ele continua partindo do segundo item, fazendo exatamente o mesmo processo.

Percebi que seriam necessários dois loops, um dentro do outro, o primeiro para percorrer a lista e marcar a posição que será ordenada através da variável(`posicaoSort`) e o segundo para percorer o restante da lista ainda não ordenado e encontrar o menor valor substituindo os dois.

No entanto, fazendo testes me deparei com o seguinte problema: quando haviam números duplicados fica impossível de encontrar a posição do menor número encontrado através do seu valor, pois acaba encontrando sempre o primeiro (quando são dois), resultando em uma ordenação completamente equivocada.

Sendo assim, decidi criar uma variável para marcar a exata posição em que o menor número da parte não ordenada da lista se encontrava(`posicaoMenor`), não seria viável criar um simples contador de posições, pois o loop não para ao encontrar o menor número, só salva o valor em uma variável(`menorValor`), então decidi que ao encontrar um valor mais baixo que o atual, a posição do menor valor seria definida como a posição atual de ordenação somado ao contador de itens não ordenados(`counter`).

### Te convido a clonar a solução, alterar a lista e testar a ordenação por conta própria
