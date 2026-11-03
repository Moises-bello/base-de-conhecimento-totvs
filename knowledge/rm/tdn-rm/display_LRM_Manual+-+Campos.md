---
content_hash: 14efa6ceb409defb1b230f1c12c15c05860ed22ac320b0d6899dc9520324025c
fetched_at: '2026-06-29T00:08:47.244454+00:00'
page_id: '319787277'
product: rm
source: tdn-rm
title: Manual - Campos
type: documentation
url: https://tdn.totvs.com/display/LRM/Manual+-+Campos
version: 3
---

As configurações de campos do registro definem a estrutura da linha que será gerada para o registro. Cada campo deve estar associado a uma ligação que pode ser um campo da ligação do registro, um valor fixo, uma expressão e/ou outros.

![](/download/attachments/319787277/campos.png?version=1&modificationDate=1512921851000&api=v2)

1Adicionar Campo

Clique para adicionar um novo campo visível ao registro.

2Adicionar Campo Invisível

Clique para adicionar um novo campo invisível ao registro. Estes campos geralmente são utilizados pelas expressões de cálculo do registro, e possuem todas as propriedades de um campo normal, porém ele não é gerado no arquivo de saída. Para mais informações consulte [Expressão de Campo](/pages/viewpage.action?pageId=319787281).

3Remover

Clique para remover o campo selecionado no registro.

4Mover para cima

Clique para mover o campo um item acima da posição atual.

5Mover para baixo

Clique para mover o campo um item abaixa do posição atual.

6Exibir Origem

Clique para alternar entre a visualização do tipo de ligação do campo.

7Campos Visíveis

Área onde são exibidos os campos visíveis do Layout. Estes campos irão ser gerados no arquivo na ordem determinada.

8Campos Invisíveis

Área onde são exibidos os campos invisíveis do Layout. Estes campos podem ser utilizados para composição da chave do registro, para utilização no cálculo de expressões e para ordenação dos registros.

9Posição

Exibe a ordem do campo visíveis no registros.

10Nome do Campo

Define o nome do campo do registro, o nome deve ser único por registro e pode ser acessado pelas expressões de cálculo do registro.

11Descrição

Informe um texto descritivo para o campo. Este texto será utilizado para geração do arquivo de documentação do Layout.

12Modo

Selecione o modo de agregação do campo quando o registro possui campos de chave primária definidos. Nestes casos podem ser feitos vários tratamentos com os dados de origem. É possível gerar registros agrupadores como por exemplo, registros de cabeçalho e rodapé de arquivo e registros de totalização de valores ou registros utilizando o modo de chave primária em conjunto com as operações de somar ou contar.

Os seguintes modos de agregação do registro estão disponíveis:

##### Chave Primária

Esta opção define que o campo será utilizado para compor a chave primária do registro. Quando um registro contém uma chave primária, todos os valores de origem serão agregados de acordo com a regra de cada campo do registro para cada composição de chave. Na prática esta opção cria um registro agrupador, onde um ou mais registros de origem que tenham a mesma chave irão gerar somente um registro no arquivo de saída.

Os outros modos de registro serão válidos somente quando o registro possuir pelo menos um campo de chave primária ou quando o tipo do registro for "Registro".

##### Primeiro Valor

Essa opção define que o valor do primeiro registro de origem atribuido ao campo que irá ser gerado no arquivo de saída. Neste caso os valores subsequentes serão descartados.

##### Último Valor

Essa opção define que o valor do último registro de origem atribuido ao campo que irá ser gerado no arquivo de saída. Neste caso os valores dos registros anteriores serão descartados.

##### Sequencial

Essa opção define que o valor do registro será um valor incremental para cada registro pai. Neste caso o valor de origem do registro não importa, pois sempre será gerado um número sequencial para o campo.

##### Contar

Essa opção irá fazer um somatório para cada valor associado ao campo independente do seu valor. Neste caso se o valor de origem for vazio ou nulo, o contador não será incrementado.

##### Somar

