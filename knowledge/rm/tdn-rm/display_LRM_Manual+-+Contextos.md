---
content_hash: 5d9fe9bf74954019bc4690768842f5a2735d008c2b908f93a0ceb7159c2e8224
fetched_at: '2026-06-29T00:08:47.263713+00:00'
page_id: '319787286'
product: rm
source: tdn-rm
title: Manual - Contextos
type: documentation
url: https://tdn.totvs.com/display/LRM/Manual+-+Contextos
version: 3
---

Os contextos do gerador são responsáveis pela disponibilização dos dados que serão utilizados para preenchimento dos registros do Layout. Existem vários tipos de contextos que podem ser utilizados dependendo da origem da informação. Algums contextos são únicos o podem ser adicionados ao Layout somente uma vez, desta forma após adicionado, o seu menu ficará desabilitado.

![](/download/attachments/319787286/contextos.png?version=1&modificationDate=1512921873000&api=v2)

1Nome

Informe o nome do contexto. Este nome deve ser único para o Layout e não pode ter o mesmo nome que um arquivo, registro ou contexto.

2Modo de Carga

Selecione o modo de carga do Layout, esta opção é habilitada somente para alguns tipos de contexto. Os modos disponíveis são:

##### Carregado no início da geração

Ao utilizar este modo, o contexto será carregado no início da geração do Layout, desta forma seus dados poderão ser utilizado como ligação principal dos registros.

##### Carregado sob-demanda

Ao utilizar este modo, o contexto será carregado sob-demanda. Neste caso os seus dados só poderão ser utilizados através da associação na aba de ligação sob-demanda dos registros. Para mais informações consulte [Ligação sob-demanda](/pages/viewpage.action?pageId=319787274).

##### Carregado sob-demanda (Cacheado)

Este modo tem o funcionamento igual ao carregado sob-demanda, porém os dados lidos por este contexto serão armazenados em um cache em memória do acordo com os parâmetros de leitura do contexto. Utilize esta opção caso os parâmetro de leitura forem repetidos muitas vezes para os registros principais. Diminuindo assim a carga do banco de dados.

3Parâmetros

Caso o contexto possua parâmetros de leitura, os mesmos serão exibidos na guia de parâmetros para que os seus valores sejam definidos. Para mais informações consulte [Parâmetros do Contexto](/pages/viewpage.action?pageId=319787287).

4Árvore do Contexto

Na árvore do contexto são exibidos todos os dados disponibilizados por cada contexto do Layout. Alguns dados são expostos como listas e outros como campo. Os campos pertecentes a uma lista só poderão ser associados ao registro caso a lista esteja associada a ligação do registro.

Para fazer a associação é necessário arrastar e soltar a lista ou campo do contexto para a ligação ao campo do registro, criando assim a associação entre ambos.

Os dados do contexto são organizados de forma hierárquica, onde uma lista pode possuir campos ou listas filhas. No caso de uma lista filha, a mesma só poderá ser associada a um registro cujo registro pai esteja associado a lista pai.

#### Estrutura do Contexto

Cada contexto pode possuir um ou mais elementos de lista, membro ou campos. A árvore de contexto exibe todos estes elementos para que possam ser arrastados aos registros ou campos do Layout, criando assim a ligação entre eles.

![](/download/attachments/319787286/CACCD254F3268D674FA675C8F1918099.jpg?version=1&modificationDate=1512921875000&api=v2)

##### Nó de Contexto

Um nó de contexto é exibido para cada contexto utilizado no Layout. Clique duas vezes nele para alterar as propriedades do mesmo. Na imagem acima podemos ver que os nós 1 e 9 representam dois contextos (Dados e Parametros).

##### Nó de Lista

Um nó de lista é exibido para cada lista exposta pelo contexto. Uma lista contém um conjunto de dados que serão utilizados para geração dos registros associados. Arraste um nó de lista para a ligação do registro para fazer a associação entre eles. Na imagem acima podemos ver que os nós 2, 4, 7 e 8 representam listas que podem ser arrastas para um registro. Sendo que a lista 4 (COMPL) é filha da lista 2 (FCFO), portanto só poderá ser associada a um registro cujo registro pai esteja associado a lista FCFO.

##### Nó de Membro

Um nó de membro representa uma agrupamento de campos do contexto ela possui uma associação 1-1 com a lista pai, sendo assim um campo de um membro pode ser associado a um registro que esteja associado a sua lista pai. Na imagem acima podemos ver que o nó 3 (Coligada) é um membro da lista 2 (FCFO), portanto para utilizar seus valores, o registro deve estar associado a lista FCFO.

##### Nó de Campo

Um nó de campo representa um campo de uma lista ou contexto do gerador. Um campo de lista só pode ser associado a um campo de um registro que esteja associado a sua lista ou esteja associado a uma lista de um registro pai. Na imagem acima podemos ver que os nó 5 (CODCFO) representa um campo da lista 4 (COMPL), portanto para utilizar o seu valor em um registro, o mesmo deve estar ligado a lista 4. Vemos também que o nó 10 (Coligada) representa um campo do contexto 9 (Parametros). Neste caso, como o campo coligada não pertence a uma lista, ele pode ser associado a qualquer campo do Layout criando assim uma ligação de contexto.

5Propriedades

As propriedades do contexto são exibidas de acordo com o tipo de contexto, para mais informações consulte a documentação de cada tipo de contexto disponível.
