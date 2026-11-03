---
content_hash: c03cb2a7f124446e934df611ad0ec745bfe676882b5133062bcac9eb1e1d8d22
fetched_at: '2026-06-29T00:08:47.226844+00:00'
page_id: '319787271'
product: rm
source: tdn-rm
title: Manual - Configuração do Registro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=319787271
version: 3
---

O registro do Layout contém um conjunto de propriedades define a estrutura das linhas do arquivo a ser gerado, quais dados serão utilizados para geração e faz toda a transformação necessária nos dados de origem para geração do registro do arquivo. É possível gerar um registro a partir de uma ou mais listas de origem, e para cada lista é possível aplicar um filtro condicionando a geração do registro de acordo com o dado de origem.

Os registros são organizados em forma de árvore, podendo ter vários níveis de detalhe conforme a necessidade de cada Layout.

![](/download/attachments/319787271/configuracao_do_registro.png?version=1&modificationDate=1512921834000&api=v2)

1Nome

Informe o nome identificador do registro. O nome do arquivo deve ser único para o Layout e será usado para acessar as propriedades do registro através das expressões de campo.

2Arquivo

Selecione o arquivo ao qual o registro pertence. Por padrão os registros são associados ao primeiro arquivo do Layout.

3Descrição

Informe um texto descritivo para o registro. Este texto será utilizado para geração do arquivo de documentação do Layout.

4Tipo

Selecione o tipo de registro. Esta opção interfere em como o registro será gravado no arquivo final. As opções disponíveis são:

##### Lista

O tipo de registro lista, indica que serão gerados vários registros no arquivo de saída, para cada item da ligação de origem. Este o é valor padrão para esta propriedade.

##### Registro

Este tipo de registro indica que será gerado somente um registro no arquivo de saída, para cada registro pai independente da quantidade de items da ligação de origem.

##### Agrupador

Este tipo de registro indica que não será gerado nenhum registro no arquivo de saída. Quando esta opção é utilizada, o gerador irá gerar somente os registros filhos do registro agrupador. Normalmente este tipo de registro é necessário quando é preciso gerar uma lista filha, sem que a lista pai seja gerada.

5Requerido

Indica se o registro deve ser gerado obrigatóriamente no arquivo de saída mesmo que os dados de origem não contenham nenhuma informação. Neste caso, o registro será gerado com os valores de campos nulos definidos na formatação.

6Ligação, Filtro e Ordenação

Nestas abas serão informados quais dados de origem (ligação) serão utilizos para geração do registro, qual filtro será aplicado para cada ligação associada ao registro, as suas ligações sob-demanda e quais campos deverão ser usados para ordenação do registro. Para mais informações consulte a [Configuração da Ligação](/pages/viewpage.action?pageId=319787272).

7Campos e Opções

Nesta área são definidos todos os campos do Layout, seu tamanho, formatatação e qual o seu valor de origem. Para mais informações consulte a [Configuração de Campos](/display/LRM/Manual+-+Campos) e [Opções do Registro](/pages/viewpage.action?pageId=319787285).
