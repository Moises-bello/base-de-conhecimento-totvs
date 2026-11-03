---
article_id: 9245346715159
category: Faturamento - Cadastros
content_hash: 26ae9de7eecc2dc27bdf36e86774b1e99605903467852a995015d0fc18beb46f
fetched_at: '2026-06-28T22:38:36.711522+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Preenchimento do
  campo "IPI (N/J/S)" (E4_IPI)
type: support-article
updated_at: '2025-05-21T19:35:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9245346715159-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Preenchimento-do-campo-IPI-N-J-S-E4-IPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:30 min**

**Dúvida**

Como preencher o campo "IPI (N/J/S)" (E4\_IPI) e para que este campo serve?

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

Nesse campo é definido como será distribuído o valor do imposto IPI no pedido de venda em que a condição de pagamento estiver colocada.

Quando esse campo não é alimentado, assume-se que é "IPI (N/J/S)" (E4\_IPI) = ‘N – Normal’.

A TES do pedido de venda deve gerar regsitros financeiros [F4\_DUPLIC = ‘S – Sim’ (TES do pedido de venda)]

* **1 – "IPI (N/J/S)" (E4\_IPI) = ‘N – Normal’**

Ação 1: Montar o pedido de venda:

"Tipo" E4\_TIPO = 1 (Condição de pagamento colocada tipo 1)

"Cond. Pagto" E4\_COND = 30,60,90 (3 parcelas)

"Total" C6\_VALOR = 100 (Total do pedido de venda)

IPI pela planilha financeira: 2,50

Total da nota pela planilha financeira: 102,50 (Valor total dos itens + Imposto)

Ação 2: Faturar o pedido de venda:

"Vlr.Total" D2\_TOTAL = 100

"Vlr.IPI" D2\_VALIPI = 2,50

Ação 3: Visualizar os títulos gerados:

Parcela 1: Vencimento 30 dias após a emissão.

"Parcela" E1\_PARCELA = A

"No. Titulo" E1\_NUM = 000001

"Saldo" E1\_SALDO = 34,17 (Dividiu o total + IPI pelas 3 parcelas igualmente)

Parcela 2: Vencimento 60 dias após a emissão.

"Parcela" E1\_PARCELA = B

"No. Titulo" E1\_NUM = 000001

"Saldo" E1\_SALDO = 34,17 (Dividiu o total + IPI pelas 3 parcelas igualmente)

Parcela 3: Vencimento 90 dias após a emissão.

"Parcela" E1\_PARCELA = C

"No. Titulo" E1\_NUM = 000001

"Saldo" E1\_SALDO = 34,16 (Dividiu o total + IPI pelas 3 parcelas igualmente)

* **2 – E4\_IPI = ‘J – Junta’**

Ação 1: Montar o pedido de venda:

"Tipo" E4\_TIPO = 1 (Condição de pagamento colocada tipo 1)

"Cond. Pagto" E4\_COND = 30,60,90 (3 parcelas)

"Total" C6\_VALOR = 100 (Total do pedido de venda)

IPI pela planilha financeira: 2,50

Total da nota pela planilha financeira: 102,50

Ação 2: Faturar o pedido de venda:

"Vlr.Total" D2\_TOTAL = 100

"Vlr.IPI" D2\_VALIPI = 2,50

Ação 3: Visualizar os títulos gerados:

Linha 1: Vencimento 30 dias após a emissão.

"Parcela" E1\_PARCELA = A

"No. Titulo" E1\_NUM = 000002

"Saldo" E1\_VALOR = 35,83 (Valor da parcela com o imposto concentrado na primeira parcela)

Linha 2: Vencimento 60 dias após a emissão.

"Parcela" E1\_PARCELA = B

"No. Titulo" E1\_NUM = 000002

"Saldo" E1\_ VALOR = 33,33 (Valor da parcela sem imposto)

Linha 3: Vencimento 90 dias após a emissão.

"Parcela" E1\_PARCELA = C

"No. Titulo" E1\_NUM = 000002

"Saldo" E1\_VALOR = 33,34 (Valor da parcela sem imposto)

* **3 – E4\_IPI = ‘S – Separa’**

Ação 1: Montar o pedido de venda:

"Tipo" E4\_TIPO = 1 (Condição de pagamento colocada tipo 1)

"Cond. Pagto" E4\_COND = 30,60,90 (3 parcelas)

"Total" C6\_VALOR = 100 (Total do pedido de venda)

IPI pela planilha financeira: 2,50

Total da nota pela planilha financeira: 102,50

Ação 2: Faturar o pedido de venda:

"Vlr.Total" D2\_TOTAL = 100

"Vlr.IPI" D2\_VALIPI = 2,50

Ação 3: Visualizar os títulos gerados:

Linha 1: Vencimento 30 dias após a emissão.

"Parcela" E1\_PARCELA = A

"No. Titulo" E1\_NUM = 000003

"Saldo" E1\_VALOR = 2,50 (Separou a primeira parcela da condição de pagamento exclusivamente para pagamento do imposto)

Linha 2: Vencimento 60 dias após a emissão.

"Parcela" E1\_PARCELA = B

"No. Titulo" E1\_NUM = 000003

"Saldo" E1\_ VALOR = 50 (Dividiu o total do título pelas duas parcelas restantes (Parcelas A e B {100/2=50})

Linha 3: Vencimento 90 dias após a emissão.

"Parcela" E1\_PARCELA = C

"No. Titulo" E1\_NUM = 000003

"Saldo" E1\_VALOR = 50 (Dividiu o total do título pelas duas parcelas restantes (Parcelas A e B {100/2=50})

**OBS 1:** Quando a opção é E4\_IPI = ‘S – Separa’, deve-se incluir uma condição de pagamento a mais para o tratamento dos impostos, pois a primeira parcela é separada exclusivamente para receber o valor do imposto isolado.

**OBS 2:** Dúvidas nas configurações de geração de impostos, contate a Equipe Fiscal.

**Saiba mais sobre as condições de pagamento:**

* **TDN:** [Condições de Pagamento - Completo](https://tdn.totvs.com/x/PdpSDg)
* **KCS:** [Condições de Pagamento - Específico](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiYm7bSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNzQ2ODMxMi1Dcm9zcy1TZWdtZW50by1UT1RWUy1CYWNrb2ZmaWNlLUxpbmhhLVByb3RoZXVzLVNJR0FGQVQtQ29uZGklQzMlQTclQzMlQjVlcy1kZS1QYWdhbWVudG8GOwhUOg5zZWFyY2hfaWRJIikxMmE5MjAxYi1hNDYyLTRkYTYtYWZmNy1mN2ZhYTY0MjQ3YmUGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIh1jb25kacOnw7VlcyBkZSBwYWdhbWVudG8GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--8f786711cbd49788c1821a37316cd02b45236625)
