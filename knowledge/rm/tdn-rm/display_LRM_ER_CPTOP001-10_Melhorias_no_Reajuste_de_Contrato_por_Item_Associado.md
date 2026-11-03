---
content_hash: 7d13a515e4c115f50440d875b2e08583785dd9d8e16d7b870b407ccfb5f1cb1d
fetched_at: '2026-06-29T00:08:10.791539+00:00'
page_id: '240981454'
product: rm
source: tdn-rm
title: ER_CPTOP001-10_Melhorias_no_Reajuste_de_Contrato_por_Item_Associado
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_CPTOP001-10_Melhorias_no_Reajuste_de_Contrato_por_Item_Associado
version: 33
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Contratos |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | CPTOP001 | **IRM1** | CPTOP001-9 |
| **Requisito1** | CPTOP001-10 | **Subtarefa1** | CPTOP001-123 |
| **Chamado2** |  | | |
| **País** | (X) Brasil  (  ) Argentina  (  ) México  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colômbia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | |  |  | | --- | --- | | **Pré-requisitos para melhor entendimento da especificação** | | | **Entidade** | **Link** | | Reajuste de contrato de maneira diferenciada por tipo de serviço contratado |  | | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Possibilitar melhorias no processo de Reajustar Itens Associados ao Contrato e em algumas funcionalidades envolvidas.

## Definição da Regra de Negócio

O processo de Reajustar Itens Associados ao Contrato requer algumas melhorias para que o reajuste possa ser considerado e definido de uma forma mais flexível, sendo assim, o mesmo e algumas funcionalidades que envolvem esse processo deverão ser alterados.

**1 - Tipo de Aplicação do Reajuste (Incidência do Reajuste)**

No cadastro do contrato deverá ter a opção, "Aplicação do Reajuste" () que permite informar se o reajuste deverá incidir sobre o valor inicialmente contratado, que representa o valor antes do primeiro reajuste realizado para o item, ou no valor atual, pois este pode ter sofrido reajustes anteriores. Essa opção está presente no próprio processo e deverá ser retirada, pois se trata de uma característica do contrato, e somente estará habilitado e disponível se o tipo de reajuste definido for "Por Item Associado" e não existirem reajustes já realizados para o contrato, pois, caso contrário, o valor do item poderia ser diminuído em reajuste posteriores.

**2 - Agrupamento de Reajustes de Itens Associados**

Para o reajuste de item associado, é necessário que a aplicação do índice (percentual) seja realizada para um grupo de itens. O DNIT, por exemplo, pode definir o índice de reajuste de acordo com o grupo:

* + Drenagem: 3%
  + Consultoria: 4,5%
  + INCC: 2,8%

Sendo assim, o processo de Reajustar Itens Associados ao Contrato deverá permitir esse agrupamento através do grid de itens, porém será necessário disponibilizar uma nova coluna que deverá representar esse agrupador do item associado ().

Para a definição de índices, deverá ser utilizado o cadastro de Moedas e Índices já existente no sistema (). O cadastro de cotações não será obrigatório, porém caso sejam feitas, será sugerido na tela do processo de reajuste a cotação referente à data selecionada para o reajuste, ficando a critério do usuário utilizar ou não. Se houver necessidade de mais de uma cotação para a mesma data de um mesmo índice, deverá ser criado um novo índice que contenha as cotações separadamente, como pode ocorrer com o INCC que pode variar de estado para estado no Brasil:

* + INCC-RJ: Cotação em 01/06/2016 = 0,0625;
  + INCC-MG: Cotação em 01/06/2016 = 0,0732.

No anexo de Itens do Contrato e no processo de Associação de itens ao contrato, deverá ser possível relacionar o índice ao item associado ao contrato ( e ), desta forma estará disponível, no processo de reajuste, a coluna com o respectivo índice do item (). A possibilidade de relacionar o índice ao item associado somente estará disponível se não existir reajuste realizado para o item no contrato.

Na tela do processo de Reajustar Itens Associados, em caso de não existirem índices associados aos itens do contrato, o campo para informar o Percentual deverá ser exibido para que o o usuário possa aplicá-lo aos itens selecionados no grid, porém, se existirem índices, deverá ser criado uma opção, através de um grid, para que o usuário possa definir o percentual de reajuste para cada índice associado aos itens contratados ():

* + Exibir somente índices associados aos itens do contrato;
  + Possibilidade de definir o percentual para os itens que não possuem índice associado (Sem Índice Associado);
  + Não deverá ser possível selecionar tarefas no grid, o mesmo apenas apresentará os valores reajustados (simulação), como ocorre atualmente;
  + A execução do processo deverá aplicar todos os percentuais dos índices em uma única execução;
  + A sugestão de cotação deverá ser apresentada na forma em que foi cadastrada, por pode ser definida diretamente em percentual ou considerando variações, como por exemplo: INCC: Cotação em 01/06/2016 = 0,0625;
  + Os campos que o grid de índices apresentará são:
    - Índice: Código do índice;
    - Descrição: Descrição do índice;
    - Percentual: Campo para a edição do percentual;
    - Reajuste Sugerido (Cotação do Índice): Campo que apresenta a cotação de acordo com a data de reajuste definida. O valor apresentado será o mesmo informado no cadastro da cotação pois o índice pode ser informado considerando variação ou o próprio percentual, impedindo que fosse apresentado em percentual na tela do processo.

