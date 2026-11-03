---
content_hash: f5c8b8f0b57be76f94b35ba38665ca5b7261b2024e022234111b6ded69237474
fetched_at: '2026-06-29T00:08:47.230737+00:00'
page_id: '319787272'
product: rm
source: tdn-rm
title: Manual - Ligação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=319787272
version: 5
---

A ligação do registro define quais dados serão utilizados para geração do registro. Para associar uma ligação a um registro deve-se arrastar e soltar uma tabela do contexto para o campo de ligações. Cada registro pode estar associado a uma ou mais ligações de origem, desde que os campos utilizados no registro possuam os mesmos nomes para todas as ligações.

![](http://tdn.totvs.com/download/attachments/319787272/ligacao.png?version=1&modificationDate=1512921837000&api=v2)

1Ligação

A aba de ligação exibe as configurações de cada ligação associada ao registro. Clique nas ligações para alterar as propriedades específicas da ligação ([Filtro](http://tdn.totvs.com/display/LRM/Manual+-+Filtro) e [Ignorar Ligações](http://tdn.totvs.com/pages/viewpage.action?pageId=319787273)).

2Lista de Ligações do Registro

Um registro pode estar associado a uma ou mais listas de origem. Para fazer a associação você deverá arrastar uma tabela de um contexto para o controle da lista. Se for uma lista filha, o registro pai deverá estar associado a lista pai desta lista. Para mais informações consulte a [Configuração do Contexto.](http://tdn.totvs.com/display/LRM/Manual+-+Contextos)

Atenção

Para fazer uma ligação, você deve arrastar uma lista do contexto para a lista de ligações do registro.

![](http://tdn.totvs.com/download/attachments/319787272/895D7B482C8C7C87F294A9F6D9F33949.jpg?version=1&modificationDate=1512921840000&api=v2)

3Filtro da Ligação

Informe uma expressão que será utilizada para verificar se o registro deverá ser gerado de acordo com os dados de origem da ligação. Esta expressão deverá retornar um valor do tipo lógico (bool). Para mais informações consulte [Expressões](http://tdn.totvs.com/pages/viewpage.action?pageId=319787306).

4Ignorar Ligações

A aba ignorar ligações permite ignorar a geração da ligação selecionada para de acordo com a ligação do registro pai. Para mais informações consulte [Ignorar Ligações](http://tdn.totvs.com/pages/viewpage.action?pageId=319787273).

5Ligação sob-demanda

A aba de ligação sob-demanda permite fazer a leitura de um contexto sob-demanda baseado nos dados da ligação principal. Esta opção tem um custo elevado e deve ser utilizada em último caso, pois para cada registro da ligação é feita uma nova leitura dos dados do contexto sob-demanda, o que aumenta o consumo do banco e dados. Para mais informações consulte [Ligação sob-demanda](http://tdn.totvs.com/pages/viewpage.action?pageId=319787274).

6Filtro

A aba filtro permite criar uma expressão de filtro para o registro independente da ligação. Diferente do filtro da ligação, esta expressão somente pode utilizar dados do contexto, pois ela será executada antes do gerador percorrer a lista da ligação. Para mais informações consulte [Filtro](http://tdn.totvs.com/display/LRM/Manual+-+Filtro).

7Ordenação

A aba de ordenação permite ao gerador ordenar os registros do arquivo de saída de acordo com os dados do registro. Utilize esta opção somente se não for possível a ordenação dos dados no contexto, pois para fazer a ordenação todos os dados do registro são mantidos em memória até o término da geração para permitir a ordenação. Para mais informações consulte [Ordenação](http://tdn.totvs.com/pages/viewpage.action?pageId=319787276).

Hierarquia

Importante

As ligações devem obecer a hierarquia dos registros, podendo o registro só ser associado a mesma ligação do registro pai, ou a uma ligação que seja filha de uma ligação do registro pai.

Temas da MDI

Alguns temas visuais da MDI podem dificultar a visualização dos dados na ligação. Nesse caso, é necessário utilizar outro tema.
