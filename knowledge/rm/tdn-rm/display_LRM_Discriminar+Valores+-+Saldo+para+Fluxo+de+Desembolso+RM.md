---
content_hash: ab853c38462debb51e23b8894c5fa50e2f43e26ac9ed40cc81f76160cbe3f8c2
fetched_at: '2026-06-29T00:10:51.302651+00:00'
page_id: '566461423'
product: rm
source: tdn-rm
title: Discriminar Valores - Saldo para Fluxo de Desembolso RM
type: documentation
url: https://tdn.totvs.com/display/LRM/Discriminar+Valores+-+Saldo+para+Fluxo+de+Desembolso+RM
version: 43
---

Ao habilitar essa opção o sistema passa a exibir cada etapa realizada no processo de Saldo de Fluxo de Desembolso.

Ao executar Linha Base:

Etapa: Histograma calculado

Nesta etapa o sistema exibirá dados do histograma utilizado para o cálculo de fluxo de caixa.

Apresentará informações derivadas do histograma, que são cruciais para calcular e entender o fluxo de caixa permitindo uma análise mais detalhada e uma gestão financeira mais eficaz.

**Id Período:** Identifica o período planejamos conforme cronograma.

**Tipo da Tarefa:** Informa o tipo da tarefa sé é despesa ou receita.

**Código do Insumo**: Informa o código do insumo

**Descrição Insumo:** Informa a descrição do insumo.

**Unidade Insumo:** Informa a unidade do insumo.

**Código Tarefa:** Informa o código da tarefa.

**Nome Tarefa:** Informa o nome da tarefa.

**Descrição Tarefa:** Informa a descrição da tarefa.

**Quantidade Planejada:** Informa a quantidade planejada da tarefa.

**Valor Unitário:** Informa o valor unitário da tarefa.

**Valor Total:** Informa o valor total da tarefa.

**Data Desembolso:** Informa a data de desembolso conforme o cronograma.

Etapa: Calculo do cronograma desembolso

Nessa etapa exibirá as informações de cálculo de cronograma de desembolso.

Baseado nas informações do planejamento e orçamento exibirá as informações das tarefas e insumos planejados tal como suas quantidades , valores parcelas e condição de pagamento.

**Id Período:** Identifica o período planejamos conforme cronograma.

**Tipo da Tarefa:** Informa o tipo da tarefa sé é despesa ou receita.

**Código do Insumo**: Informa o código do insumo

**Descrição Insumo:** Informa a descrição do insumo.

**Unidade Insumo:** Informa a unidade do insumo.

**Código Tarefa:** Informa o código da tarefa.

**Nome Tarefa:** Informa o nome da tarefa.

**Descrição Tarefa:** Informa a descrição da tarefa.

**Quantidade Planejada:** Informa a quantidade planejada da tarefa.

**Valor Unitário:** Informa o valor unitário da tarefa.

**Valor Total:** Informa o valor total da tarefa.

**Data Desembolso:** Informa a data de desembolso conforme o cronograma.

**Quantidade Desembolso:** Informa a quantidade a ser desembolsada conforme o cronograma.

**Valor Desembolso:** Informa o valor a ser desembolsado conforme cronograma.

**Parcela:** Informa a quantidade de parcelas conforme condição de pagamento definida.

**Origem Condição Pagamento:** Informa a origem da condição de pagamento se é no insumo ou do projeto.

**Código Condição de Pagamento:** Informa o código da condição de pagamento.

**É importante destacar que os itens que foram zerados pelo consumo nas etapas anteriores não serão utilizados nesse cálculo.**

**Prévia de Lançamentos Financeiros**

Nessa etapa será exibida uma prévia dos lançamentos que serão criados no módulo financeiro.

**Tipo da Tarefa :** Informa o tipo da tarefa.

**Origem Natureza:** Informa a origem da natureza financeira informada.

**Col Natureza:** Coligada da natureza.

**Cod Natureza:** Informa o código da natureza financeira.

**Origem Centro de Custos:** Informa a origem do centro de custo informado.

**Cód. Centro Custo:** Informa o código do centro de custo informado.

**Valor Previsto:** Informa o valor previsto para os lançamentos conforme a condição de pagamento e cronograma definido.

No final da execução da linha base exibirá o log do processo completo mostrando:

**Valor inicial:** Valor inicial conforme o histograma.

