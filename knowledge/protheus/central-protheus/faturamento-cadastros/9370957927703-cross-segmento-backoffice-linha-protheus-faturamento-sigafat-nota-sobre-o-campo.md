---
article_id: 9370957927703
category: Faturamento - Cadastros
content_hash: 5185820c7333f0c7b1fb76e27793fc21d57e2ea109f317051042dc3c40a42142
fetched_at: '2026-06-28T22:38:36.505747+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Nota
  sobre o campo E4_ACRSFIN
type: support-article
updated_at: '2022-10-06T16:49:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9370957927703-Cross-Segmento-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Nota-sobre-o-campo-E4-ACRSFIN
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:30 min**

**Dúvida**

Qual a finalidade do campo E4\_ ACRSFIN?  
  
**Ambiente**Cross Segmento - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões  
  
**Solução**

Campo destinado a determinar o acréscimo financeiro por porcentagem, aparece só em simulações na planilha financeira e é aplicado na geração da nota fiscal de saída.

**E4\_ACRSFIN --> C5\_ACRSFIN**

**Exemplos:**

1 - Configuração da condição de pagamento:

(...)

E4\_CODIGO = 005

**E4\_ACRSFIN = 10 (Porcentagem de acréscimo)**

(...)

2 – No pedido de vendas:

**C5\_ACRSFIN = 10**

C5\_CONDPAG = 005

C6\_VALOR = 50

**Fórmula do cálculo:** C6\_VALOR + (C6\_VALOR \* [E4\_ACRSFIN/100])

* 0 - C6\_VALOR + (C6\_VALOR \* [E4\_ACRSFIN/100])
* 1 - 50 + (50 \* [10/100])
* 2 – 50 + (50 \* [0,1])
* 3 – 50 + 5
* 4 – 55

**Planilha financeira:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9370901226263)

**No título (caso gere [F4\_DUPLIC = 'S - Sim']):**

E1\_VALOR = 55

**Na nota fiscal:**

D2\_TOTAL = 55

**Saiba mais sobre as condições de pagamento:**

* **TDN:** <https://tdn.totvs.com/pages/viewpage.action?pageId=240310845>
* **KCS:** [Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Condições de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiYm7bSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNzQ2ODMxMi1Dcm9zcy1TZWdtZW50by1UT1RWUy1CYWNrb2ZmaWNlLUxpbmhhLVByb3RoZXVzLVNJR0FGQVQtQ29uZGklQzMlQTclQzMlQjVlcy1kZS1QYWdhbWVudG8GOwhUOg5zZWFyY2hfaWRJIikxMmE5MjAxYi1hNDYyLTRkYTYtYWZmNy1mN2ZhYTY0MjQ3YmUGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIh1jb25kacOnw7VlcyBkZSBwYWdhbWVudG8GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--8f786711cbd49788c1821a37316cd02b45236625) (<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017468312-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Condi%C3%A7%C3%B5es-de-Pagamento>)
