---
content_hash: 47223eebef8aeb59bb8ff07c899ec54b7a648956784095ff25d24e2b082b7a13
fetched_at: '2026-06-29T00:08:47.285814+00:00'
page_id: '319787289'
product: rm
source: tdn-rm
title: Manual - Contadores
type: documentation
url: https://tdn.totvs.com/display/LRM/Manual+-+Contadores
version: 3
---

O contexto de contadores permite que sejam criados indicadores e tabelas estatísticas baseado nos valores dos registros do Layout. É possível criar contadores baseados em um ou mais registros do Layout e os valores podem ser agrupados para fazer a contagem, soma, média e outras operações com os valores dos registros.

![](/download/attachments/319787289/contadores.png?version=1&modificationDate=1512921883000&api=v2)

1Adicionar

Clique para adicionar um novo contador ao contexto.

2Remover

Clique para remover o contador selecionado do contexto.

3Mover Para Cima

Clique para mover o contador selecionado para cima na lista de contadores do contexto.

4Mover Para Baixo

Clique para mover o contador selecionado para baixo na lista de contadores do contexto.

5Lista de Contadores

Exibe a lista de contadores disponíveis no contexto.

6Nome

Informe o nome do contador do contexto. Este nome deve ser único para o Layout e será usado para ligação do contador ao registro.

7Grupo

Informe o nome do grupo de contadores do contexto. Quando um contador é agrupado, o gerador irá criar uma "tabela virtual", fazendo o agrupamento dos dados dos contadores de acordo com os campos da sua chave primária. Esta tabela é disponibilizada como uma lista do contexto e seus campos serão todos os campos da chave primária e um campo para cada contador associado ao grupo.

Caso uma chave primária não seja informada, a tabela gerada irá conter 2 campos (NOME e VALOR), onde o será gerado um registro para cada contador do grupo contendo o nome e o valor calculado do contador.

Este recurso é usado principalmente em Layouts que possuem registros totalizadores, seja para contar a quantidade de registros do arquivo ou para fazer a soma de valores dos campos dos registro.

#### Exemplo

O registro 9900 do EFD PIS/ICMS é um exemplo de registro que utiliza o grupo de contadores para contar todos os registros do arquivo gerado. De acordo com a especificação da secretaria de fazenda este registro possui a seguinte estrutura:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Tipo** | **Tam** | **Dec** | **Obrig** |
| 01 | REG | Texto fixo contendo "9900". | C | 004 | - | O |
| 02 | REG\_BLC | Registro que será totalizado no próximo campo. | C | 004 | - | O |
| 03 | QTD\_REG\_BLC | Total de registros do tipo informado no campo anterior. | N | - | - | O |

Para gerar a tabela para este registro, deve ser criado um contador com as seguintes configurações:

1. Criar um campo chamado REG\_BLC em todos os registros do Layout. Este campo deve ter um valor fixo em cada registro, contendo o nome do registro correspondente como valor.
2. Criar um contador chamado QTD\_REG\_BLC (6) utilizando o modo "Contar" (13) e colocar o no nome do grupo (7) um nome para tabela.
3. Adicionar o campo REG\_BLC como chave primária do contador.
4. Associar todos os registros do Layout a este contador, arrastando o registro da árvore de registros para a lista de registros do contador (15). Não é necessário selecionar o campo, pois o modo é "Contar".

Ao fazer isso uma lista com o nome do grupo será exibida no contexto, para que seja feita a sua ligação com o registro 9900, esta tabela irá conter o campo REG\_BLZ (chave primária) e o campo QTD\_REG\_BLZ (nome do contador) que poderão ser arrastados para os campos 02 e 03 do registro 9900.

Dica

Além da totalização de registros, algums layouts necessitam também de totalizar valores dos registros. Neste caso o procedimento é o mesmo, porem deverá ser utilizado o modo de agrupamento "Somar" e um campo contendo o valor a ser somada deverá ser escolhido na coluna CAMPOS da lista de registros do contador.

Se for necessário a soma de mais de um campo do mesmo registro, utilize o mesmo grupo para todos os contadores de campos criados, criando assim uma tabela virtual com uma coluna para cada campo da chave e uma para cada contador do grupo.

8Chave

Exibe a lista de campos do registro que serão utilizados como chave primária para agrupamento da "tabela virtual" do contador. Esta informação só é necessária caso seja informado um grupo para o contador.

9Adicionar Chave

Clique para adicionar um campo do registro na chave do grupo do contador.

10Remover Chave

Clique para remover o campo selecionado da chave do grupo do contador.

11Mover Chave Para Cima

Clique para mover o campo selecionado da chave para cima.

12Mover Chave Para Baixo

Clique para mover o campo selecionado da chave para baixo.

13Modo de Agrupamento

Selecione o modo como é feito o agrupamento dos dados do registro para este contador. Os modos disponíveis são:

|  |  |
| --- | --- |
| Contar | Utilize este modo para que o contador faça a contagem do(s) registro(s) associado(s). |
| Somar | Utilize este modo para que o contador faça uma soma do campo do(s) registro(s) associado(s). |
| Mínimo | Utilize este modo para que o contador utilize o valor mínimo do campo do(s) registro(s) associado(s). |
| Máximo | Utilize este modo para que o contador utilize o valor mínimo do campo do(s) registro(s) associado(s). |

Importante

Quando o agrupamento for Somar, Mínimo ou Máximo o campo associado do registro deve ser do tipo Inteiro ou Decimal. Não é possível utilizar o agrupamento de campos que não sejam destes tipos.

14Remover Registro

Clique para remover o registro associado ao contador.

15Lista de Registros

Exibe a lista de registros associados ao contador. Caso o modo de agrupamento não seja "Contar", o campo do registro deve ser selecionado para que o gerador faça a operação de agrupamento selecionada usando o valor do campo do registro selecionado.

Atenção

Para fazer a associação do registro com o contador, é necessário arrastar o registro da árvore de registros do Layout para a lista de registros do contador criando assim a ligação entre eles.

![](/download/attachments/319787289/B13415C05A5F2AD48648339056C30605.jpg?version=1&modificationDate=1512921884000&api=v2)