**Valor adicionado previsto em contratos:** O valor informado no cadastro do período caso seja informado é considerado.

**Valor do Desembolso:** Valor total do desembolso.

No financeiro é possível verificar se a linha base foi gerada conforme esperado.

Será possível visualizar as datas de emissão , vencimento e da previsão da baixa, numero do documento valor da baixa dentre outras informações pertinentes.

Ao executar saldo...

Etapa: Histograma calculado

Nesta etapa o sistema exibirá dados do histograma utilizado para o cálculo de fluxo de caixa.

Apresentará informações derivadas do histograma, que são cruciais para calcular e entender o fluxo de caixa permitindo uma análise mais detalhada e uma gestão financeira mais eficaz.

**Id Período:** Identifica o período planejamos conforme cronograma.

**Tipo da Tarefa:** Informa o tipo da tarefa sé é despesa ou receita.

**Código do Insumo**: Informa o código do insumo

**Descrição Insumo:** Informa a descrição do insumo.

**Unidade Insumo:** Informa a unidade do insumo.

**Código Tarefa:** Informa o código da tarefa.

**Nome Tarefa:** Informa o nome da tarefa.

**Descrição Tarefa:** Informa a descrição da tarefa.

**Quantidade Planejada:** Informa a quantidade planejada da tarefa.

**Valor Unitário:** Informa o valor unitário da tarefa.

**Valor Total:** Informa o valor total da tarefa.

**Data Desembolso:** Informa a data de desembolso conforme o cronograma.

Etapa: Calculo de consumo de contratos

Nesta etapa o sistema exibirá os dados do histograma utilizado para o calculo de fluxo de caixa e o consumo de contratos.

Nessa visão o sistema considerará o valor medido e previsto caso tenha nos períodos do contrato.

Levará em consideração no calculo (valores medidos e previsto que ainda não estão liberados para o Suprimento e Faturamento)

**Importante :**

O valor associado  no contrato só aparecerá nas etapas discriminadas se o contrato tiver períodos e estiver calculado.

Ao realizar contratação e informar valor previsto no período do contrato é importante destacar que sempre é necessário calcular o contrato para que esse valor seja considerado no calculo do Saldo de fluxo de desembolso.

**Id Período:** Identificador do período da tarefa.

**Tipo da Tarefa:** Tipo da tarefa , se e de despesa ou de receita.

**Código insumo:** Código do insumo associado a tarefa.

**Descrição Insumo:** Descrição do insumo associado a tarefa.

**Código Tarefa:** Código da tarefa**.**

**Nome Tarefa:** Nome da tarefa.

**Descrição Tarefa:** Descrição da tarefa

**Quantidade Planejada:** Quantidade planejada da tarefa.

**Valor Unitário:** Valor unitário do insumo associado a tarefa.

**Valor Total:** Valor total da tarefa.

**Data Desembolso:** Data de desembolso.

**Quantidade Associado Contrato:** Quantidade associada ao contrato na medição.

**Associado Contrato:** Quantidade consumida no contrato.

**Percentual Contrato:** Percentual consumido no contrato.

**Quantidade Desembolso:** Quantidade disponível para desembolso.

**Valor Desembolso:** Valor disponível para desembolso.

**Contratos:** Contrato que a tarefa esta vinculada.

**Observações:**

Etapa: Calculo de consumo de Pedidos

Na etapa cálculo de consumo de pedidos são abatimentos de quantidade de ordem de compra ou venda que estejam faturados.

**Serão considerados consumos dos pedidos que geraram Ordem de Compra a ser Faturada no TOTVS Gestão de Estoque, Compras e Faturamento, assim o saldo de fluxo de desembolso realizará o abatimento dos itens pedidos a partir dos produtos que constam nessas movimentações, para através deles chegar aos seus respectivos insumos e tarefas para abatimento. Somente será exibido o consumo do pedido na geração da ordem de compra desde que esteja devidamente configurado conforme os passos abaixo.**

**Nessa etapa são apresentadas as informações do Cálculo de Consumo de Contratos como:**

* **Quantidade Associada a Contrato** (Quantidade associada ao contrato na medição)
* **Associado a contrato** (Quantidade consumida no contrato)

Configurações necessárias para o tipo de movimento de destino ao movimento de origem do TCOP:  
  
