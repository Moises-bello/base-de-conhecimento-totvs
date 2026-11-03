---
content_hash: e2cf033f2f1703fe30a97ddfeedd8ac01aeb6dce40614871bc9ce6f0b31a09b3
fetched_at: '2026-06-29T00:08:47.234733+00:00'
page_id: '319787274'
product: rm
source: tdn-rm
title: Manual - Ligação sob-demanda
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=319787274
version: 3
---

A aba de ligação sob-demanda permite fazer a leitura de um contexto sob-demanda baseado nos dados da ligação principal. Você deve alterar o modo de leitura do contexto para "Sob-demanda" para poder utilizar o contexto sob-demanda. Para mais informações consulte a [Configuração do Contexto](/display/LRM/Manual+-+Contextos).

![](/download/attachments/319787274/ligacao_sobdemanda.png?version=1&modificationDate=1512921844000&api=v2)

1Lista de Ligações

Um registro pode estar associado a uma ou mais ligações sob-demanda. Para fazer a associação você deverá arrastar uma tabela de um contexto sob-demanda para o controle da lista. Ao fazer essa associação é necessário informar os valores dos parâmetros do contexto associado, para isto é necessário arrastar os campos da ligação do contexto para os parâmetros da ligação sob-demanda. Também é possível informar valores fixos ou utilizar uma expressão para calcular o valor.

2Remover

Clique para remover a ligação sob-demanda do registro.

3Parâmetro da Ligação

Nesta área são exibidos os parâmetros do contexto da ligação, você deverá associa-los aos campos da ligação do registro, arrastando cada campo para para o parâmetro desejado.

4Tipo do Parâmetro da Ligação

O tipo de parâmetro exibe o tipo de dado do parâmetro somente para consulta.

5Valor do Parâmetro

Clique para visualizar o valor do parâmetro associado. O popup de ligações será exibido com as configurações do valor. Para mais informações consulte o tópico sobre [Ligação do Campo](/pages/viewpage.action?pageId=319787278).

Atenção

Esta opção tem um custo elevado e deve ser utilizada em último caso, pois para cada item da ligação do registro, é feita uma nova leitura dos dados do contexto sob-demanda, o que aumenta o consumo do banco e dados e o tempo de geração. O ideal que é a ligação principal sempre faça a leitura de todos os dados necessários para geração do registro.

Normalmente a ligação sob-demanda será necessária para adicionar informações customizadas aos Layouts baseados em Contextos de Biblioteca .NET, pois as mesmas não podem ser extendidas.
