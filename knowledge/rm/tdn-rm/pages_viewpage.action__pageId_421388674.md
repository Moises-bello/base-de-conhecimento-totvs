---
content_hash: 3b570375c1c533225e05a98108805ddfa380a6355301677d18f6199872dac4f0
fetched_at: '2026-06-29T00:09:18.122411+00:00'
page_id: '421388674'
product: rm
source: tdn-rm
title: Nota de Crédito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388674
version: 4
---

É normalmente utilizada em operações sem envolvimento de dinheiro, ou seja, a quitação de um Lançamento Financeiro ficará vinculada a um crédito obtido ou concedido. Poderá haver movimentação Financeira quando houver diferenças entre os valores.

**Exemplo**

A empresa  Comercial Fronteira presta serviços à empresa TOTVS. Como pagamento pelo serviço, a TOTVS oferece um crédito em produtos que comercializa à empresa Comercial Fronteira.

**Pré-requisito**

Tipo de Documento classificado como "sem classificação" . Tipo de documento classificado como "Nota de Crédito" . Cliente/Fornecedor com classificação "ambos".

**Procedimento**

1. (De acordo com o Exemplo) Inclusão de um Lançamento financeiro a pagar correspondente à prestação de serviços. Este Lançamento poderá ter incidência de Tributos ou não e poderá inclusive, ser gerado através de outros segmentos, como por exemplo o TOTVS Gestão de Compras, Estoque e Faturamento.
2. Inclusão de um Lançamento Financeiro correspondente ao crédito concedido. Nesse caso, deverá ser "a receber" e com tipo de documento classificado como "Nota de Crédito".
3. Estabelecer o vínculo entre os dois Lançamentos. Poderá se realizado durante o processo de baixa ou antes, através da visão de Lançamento, Processos / Vínculos.
4. Baixar o Lançamento, que poderá ser tanto o Lançamento o comum, quanto o Lançamento correspondente ao Crédito.

**Efeitos**

Se o valor do crédito for igual ao valor da(s) Nota(s) de prestação de serviços, a baixa será realizada com valor zerado e não será gerado registro no extrato de caixa.

Se o valor do Crédito for menor do que o valor da(s) Nota(s) de prestação de serviços, a baixa será realizada pela diferença. Nesse caso, haverá registro no extrato de Caixa correspondente a diferença efetivamente paga.

Se o valor do Crédito for maior do que o valor da(s) Nota(s) de prestação de serviços, a baixa será realizada com valor zero (não gerará extrato) e restante do Crédito poderá ser utilizado em outra operação. Nesse caso, o Lançamento correspondente ao Crédito ficará com status de "Baixado parcialmente". Esse restante "vinculável" poderá ser utilizado numa próxima operação ou poderá ser baixado, gerando um extrato de caixa, que corresponde a restituição ao Fornecedor, ou seja, o Fornecedor optou por receber o valor correspondente ao Crédito ao invés de utilizá-lo numa próxima operação.

**Observações**

* Só é possível vincular Nota de Crédito a Lançamentos que possuam o tipo Pag/Rec ("Pagar"/"Receber") oposto a ele.
* Ao baixar a Nota de Crédito é possível vincular vários Lançamentos comuns e vice-versa.
* Não será permitido a geração de Borderô de pagamento para lançamentos com valor líquido igual a 0 (zero), com data de referencia a sua data de vencimento.
* É possível vincular o lançamento pertinente a nota de crédito com outro cujo o Cliente/Fornecedor seja diferente, desde que o parâmetro "Não Permite vínculo de Lançamentos entre Cliente/Fornecedores Diferentes' esteja desmarcado. Para visualizar este parâmetro, acesse o menu Ambiente | Parâmetros | TOTVS Gestão Financeira | Avançar | Contas a Receber | Avançar | Etapa Baixa 2/6.

**Dica**

O sistema permite que um Lançamento Financeiro seja vinculado a Adiantamento, Devolução e Nota de Crédito, simultaneamente.  Nesse caso, o valor da baixa será o liquido, considerando cada um desses processos.  
Tomemos como exemplo um lançamento financeiro no valor de 10.500,00 vinculado a:

* Devoluções no valor de R$2500,00
* Nota de Crédito no valor de R$1000,00
* Crédito de Adiantamento no valor de R$4000,00

**Efeitos**

* O valor baixado será R$3.000,00 .
* Todos os Lançamentos ficarão com status de "Baixado" . Será gravado um registro no extrato de caixa.

Para cancelar esta operação, basta cancelar a baixa do Lançamento comum. O vinculo continuará estabelecido e para cancelar, acesse Processos/Vínculos.