Essa opção irá somar todos os valores adicionados ao campo, para isso somente podem ser utilizados como origem, campos de número inteiro ou decimal. Neste caso qualquer outro valor que não seja numérico será descartado.

##### Média

Essa opção irá fazer uma média de todos os valores adicionados ao campo, para isso somente podem ser utilizados como origem, campos de número inteiro ou decimal. Neste caso qualquer outro valor que não seja numérico será descartado.

13Tamanho

Define o tamanho máximo do campo, se o seu valor ultrapassar este tamanho, o mesmo será truncado e um aviso será exibido no Log de geração do arquivo. Este valor também é utilizado para preencher o valor do campo com o caractere definido na formatação, necessário para criação de arquivos de tamanho fixo como por exemplo os padrões CNAB.

14Posição

Exibe a posição que o campo ocupa no registro. Esta informação é útil para validação do registro de arquivos de tamanho fixo.

15Requerido

Indica se o valor do campo é de preenchimento obrigatório. Caso o seu valor não seja informado um aviso será exibido no Log de geração.

16Tipo de dado

Indica qual é o tipo de dado do campo. O seu valor de saída será formatado de acordo com o seu tipo, utilizando a formatação padrão do Layout, ou a formatação específica do campo caso a mesma seja informada. Quando uma formatação específica está definida para o campo, o texto do tipo será exibido em negrito. Para alterar a formatação específica do registro, clique no botão "..." ao lado do tipo de dado.

17Ligação

Exibe a informação da ligação do campo, clique para alterar a sua configuração ou arraste um campo do contexto para criar uma ligação de registro ou de contexto. Existem vários tipos de ligações possíveis que são:

##### Contexto

As ligações de contexto são criadas ao arrastar um campo do contexto para um campo do registro. Somente campos que não sejam de uma lista podem ser arrastados desta forma. Como por exemplo campos do contexto de parâmetros ou campos do contexto de contadores. Para mais informações consulte [Ligação de Contexto](/display/LRM/Manual+-+Contexto).

##### Registro

As ligações de registro também são criadas ao arrastar um campo do contexto para um campo do registro, mas neste caso o campo arrastado pertence a uma ligação associada ao registro ou aos seus registros pais. Para mais informações consulte [Ligação de Registro](/display/LRM/Manual+-+Registro).

##### Valor Fixo

Esta opção é usada para definir um valor fixo para o campo. Para mais informações consulte [Ligação de Valor Fixo](/display/LRM/Manual+-+Valor+Fixo).

##### Expressão

Esta opção é usada para definir uma expressão que irá formar o valor do campo. A expressão de campo pode utilizar qualquer valor da ligação do campo, também podem usar valores de campos de contexto e executar funções para tratamento dos valores. No caso das expressões de campo, ao clicar no CheckBox "Utilizar expressão no cálculo do registro", a mesma será executada após todos os campos do registros tiverem sido preenchidos e seus valores calculados. E nesta condição somente os valores dos campos do registro estão disponíveis para uso na expressão sendo estes valores visíveis ou não. Para mais informações consulte [Ligação de Expressão](/pages/viewpage.action?pageId=319787281).

##### Fórmula (RM)

Esta opção é usada para que o valor do campo seja calculado a partir de uma fórmula do RM, ela esta disponível somente para o gerador de saídas integrado no RM. Para mais informações consulte [Ligação de Fórmula (RM)](/pages/viewpage.action?pageId=319787283).

Atenção

Para fazer uma ligação de Registro ou de Contexto, você deve arrastar um campo do contexto para o campo do registro.

![](/download/attachments/319787277/F811250B8437AE382DDB3F599DC31A66.jpg?version=1&modificationDate=1512921853000&api=v2)

18Propriedades do Registro

Clique neste botão para exibir todas as propriedades do registro. Além poder altera-las também é possível definir uma regra de "dê/para" dos valores do campo. Para mais informações consulte [Conversão de Valores](/pages/viewpage.action?pageId=319787284).
