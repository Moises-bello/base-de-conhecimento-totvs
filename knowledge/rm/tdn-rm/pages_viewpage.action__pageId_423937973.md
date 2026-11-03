---
content_hash: f894004330bcb48879f9f6a6fdd30acaa3782bc12a365e71c113ae7c22e8d3e5
fetched_at: '2026-06-29T00:09:24.629220+00:00'
page_id: '423937973'
product: rm
source: tdn-rm
title: Relatório de Agrupamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937973
version: 3
---

O objetivo do relatório de agrupamento por contas é possibilitar a emissão de toda movimentação patrimonial do período agrupada por conta contábil. A emissão do relatório se dará por um processo semelhante ao de emissão de ficha de imobilizado, se diferenciando apenas por não ser obrigatório o filtro de grupos de patrimônio e por possibilitar o agrupamento por faixa de contas contábeis.

**Regras para Emissão do Relatório**  
O novo modelo de contabilização do Gestão Patrimonial é baseado exclusivamente em eventos contábeis,  o sistema não controla as contas contábeis utilizadas em processos de contabilização. Portanto a TOTVS não se responsabiliza pelos dados cadastrados nos grupos de patrimônio, para possível emissão deste relatório. Como pré-requisitos para composição deste relatório deverão ser importados, no RM Reports, a estrutura do relatório de Agrupamento por Contas e Agrupamento por Contas por Filial. A estrutura do relatório de Agrupamento por Contas apresenta as informações de forma agrupada, mesmo que na parametrização do relatório sejam previamente definidas as filiais. Ou seja, o relatório não será com quebra por filial, apenas contas contábeis. Quando a estrutura utilizada é do relatório de Agrupamento por Contas por Filial, os totalizadores são apresentados respeitando as filiais e a faixa de contas parametrizada. Os relatórios exibirão apenas as informações contidas dentro do período de cálculo em aberto.

**Emissão do Relatório de Agrupamento**  
Inicialmente devem ser informados os meses e anos, respectivamente, iniciais e finais desejados para apuração (seleção do período), quais patrimônios serão envolvidos (os ativos e/ou inativos) e o cenário de cálculo correspondente a estes patrimônios. Caso seja necessário pode-se selecionar uma ou mais filiais. Desta forma somente as informações dos patrimônios existentes nas filiais selecionadas serão exibidas. A particularidade deste relatório está em permitir a seleção de uma faixa de contas contábeis. Existe também a possibilidade de selecionar uma opção entre o filtro por grupos de patrimônio (selecionado um ou mais grupos). O relatório agrupamento por contas permite totalizar cada conjunto de informações definidas, neste caso, como de aquisições ou ocorrências (baixas, acréscimos e transferências monetária).

A totalização pode ser realizada para cada um dos conjuntos acima ou para todos. Podem existir na base de dados patrimônios que possuem saldo, porém não tiveram movimentação no período a ser gerado o relatório. Desta forma, caso seja necessário exibir este tipo de informação é fundamental marcar a opção que permite imprimir dados dos grupos de patrimônio sem movimentação.

Também podem existir situações como a movimentação com valores zerados que está exemplificada abaixo:

O patrimônio foi inserido no sistema, consequentemente no relatório será apresentada uma aquisição. Porém por algum motivo o cálculo de depreciação não foi executado. Desta forma, ao marcar opção "Imprime movimentações com valores zerados" o sistema apresentará a aquisição do patrimônio e depreciação igual a 0,00. Ao solicitar a impressão de reavaliações/avaliações patrimoniais serão apresentadas no relatório de agrupamento por contas as reavaliações/avaliações realizadas de acordo com a parametrização pré-definida. Como obrigatoriedade, para composição do layout das informações, deve ser informado o relatório (agrupamento por contas ou agrupamento por contas por filial). Depois de realizada a correta parametrização, o relatório poderá ser executado, sendo que ao seu final serão apresentados o próprio relatório e o log contendo todas as informações referentes à execução do processo.

Veja Também

* Relatório Ficha de Imobilizado