1 - Estar configurado como Fatura.

2 - Estar configurado para usa rateio de centro de custo e consequentemente a formula de valor de rateio.

3 - Utiliza rateio de Projeto/Tarefa.

Estando devidamente configurado, a tela de consumo de pedidos irá apresentar os dados a partir dos pedidos criados:

Foi disponibilizado o botão de rastreamento de movimentos , que possibilita ao usuário verificar toda a árvore de movimentos criados a partir do movimento gerado pelo TCOP. Ao selecionar o pedido e clicar , irá apresentar a seguinte tela:

Para ver a rastreabilidade, basta selecionar o movimento e clicar em :

Etapa: Calculo de consumo de Apropriação

Consumo de apropriações considerando abatimentos de quantidade originadas através da Apropriação de Serviços/Insumo.

**Nessa etapa são apresentadas as seguintes informações de etapas anteriores:**

* **Cálculo de Consumo de Contratos**
  + **Quantidade Associada** (Quantidade associada ao contrato na medição)
  + **Contrato e Associado a contrato** (Quantidade consumida no contrato)
* **Cálculo de Consumo de Pedidos**
  + **Quantidade Consumido Pedido** (Quantidade consumida do pedido)
  + **Consumo Pedido** (O quanto o pedido foi consumido)
Etapa: Calculo de cronograma desembolso

Os itens que foram zerados pelos consumos não serão utilizados neste calculo.

Etapa: Cronograma desembolso considerando previsão em períodos de contratos

São considerados períodos de contratos com previsão informada e não integrados com Suprimentos / Faturamento.

**Nessa etapa são apresentadas informações tanto do Histograma quanto de itens Associados em Contratos. Para validar, a coluna Origem faz a distinção das previsões.**

Visão da previsão de contratos no cronograma desembolso.

No final exibirá o log do processo

[05/12/2018 18:13:52] - Iniciando transação...  
[05/12/2018 18:13:52] - Etapa 1 de 19 - Calculando o projeto......  
[05/12/2018 18:14:00] - Etapa 2 de 19 - Calculando curva ABC de insumos...  
[05/12/2018 18:14:00] - Etapa 3 de 19 - Calculando histograma...  
[05/12/2018 18:14:02] - Etapa 4 de 19 - Obtendo quantidades de insumos contratadas...  
[05/12/2018 18:14:02] - Etapa 5 de 19 - Abatendo quantidades contratadas do histograma...  
[05/12/2018 18:14:04] - Etapa 6 de 19 - Abatendo quantidades dos insumos pedidos do histograma...  
[05/12/2018 18:14:09] - Etapa 7 de 19 - Abatendo apropriações diretas do histograma...  
[05/12/2018 18:14:09] - Etapa 8 de 19 - Carregando cronograma de desembolso...  
[05/12/2018 18:14:10] - Etapa 9 de 19 - Adicionando valores previstos em contratos ao cronograma de desembolso...  
[05/12/2018 18:14:10] - Etapa 10 de 19 - Buscando natureza de produto, insumo, grupo de custo e tarefa...  
[05/12/2018 18:14:10] - Etapa 11 de 19 - Buscando tarefas associadas ao contrato...  
[05/12/2018 18:14:10] - Etapa 12 de 19 - Apagando lançamentos anteriores do tipo de documento: 17 - DESPACHO DE TRANSPORTE...  
[05/12/2018 18:14:11] - Etapa 13 de 19 - Salvando dados...  
[05/12/2018 18:14:11] - Etapa 14 de 19 - Gerando lançamentos financeiros...  
[05/12/2018 18:14:11] - Etapa 15 de 19 - Montando estrutura para lançamentos financeiros......  
[05/12/2018 18:14:11] - Etapa 16 de 19 - Enviando lançamentos ao Financeiro......  
[05/12/2018 18:14:22] - Etapa 17 de 19 - Atualizando status de envio dos lançamentos......  
[05/12/2018 18:14:22] - Processo executado com sucesso!  
[05/12/2018 18:14:22] - Duração aproximada da execução do processo: 00:00:31

**Exportação**

Em cada tela de etapa, é possível exportar os resultados nos formatos listados na imagem abaixo. Basta clicar na opção desejada que o sistema irá perguntar se você deseja fazer a exportação pelo disco da sua máquina ou através do SharePoint.
