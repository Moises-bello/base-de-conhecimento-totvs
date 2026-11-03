---
article_id: 360018499931
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: b9f09b5fa150a643f15f9c534d3c5901746373313e0a3ddb5a76f655f6fea1ff
fetched_at: '2026-06-28T22:38:28.747920+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Preenchimento do
  campo "Forma" (E4_FORMA) no faturamento
type: support-article
updated_at: '2023-01-25T19:15:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018499931-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Preenchimento-do-campo-Forma-E4-FORMA-no-faturamento
---

**Dúvida**

Como preencher o campo "Forma" (E4\_FORMA) e para que este campo serve?

**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões  
  
**Solução**

Na regra de negócio, podemos configurar a mesma para utilizar a forma de pagamento, porém a forma de pagamento que será utilizada, é a forma existente na condição de pagamento (E4\_FORMA), não tendo nenhum relacionamento com o campo CV\_FORMAPG.

Para uso da forma de pagamento além do uso de validação da regra de negócio, contate a Equipe Protheus Automação Comercial.

Caso no campo de uma regra de negócio seja colocado no campo "Cond. Pagto" (ACT\_CONDPG) e "Tipo Regra" (ACT\_TPRGNG) = 1 - Regra, ou seja, a condição de pagamento que for colocada deve ser regra para todos os pedidos de venda.

Caso a condição de pagamento colocada no pedido de venda, não tenha o campo "Forma (E4\_FORMA)" a mesma conteúdo (forma de pagamento) requerido na regra de negócio.

**Saiba mais sobre as condições de pagamento:**

* **TDN:** <https://tdn.totvs.com/pages/viewpage.action?pageId=240310845>
* **KCS:** [Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Condições de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiYm7bSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNzQ2ODMxMi1Dcm9zcy1TZWdtZW50by1UT1RWUy1CYWNrb2ZmaWNlLUxpbmhhLVByb3RoZXVzLVNJR0FGQVQtQ29uZGklQzMlQTclQzMlQjVlcy1kZS1QYWdhbWVudG8GOwhUOg5zZWFyY2hfaWRJIikxMmE5MjAxYi1hNDYyLTRkYTYtYWZmNy1mN2ZhYTY0MjQ3YmUGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIh1jb25kacOnw7VlcyBkZSBwYWdhbWVudG8GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--8f786711cbd49788c1821a37316cd02b45236625) (<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017468312-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Condi%C3%A7%C3%B5es-de-Pagamento>)