**3 - Reajustes quando existir período medido e liberado**

Em  algumas ocasiões pode acontecer de os índices de reajuste serem definidos no período posterior ao período onde o mesmo deve ser aplicado, porém podem existir períodos de contrato com medição e liberação realizados que correspondem ao intervalo onde o reajuste deverá ser aplicado. Atualmente, o processo de Reajustar Itens Associados ao Contrato não permite realizar reajustes para itens que estão medidos no período selecionado para o reajuste, sendo assim, o processo deverá ser modificado para que possibilite a aplicação do reajuste em itens que foram medidos ou liberados, obedecendo às seguintes regras:

* + Período Medido: Para itens em períodos medidos, deverá ser realizado o recálculo da medição com a atualização do valor atual de cada item considerando o reajuste, assim como o recálculo de todos os rateios que porventura foram definidos junto ao item medido. O recálculo deverá ser realizado, também, para todos os períodos medidos que tem a data maior que a data de reajuste. Períodos de estorno não deverão ser considerados pois o mesmo não deve ser recalculado pelo fato de ser um valor predefinido que não deveria ser ajustado;
  + Período Liberado: Para itens em períodos liberados, deverá ser realizado o cálculo da diferença entre o valor medido considerando o valor reajustado e o valor medido liberado e essa diferença deverá ser associada a um novo tipo de período, representado pele letra "R", semelhante ao  período complementar, mas originado de reajuste (), conforme exemplo:

    - Algumas regras deverão ser consideradas:
    - * O processo de Reajustar Itens Associados ao Contrato, após o cálculo da diferença, e esta sendo maior que zero(0), deverá criar um novo período complementar de reajuste para o período liberado, que será representado pela letra "R" (Ex.: 0001R001), inserir uma medição para o item com o valor da diferença, porém com a quantidade zerada, pois esta não deverá interferir no saldo quantitativo do item no contrato;
      * Esse novo tipo de período deverá ser criado pelo sistema, através do processo de Reajustar Itens Associados ao Contrato, sem possibilidade de uma inclusão manual;
      * Para esse tipo de período, com a característica de reajuste, somente será possível executar os processos de "Liberar Período" e "Gerar Integração com Suprimento/Faturamento";
      * Na tela do processo de Liberar Período, não será possível incluir informações de Deduções e Retenções;
      * O novo período (Período de Reajuste) não poderá ser excluído, pois apenas o processo de Cancelar Último Reajuste de Item Associado poderá realizar essa tarefa;
      * Todos os períodos liberados posteriores à data de reajuste também deverão ser considerados, pois o valor do item será reajustado, e estes, devem considerar o recálculo para a criação do período de reajuste, portanto pode ocorrer de um período principal ter mais de um período de reajuste, conforme exemplo:
      * No caso de existirem períodos complementares de reajuste já liberados, o cálculo para o valor que estará presente no próximo período de reajuste deverá considerar esse período liberado:
      * No período de reajuste, deverá conter todos os rateios (produto, centro de custo e estado e município) realizados para os itens dos períodos de origem. O cálculo do rateio, levará em conta a proporção do valor para definir o novo percentual, pois os mesmos devem fechar em 100%:
      * O cálculo do valor do contrato deverá considerar esse novo tipo de período, porém desconsiderando a quantidade zero (0) do mesmo, apenas o valor. O valor medido do período de reajuste considera as medições realizadas acima de 100% do item contratado, porém, no cálculo do projeto o mesmo valor não deverá ser considerado, assim como ocorre com as medições comuns, para o período de reajuste deverá ser descontado o valor que ultrapassa os 100% do item contratado.

**4 - Cancelamento de Reajustes** 

O processo de Cancelar Último Reajuste de Item Associado deverá ser alterado para permitir o cancelamento de reajustes para períodos medidos ou liberados, obedecendo às seguintes regras:

* + O cancelamento do reajuste do item somente será processado se não existir nenhum período principal liberado com a data de liberação maior ou igual à data do reajuste onde o item está presente;
  + O cancelamento do reajuste do item somente será processado se não existir nenhum período complementar de reajuste liberado onde o item está presente;
  + Período Medido: Ao cancelar o reajuste realizado para o item, as medições dos períodos reajustados deverão ser recalculadas pois o valor do item será alterado para o valor anterior ao reajuste. O recálculo deverá ser realizado, também, para todos os períodos medidos que tem a data maior que a data de reajuste. Períodos de estorno não deverão ser considerados pois o mesmo não deve ser recalculado pelo fato de ser um valor predefinido que não deveria ser ajustado;
  + Período Principal Liberado: Ao cancelar o reajuste realizado para o item, a medição do item no período de reajuste medido deverá ser excluída e caso não exista mais nenhuma medição no período, o mesmo também deverá ser excluído.

**Importante:** 

* **O processo de Realinhar Itens Associado ao Contrato não estará disponível caso o contrato já tenha reajustes realizados;**
* **Alterações e exclusões de itens associados e também de aditivos não serão permitidos se os mesmos tiverem reajustes realizados.**

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Contratos | [Alteração] | Controle -> Contrato -> Contratos | - |

### Protótipo de Tela

**Protótipo 01**

**Protótipo 02**

**Protótipo 03**

****Protótipo 04****

****************Protótipo 05****************

********Protótipo 06********
