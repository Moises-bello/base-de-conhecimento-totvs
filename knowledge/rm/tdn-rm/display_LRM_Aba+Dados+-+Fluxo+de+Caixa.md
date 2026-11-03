---
content_hash: 637f908d8c70621f4fd9d1d52c3eff758a0a3eae6d5e71086d5008f2d715bc52
fetched_at: '2026-06-29T00:09:17.704257+00:00'
page_id: '421388620'
product: rm
source: tdn-rm
title: Aba Dados - Fluxo de Caixa
type: documentation
url: https://tdn.totvs.com/display/LRM/Aba+Dados+-+Fluxo+de+Caixa
version: 8
---

---

Permite a utilização do Fluxo de Caixa Projetado. Nessa aba será apresentado os dados do lançamento: Coligada, IDLAN, Valor, valor baixado/compensado, data de vencimento, data baixa/compensação, histórico, nome/razão social e nome fantasia do cliente/fornecedor.

É possível simular a inclusão/exclusão e baixa/cancelamento de baixa/compensação de lançamento ou extratos de caixa a fim de visualizar uma projeção dos valores de entrada e saída da empresa a curto, médio e longo prazo. Toda operação efetuada por essa aba não altera nada no sistema. São apenas simulações que, ao fechar o Fluxo de Caixa deixam de existir.

Simular Inclusão

Permite a inclusão de um lançamento financeiro em um determinado período. Deve-se selecionar uma célula da planilha que esteja vazia dentro de algum período e informar os seguintes campos:

* Data;
* Valor;
* Tipo = (Em Aberto, Baixado).

Não é permitido simular a baixa de um lançamento incluído por simulação, para que o mesmo seja baixado, deve-se incluí-lo com o tipo = baixado.

Simula o Cancelamento de lançamento

Permite que um lançamento seja cancelado através de simulação. Deve-se selecionar a célula na planilha que habilitará o lançamento na visão inferior do Fluxo de Caixa, depois selecionar o lançamento e executar a operação de cancelamento de lançamento. Somente lançamento incluídos via simulação podem ser cancelados por simulação.

Simular Baixa

Permite que seja simulada a baixa de lançamentos exibidos no Fluxo de Caixa, deve-se informar a data em que o lançamento será baixado. Não é permitido a baixa de lançamentos com data inferior a data de inclusão do lançamento.

Cancelar simulação de baixa

Cancela a simulação da baixa de um lançamento. Não é permitido cancelar a baixa de lançamentos que não tiveram sua baixa simulada.

---
