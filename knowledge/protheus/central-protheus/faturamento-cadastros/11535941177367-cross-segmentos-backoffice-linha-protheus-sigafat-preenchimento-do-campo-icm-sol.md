---
article_id: 11535941177367
category: Faturamento - Cadastros
content_hash: 13a906e17cf20580c3911032324d5e9d4cd90b88abb0b93acbe2d99f3c659a82
fetched_at: '2026-06-28T22:38:36.703327+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Preenchimento do
  campo "ICM Solid." (E4_SOLID)
type: support-article
updated_at: '2023-01-25T19:58:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11535941177367-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Preenchimento-do-campo-ICM-Solid-E4-SOLID
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:30 min**

**Dúvida**

Como preencher o campo "ICM Solid." (E4\_SOLID) e para que este campo serve?

**Ambiente**Cross Segmentos – TOTVS Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões  
**Solução**

Nesse campo é definido como será distribuído o valor do imposto IPI no pedido de venda em que a condição de pagamento estiver colocada.

Quando esse campo não é alimentado, assume-se que é "ICM Solid.)" (E4\_SOLID) = ‘N – Normal’.

A TES do pedido de venda deve gerar regsitros financeiros [F4\_DUPLIC = ‘S – Sim’ (TES do pedido de venda)]

**1 – E4\_SOLID = ‘N – Normal’**

Ação 1: Montar o pedido de venda:

"Tipo" E4\_TIPO = 1 e "Cond. Pagto" E4\_COND = 30,60,90 (3 parcelas)

"Total" C6\_VALOR = 100 (Total do pedido de venda)

ICMS pela planilha financeira: 2,50

Total da nota pela planilha financeira: 102,50

Ação 2: Faturar o pedido de venda:

"Vlr.Total" D2\_TOTAL = 100

"Vlr.ICMS" D2\_VALICM = 2,50

Ação 3: Visualizar os títulos gerados:

Linha 1: Vencimento 30 dias após a emissão.

"Parcela" E1\_PARCELA = A

"No. Titulo" E1\_NUM = 000001

"Saldo" E1\_SALDO = 34,17 (Dividiu o total + ICMS pelas 3 parcelas igualmente)

Linha 2: Vencimento 60 dias após a emissão.

"Parcela" E1\_PARCELA = B

"No. Titulo" E1\_NUM = 000001

"Saldo" E1\_SALDO = 34,17 (Dividiu o total + ICMS pelas 3 parcelas igualmente)

Linha 3: Vencimento 90 dias após a emissão.

"Parcela" E1\_PARCELA = C

"No. Titulo" E1\_NUM = 000001

"Saldo" E1\_SALDO = 34,16 (Dividiu o total + ICMS pelas 3 parcelas igualmente)

**2 – E4\_SOLID = ‘J – Junta’**

Ação 1: Montar o pedido de venda:

"Tipo" E4\_TIPO = 1 e "Cond. Pagto" E4\_COND = 30,60,90 (3 parcelas)

"Total" C6\_VALOR = 100 (Total do pedido de venda)

ICMS pela planilha financeira: 2,50

Total da nota pela planilha financeira: 102,50

Ação 2: Faturar o pedido de venda:

"Vlr.Total" D2\_TOTAL = 100

"Vlr.ICMS" D2\_VALICM = 2,50

Ação 3: Visualizar os títulos gerados:

Linha 1: Vencimento 30 dias após a emissão.

"Parcela" E1\_PARCELA = A

"No. Titulo" E1\_NUM = 000002

"Saldo" E1\_VALOR = 35,83 (Dividiu o total pelas 3 parcelas e aplicou o ICMS somente na primeira parcela)

Linha 2: Vencimento 60 dias após a emissão.

"Parcela" E1\_PARCELA = B

"No. Titulo" E1\_NUM = 000002

"Saldo" E1\_ VALOR = 33,33

Linha 3: Vencimento 90 dias após a emissão.

"Parcela" E1\_PARCELA = C

"No. Titulo" E1\_NUM = 000002

"Saldo" E1\_VALOR = 33,34

**3 – E4\_SOLID = ‘S – Separa’**

Ação 1: Montar o pedido de venda:

"Tipo" E4\_TIPO = 1 e "Cond. Pagto" E4\_COND = 30,60,90 (3 parcelas)

"Total" C6\_VALOR = 100 (Total do pedido de venda)

ICMS pela planilha financeira: 2,50

Total da nota pela planilha financeira: 102,50

Ação 2: Faturar o pedido de venda:

"Vlr.Total" D2\_TOTAL = 100

"Vlr.ICMS"D2\_VALICM = 2,50

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

**OBS 1:** Quando a opção é E4\_SOLID = ‘S – Separa’, deve-se incluir uma condição de pagamento a mais para o tratamento dos impostos, pois a primeira parcela é separada exclusivamente para receber o valor do imposto isolado.

**OBS 2:** Dúvidas nas configurações de geração de impostos, contate a Equipe Fiscal.

**Saiba mais sobre as condições de pagamento:**

* **TDN:** [Condições de Pagamento](https://tdn.totvs.com/pages/viewpage.action?pageId=240310845)
* **KCS:** [Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Condições de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiYm7bSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNzQ2ODMxMi1Dcm9zcy1TZWdtZW50by1UT1RWUy1CYWNrb2ZmaWNlLUxpbmhhLVByb3RoZXVzLVNJR0FGQVQtQ29uZGklQzMlQTclQzMlQjVlcy1kZS1QYWdhbWVudG8GOwhUOg5zZWFyY2hfaWRJIikxMmE5MjAxYi1hNDYyLTRkYTYtYWZmNy1mN2ZhYTY0MjQ3YmUGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIh1jb25kacOnw7VlcyBkZSBwYWdhbWVudG8GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--8f786711cbd49788c1821a37316cd02b45236625) (<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017468312-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Condi%C3%A7%C3%B5es-de-Pagamento>)
