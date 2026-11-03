---
content_hash: 3a639c9e520be04d047f18ad6f8243a4ab46c355536b4dc28c4a9bf661b0d316
fetched_at: '2026-06-29T00:09:17.707333+00:00'
page_id: '421388621'
product: rm
source: tdn-rm
title: Aba Parâmetros - Fluxo de Caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388621
version: 10
---

Considera Período Anterior

Define se serão considerados lançamentos em aberto antes do período inicial.

Não Considerar Natureza com Valor Zerado

Ao executar o Fluxo de Caixa não serão listadas as naturezas que não tiverem valor.

Considerar lançamento com Conta Caixa Vazia

Considera os lançamentos que não tenham Conta/Caixa informada.

Listar Conta/Caixa Inativa

Permite definir se será listado as contas/caixa inativas para seleção no Fluxo de Caixa. Ao marcar ou desmarcar esta opção, a lista de Centro de Custo e Conta/Caixa deverá ser carregada novamente.

Considerar Centro de Custo por Natureza

Ao selecionar esta opção, é exibido no relatório o Centro de Custo de acordo com a Natureza, sendo exibido também os rateios.

O centro de custo será exibido no relatório com as informações: Coligada + Cod. Centro de Custo + Descrição, como no exemplo abaixo:

***Obs***: Quando este parâmetro é selecionado, a aba Dados ficará desabilitada.

Considerar baixa não compensada como previsão

Atualmente o fluxo de caixa considera a baixa sempre como valor realizado, com essa opção marcada é possível visualizar a baixa não compensada como valor previsto. Ao compensar o extrato de caixa o valor realizado ficará preenchido na data de compensação do extrato.

Considera apenas códigos sintéticos para Centros de Custos e Naturezas

Essa opção será default nos parâmetros, Com ela serão apresentadas somente os códigos sintéticos do Centro de Custo e Natureza Financeira.

Data Previsto

Será possível definir a data previsto de acordo com as opções disponibilizadas, data de vencimento ou a data de previsão de baixa do lançamento, para o cálculo do valor original ou líquido no relatório gerado.

* Data de vencimento **-** Definindo a data previsto como "Data de vencimento" o valor original ou líquido será calculado considerando a data de vencimento do lançamento, opção vem como default marcada.
* Data de Previsão de baixa **-** Definindo a data previsto como "Data de previsão de baixa" o valor original ou líquido será calculado considerando a data de previsão de baixa do lançamento.

Valor Previsto

Será possível definir o valor previsto do lançamento de acordo com as opções disponibilizadas no relatório para valor original e liquido. Caso a opção seja pelo valor líquido (data atual ou vencimento/previsão de baixa), o cálculo será feito aplicando-se o percentual do rateio ao valor.

* Valor original **-** Definindo valor previsto como "Valor Original", opção Default no qual leva em consideração o valor original do lançamento.
* Líquido na data atual **-** Definindo Valor previsto como "Líquido na Data Atual", é feito o cálculo do valor líquido levando em consideração a data do sistema.
* Líquido no vencimento / Previsão de baixa **-** Definindo Valor previsto como "Líquido no Vencimento / Previsão de baixa", é feito o cálculo do valor líquido levando em consideração a data de Vencimento / de previsão de baixa do lançamento, conforme for definido na Data Previsto.

Parâmetros default

As opções dos parâmetros da tela poderão ser carregadas como default, se a opção " Salvar os parâmetros utilizados" no menu de [Preferência de Usuários](http://tdn.totvs.com/x/8OAdGQ), estiver marcada.
