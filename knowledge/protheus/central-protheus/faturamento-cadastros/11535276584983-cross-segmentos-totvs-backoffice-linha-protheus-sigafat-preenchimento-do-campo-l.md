---
article_id: 11535276584983
category: Faturamento - Cadastros
content_hash: 1e5ba0fc03b82d845022782a33b241373f7c1ddd13b86d126c8f83f47eda3d96
fetched_at: '2026-06-28T22:38:36.915038+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos – TOTVS Backoffice (Linha Protheus) – SIGAFAT – Preenchimento
  do campo "Lim. Inferior" (E4_INFER)
type: support-article
updated_at: '2026-04-02T20:35:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11535276584983-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Preenchimento-do-campo-Lim-Inferior-E4-INFER
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39483952817047) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

Para que serve o campo "Lim. Inferior" (E4\_INFER)?  
  
**Ambiente**  
Cross Segmentos – TOTVS Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões  
  
**Solução**

Nesse campo é definido qual será o valor mínimo de uma venda utilizando essa condição de pagamento.

Configuração da condição de pagamento para os exemplos:

"Lim. Inferior" (E4\_INFER) = 200

Informando essa condição de pagamento em um Pedido de Vendas (MATA410), caso o valor total do pedido seja menor que o "Lim. Inferior" (E4\_INFER), o sistema apresentará o HELP LJLIMINFER.

![LJLIMINFER.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11601307219351)

Nesse caso, o sistema considera o valor total do pedido de vendas, não apenas o valor da linha de item

![Valor_Total.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11601407276183)

 **Importante:** Os valores relacionados aos impostos no pedido de vendas não são considerados nessa configuração. O que será considerado será o **valor total** do pedido de vendas.

**Saiba mais sobre as condições de pagamento:**

* **TDN:** <https://tdn.totvs.com/pages/viewpage.action?pageId=240310845>
* **KCS:** [Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Condições de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiYm7bSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNzQ2ODMxMi1Dcm9zcy1TZWdtZW50by1UT1RWUy1CYWNrb2ZmaWNlLUxpbmhhLVByb3RoZXVzLVNJR0FGQVQtQ29uZGklQzMlQTclQzMlQjVlcy1kZS1QYWdhbWVudG8GOwhUOg5zZWFyY2hfaWRJIikxMmE5MjAxYi1hNDYyLTRkYTYtYWZmNy1mN2ZhYTY0MjQ3YmUGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIh1jb25kacOnw7VlcyBkZSBwYWdhbWVudG8GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--8f786711cbd49788c1821a37316cd02b45236625) (<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017468312-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Condi%C3%A7%C3%B5es-de-Pagamento>)
* **Campo E4\_SUPER:** [Cross Segmento - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Nota sobre o campo E4\_SUPER](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXhHcVhgg6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBn2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzkzNzE5Nzg3OTQxMzUtQ3Jvc3MtU2VnbWVudG8tQmFja29mZmljZS1MaW5oYS1Qcm90aGV1cy1GYXR1cmFtZW50by1TSUdBRkFULU5vdGEtc29icmUtby1jYW1wby1FNC1TVVBFUgY7CFQ6DnNlYXJjaF9pZEkiKTg2MTdhMDgwLWMwMzYtNGZjYy1iNjc5LTM4NzkwNTVkNDI5YgY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiDUU0X0lORkVSBjsIVDoScmVzdWx0c19jb3VudGlw--e4f00b8a3f60b17e4237b206b2cf1dcf43db7932)
