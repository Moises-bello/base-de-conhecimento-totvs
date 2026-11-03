---
article_id: 9246260905111
category: Faturamento - Cadastros
content_hash: e41144b6d8b10bc23c29bd6cb732b8a89a3581da8285bca91a8afc1ba12321d8
fetched_at: '2026-06-28T22:38:36.683372+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Preenchimento do
  campo "% Acres.Fin." (E4_ACRSFIN)
type: support-article
updated_at: '2023-01-25T19:25:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9246260905111-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Preenchimento-do-campo-Acres-Fin-E4-ACRSFIN
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**

Como preencher o campo "% Acres.Fin." (E4\_ACRSFIN) e para que este campo serve?

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

Na condição de pagamento, é permitido colocar acréscimos no pedido de venda dependendo da necessidade da condição de pagamento utilizada.

Esse campo destinado a determinar o acréscimo financeiro por porcentagem, aparece só em simulações na planilha financeira e é aplicado na geração da nota fiscal de saída, caso a condição de pagamento colocada no pedido de vendas "Cond Pagto (C5\_CONDPAG)" tenha o acréscimo informado no campo "% Acres.Fin." (E4\_ACRSFIN).

**Fluxograma de gatilhos:**

E4\_ACRSFIN (condição de pagamento) -> C5\_ACRSFIN (pedido de venda)

**Exemplos:**

1 - Configuração do cadastro de uma condição de pagamento qualquer:

* **E4\_ACRSFIN = 10 (Porcentagem de acréscimo)**

2 – Ao informar essa condição no pedido de vendas:

* **C5\_ACRSFIN = 10 (Acréscimo gatilhado)**
* C6\_VALOR = 50 (Total hipotético do pedido de vendas)

O total do título e nota fiscal de saída será R$55, pois no valor total sem o acréscimo que é R$50, foi aplicado 10% de acréscimo.

**Fórmula do cálculo:**

1 - C6\_VALOR + (C6\_VALOR \* [E4\_ACRSFIN/100])

2 - 50 + (50 \* [10/100])

3 – 50 + (50 \* [0,1])

4 – 50 + 5

5 – 55

**Planilha financeira:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9246129930263/mceclip0.png)

**No título (caso gere):**

* "Vlr.Titulo" E1\_VALOR = 55 (Valor do título financeiro)

**Na nota fiscal:**

* **"Vlr.Total" D2\_TOTAL = 55 (Valor da nota fiscal de saída)**

**Saiba mais sobre as condições de pagamento:**

* **TDN:** [Condições de Pagamento - Completo](https://tdn.totvs.com/x/PdpSDg)
* **KCS:** [Condições de Pagamento - Específico](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiYm7bSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNzQ2ODMxMi1Dcm9zcy1TZWdtZW50by1UT1RWUy1CYWNrb2ZmaWNlLUxpbmhhLVByb3RoZXVzLVNJR0FGQVQtQ29uZGklQzMlQTclQzMlQjVlcy1kZS1QYWdhbWVudG8GOwhUOg5zZWFyY2hfaWRJIikxMmE5MjAxYi1hNDYyLTRkYTYtYWZmNy1mN2ZhYTY0MjQ3YmUGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIh1jb25kacOnw7VlcyBkZSBwYWdhbWVudG8GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--8f786711cbd49788c1821a37316cd02b45236625)
