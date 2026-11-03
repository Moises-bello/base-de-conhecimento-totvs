---
article_id: 9371978794135
category: Faturamento - Cadastros
content_hash: 28c1e6be442a47280c2f4ddf4083979e45d74d372c656af67139fa5a515f1094
fetched_at: '2026-06-28T22:38:36.834177+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus – SIGAFAT – Preenchimento do campo "Lim.Superior"
  (E4_SUPER)
type: support-article
updated_at: '2024-07-09T20:16:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9371978794135-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Preenchimento-do-campo-Lim-Superior-E4-SUPER
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24771202501783) Tempo aproximado para leitura: **00:00:30 min**

**Dúvida**

Como preencher o campo "Lim.Superior" (E4\_SUPER) e para que este campo serve?

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões  
**Solução**

Nesse campo é definido qual será o valor máximo de um pedido de venda, caso nele seja utilizado uma certa condição de pagamento que restrinja esse valor máximo.

**OBSERVAÇÃO:** Se os campos “Limite superior (E4\_SUPER)” e “Limite inferior (E4\_INFER)” forem maiores que zero, o campo “Limite superior (E4\_SUPER)” não pode ser menor que o campo da condição de pagamento “Limite inferior (E4\_INFER)”.

Configuração de uma condição de pagamento para os exemplos:

**Se o total do pedido de vendas do rodapé for maior que o campo “Lim.Superior” (E4\_SUPER) do cadastro da condição de pagamento colocada no pedido de vendas, apresentará o HELP:**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9371953787031)**

**Exemplo da aplicação caso ela esteja inserida no pedido de vendas:**

Linha do item 1:

“Item" C6\_ITEM = 001

"Quantidade" C6\_QTDVEN = 1

"Prc Unitario" C6\_PRCVEN = 100

Linha do item 2:

"Item" C6\_ITEM = 002

"Quantidade" C6\_QTDVEN = 1

"Prc Unitario" C6\_PRCVEN = 100

Linha do item 3:

"Item" C6\_ITEM = 003

"Quantidade" C6\_QTDVEN = 1

"Prc Unitario" C6\_PRCVEN = 1

Apresentará o **HELP LJLIMSUPER** pelo total ter excedido o valor colocado no campo “Lim.Superior” (E4\_SUPER).

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9371953787031)

**Exemplo 2:**

Linha do item 1:

"Item" C6\_ITEM = 001

"Quantidade" C6\_QTDVEN = 1

"Prc Unitario" C6\_PRCVEN = 201

Apresentará o HELP LJLIMSUPER pelo total ter excedido o valor colocado no campo "Lim.Superior" (E4\_SUPER).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9371953031575)

O sistema considera o valor total do pedido de vendas, não apenas o valor da linha de item

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11938172610583)

**Saiba mais sobre as condições de pagamento:**

**TDN:**<https://tdn.totvs.com/pages/viewpage.action?pageId=240310845>

**KCS:** [Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Condições de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiYm7bSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNzQ2ODMxMi1Dcm9zcy1TZWdtZW50by1UT1RWUy1CYWNrb2ZmaWNlLUxpbmhhLVByb3RoZXVzLVNJR0FGQVQtQ29uZGklQzMlQTclQzMlQjVlcy1kZS1QYWdhbWVudG8GOwhUOg5zZWFyY2hfaWRJIikxMmE5MjAxYi1hNDYyLTRkYTYtYWZmNy1mN2ZhYTY0MjQ3YmUGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIh1jb25kacOnw7VlcyBkZSBwYWdhbWVudG8GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--8f786711cbd49788c1821a37316cd02b45236625) (<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017468312-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Condi%C3%A7%C3%B5es-de-Pagamento>)
