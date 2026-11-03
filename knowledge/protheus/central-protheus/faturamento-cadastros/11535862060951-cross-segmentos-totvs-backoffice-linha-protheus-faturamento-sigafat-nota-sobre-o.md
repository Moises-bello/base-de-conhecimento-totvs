---
article_id: 11535862060951
category: Faturamento - Cadastros
content_hash: 507239f09e35a299558e6fbcae033f9a29e6a7704012b1a5b9004f0d7f392065
fetched_at: '2026-06-28T22:38:36.895187+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos – TOTVS Backoffice (Linha Protheus) – Faturamento (SIGAFAT)
  – Nota sobre o campo EC_IPI
type: support-article
updated_at: '2024-05-27T21:25:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11535862060951-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Nota-sobre-o-campo-EC-IPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:00:30 min**

**Dúvida**

Qual a Nota sobre o campo EC\_IPI?

**Ambiente**Cross Segmentos – TOTVS Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões.

**Solução**

Nesse campo é definido como será distribuído o valor do imposto IPI no pedido de venda em que a condição de pagamento estiver colocada.

**1 – EC\_IPI = ‘N – Normal’**

Ação 1: Montar o pedido de venda:

F4\_DUPLIC = ‘S – Sim’ (TES do pedido de venda)

E4\_TIPO = B

E4\_COND = 0 (Em condições de pagamento do Tipo B a regra é colocada no item, nos campos EC\_COND mas é obrigatório colocar algum valor no campo da regra do cabeçalho para salvar o cadastro).

EC\_TIPO = 1 (Condição de pagamento colocada tipo 1)

EC\_COND = 30,60,90 (3 parcelas)

EC\_RATEIO = 100

C6\_VALOR = 100 (Total do pedido de venda)

IPI pela planilha financeira: 2,50

Total da nota pela planilha financeira: 102,50

Ação 2: Faturar o pedido de venda:

D2\_TOTAL = 100

D2\_VALIPI = 2,50

Ação 3: Visualizar os títulos gerados:

Linha 1:

            Vencimento 30 dias após a emissão.

E1\_PARCELA = A

E1\_NUM = 000001

E1\_TIPO = NF

E1\_SALDO = 34,17 (Dividiu o total + IPI pelas 3 parcelas igualmente)

Linha 2:

            Vencimento 60 dias após a emissão.

E1\_PARCELA = B

E1\_NUM = 000001

E1\_TIPO = NF

E1\_SALDO = 34,17 (Dividiu o total + IPI pelas 3 parcelas igualmente)

Linha 3:

            Vencimento 90 dias após a emissão.

E1\_PARCELA = C

E1\_NUM = 000001

E1\_TIPO = NF

E1\_SALDO = 34,16 (Dividiu o total + IPI pelas 3 parcelas igualmente)

**2 – EC\_IPI = ‘J – Junta’**

Ação 1: Montar o pedido de venda:

F4\_DUPLIC = ‘S – Sim’ (TES do pedido de venda)

E4\_TIPO = B

E4\_COND = 0 (Em condições de pagamento do Tipo B a regra é colocada no item, nos campos EC\_COND mas é obrigatório colocar algum valor no campo da regra do cabeçalho para salvar o cadastro).

EC\_TIPO = 1 (Condição de pagamento colocada tipo 1)

EC\_COND = 30,60,90 (3 parcelas)

EC\_RATEIO = 100

C6\_VALOR = 100 (Total do pedido de venda)

IPI pela planilha financeira: 2,50

Total da nota pela planilha financeira: 102,50

Ação 2: Faturar o pedido de venda:

D2\_TOTAL = 100

D2\_VALIPI = 2,50

Ação 3: Visualizar os títulos gerados:

Linha 1:

            Vencimento 30 dias após a emissão.

E1\_PARCELA = A

E1\_NUM = 000002

E1\_TIPO = NF

E1\_VALOR = 35,83 (Dividiu o total pelas 3 parcelas e aplicou o IPI somente na primeira parcela)

Linha 2:

            Vencimento 60 dias após a emissão.

E1\_PARCELA = B

E1\_NUM = 000002

E1\_TIPO = NF

E1\_ VALOR = 33,33

Linha 3:

            Vencimento 90 dias após a emissão.

E1\_PARCELA = C

E1\_NUM = 000002

E1\_ TIPO = NF

E1\_VALOR = 33,34

**3 – EC\_IPI = ‘S – Separa’**

Ação 1: Montar o pedido de venda:

F4\_DUPLIC = ‘S – Sim’ (TES do pedido de venda)

E4\_TIPO = B

E4\_COND = 0 (Em condições de pagamento do Tipo B a regra é colocada no item, nos campos EC\_COND mas é obrigatório colocar algum valor no campo da regra do cabeçalho para salvar o cadastro).

EC\_TIPO = 1 (Condição de pagamento colocada tipo 1)

EC\_COND = 30,60,90 (3 parcelas)

EC\_RATEIO = 100

C6\_VALOR = 100 (Total do pedido de venda)

IPI pela planilha financeira: 2,50

Total da nota pela planilha financeira: 102,50

Ação 2: Faturar o pedido de venda:

D2\_TOTAL = 100

D2\_VALIPI = 2,50

Ação 3: Visualizar os títulos gerados:

Linha 1:

            Vencimento 30 dias após a emissão.

E1\_PARCELA = A

E1\_NUM = 000003

E1\_TIPO = NF

E1\_VALOR = 2,50 (Separou a primeira parcela da condição de pagamento exclusivamente para pagamento do imposto)

Linha 2:

            Vencimento 60 dias após a emissão.

E1\_PARCELA = B

E1\_NUM = 000003

E1\_TIPO = NF

E1\_ VALOR = 50 (Dividiu o total do título pelas duas parcelas restantes (Parcelas A e B {100/2=50})

Linha 3:

            Vencimento 90 dias após a emissão.

E1\_PARCELA = C

E1\_NUM = 000003

E1\_ TIPO = NF

E1\_VALOR = 50 (Dividiu o total do título pelas duas parcelas restantes (Parcelas A e B {100/2=50})

**OBS 1:** Quando a opção é EC\_IPI = ‘S – Separa’, deve-se incluir uma condição de pagamento a mais para o tratamento dos impostos.

**OBS 2:** Dúvidas nas configurações de geração de impostos, contate a Equipe Fiscal.

**Saiba mais sobre as condições de pagamento:**

* **TDN:** <https://tdn.totvs.com/pages/viewpage.action?pageId=240310845>
* **KCS:** [Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Condições de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiYm7bSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNzQ2ODMxMi1Dcm9zcy1TZWdtZW50by1UT1RWUy1CYWNrb2ZmaWNlLUxpbmhhLVByb3RoZXVzLVNJR0FGQVQtQ29uZGklQzMlQTclQzMlQjVlcy1kZS1QYWdhbWVudG8GOwhUOg5zZWFyY2hfaWRJIikxMmE5MjAxYi1hNDYyLTRkYTYtYWZmNy1mN2ZhYTY0MjQ3YmUGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIh1jb25kacOnw7VlcyBkZSBwYWdhbWVudG8GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--8f786711cbd49788c1821a37316cd02b45236625) (<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017468312-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Condi%C3%A7%C3%B5es-de-Pagamento>)
