---
content_hash: 1e3236d4512da434a566337f63c5ae89423cb683aa2701b562292fd92cff52a3
fetched_at: '2026-06-29T00:08:47.247228+00:00'
page_id: '319787278'
product: rm
source: tdn-rm
title: Manual - Ligação do Campo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=319787278
version: 3
---

A ligação do campo contém as informações para preenchimento do valor do campo do registro. Existem vários tipos de ligação de acordo com o valor a ser utilizado no campo. Para fazer uma nova ligação deve-se arrastar um campo do contexto para o campo do registro criando assim a ligação de Contexto ou de Registro de acordo com o campo que é arrastado. Conforme o seguinte exemplo:

![](/download/attachments/319787278/07B96BADCEDD024A228204F80609FDDE.jpg?version=1&modificationDate=1512921855000&api=v2)

Para poder arrastar o campo da lista GCOLIGADA, é necessário que o registro esteja associado a ela. Caso contrário o gerador não irá permitir que o campo seja associado. No caso do campo de Parâmetro Coligada, como ele não está associado a nenhuma lista, a sua ligação será criada como uma ligação de Contexto e não há necessidade de fazer a associação ao Registro pois o mesmo não pertence a uma lista.

É possível também definir os outros tipos de ligação clicando no botão ao lado da coluna de ligação "...".

![](/download/attachments/319787278/ligacao_do_campo.png?version=1&modificationDate=1512921856000&api=v2)

1Tipo de Ligação

O tipo de ligação define que tipo de valor está ligado ao campo. Os seguintes tipos estão disponíveis:

##### Contexto

A ligação de contexto indica que o valor do campo tem como base o valor de um campo do contexto. Somente campos que não são de uma lista podem ser utilizados como valor de contexto. Para fazer a associação, deve-se arrastar o campo do contexto para o campo do registro. Para mais informações consulte a [Ligação de Contexto](/display/LRM/Manual+-+Contexto).

##### Registro

A ligação de registro é criada quando um campo da ligação do contexto associada ao registro é arrastado para um campo do registro. Quando um registro possuir mais de uma ligação, os nomes dos campos das ligações devem ser os mesmos. Caso contrário o valor irá ficar vazio se a ligação não possuir o campo correspondente. Para mais informações consulte a [Ligação de Registro](/display/LRM/Manual+-+Registro).

##### Expressão

A ligação de expressão permite informar uma expressão C# como origem do valor do campo. Para mais informações consulte a [Ligação de Expressão](/pages/viewpage.action?pageId=319787281).

##### Valor Fixo

A ligação de valor fixo permite informar um valor fixo para o campo que será impresso em todos os registros. Para mais informações consulte a [Ligação de Valor Fixo](/display/LRM/Manual+-+Valor+Fixo).

##### Fórmula RM

A ligação de fórmula RM permite associar o resultado da execução de uma fórmula RM ao valor do campo. Para mais informações consulte a [Ligação de Fórmula RM](/pages/viewpage.action?pageId=319787283).

2Propriedades da Ligação

Na área de propriedades são exibidas as configurações da ligação do campo de acordo com o seu tipo.
