---
article_id: 9306290787479
category: Faturamento - Cadastros
content_hash: 3207a4cea38bf9c045734a98b320623b3f4d69a9b5fad17eab059f14f38898e5
fetched_at: '2026-06-28T22:38:36.716234+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Preenchimento do
  campo "Status" (E4_MSBLQL)
type: support-article
updated_at: '2024-04-12T16:40:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9306290787479-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Preenchimento-do-campo-Status-E4-MSBLQL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**

Como preencher o campo "Status" (E4\_MSBLQL) e para que este campo serve?

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

Campo de status do registro da tabela de condição de pagamento. Determina se este registro/cadastro/ está ativo ou desativo para uso pelo sistema.

**Exemplos:**

1 – Condição de pagamento qualquer que possui o campo como “Inativo” em meio ao seu cadastro:

**E4\_MSBLQL = ‘1 – Inativo’**

Caso 1:

Ao entrar no **pedido de vendas (MATA410)** por exemplo, e no campo **“Cond. Pagto\* [C5\_CONDPAG]”** colocar a condição de pagamento **“123**”, apresentará o **HELP REGBLOQ:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9306186745367/mceclip1.png)

Caso 2:

Ao copiar um **pedido de vendas (MATA410)** que tem no campo **“Cond. Pagto\* [C5\_CONDPAG]”** a condição de pagamento **“123**”, já colocada anteriormente quando não era bloqueada, ao tentar salvar o pedido de vendas apresentará o **HELP A410CPGBLK:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9306247018647/mceclip0.png)

Caso 3:

Ao liberar parcialmente e/ou faturar um **pedido de vendas (MATA410)** que tem no campo **“Cond. Pagto\* [C5\_CONDPAG]”** a condição de pagamento **“123**”, já colocada anteriormente quando não era bloqueada será possível liberar parcialmente e faturar pois a condição de pagamento foi colocada quando ainda era válida.

**OBS:** Caso você reafirme a condição de pagamento dando, selecionado o campo C5\_CONDPAG e selecionando pela Lupa “F3” o sistema validará e alertará que a condição de pagamento está bloqueada.

2 – Condição de pagamento qualquer que possui o campo como “Ativo” em meio ao seu cadastro:

**E4\_MSBLQL = ‘2 – Ativo’**

É possível usar a condição de pagamento livremente sem a aparência de HELPS.

**Saiba mais sobre as condições de pagamento:**

* **TDN:** <https://tdn.totvs.com/pages/viewpage.action?pageId=240310845>
* **KCS:** [Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Condições de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiYm7bSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNzQ2ODMxMi1Dcm9zcy1TZWdtZW50by1UT1RWUy1CYWNrb2ZmaWNlLUxpbmhhLVByb3RoZXVzLVNJR0FGQVQtQ29uZGklQzMlQTclQzMlQjVlcy1kZS1QYWdhbWVudG8GOwhUOg5zZWFyY2hfaWRJIikxMmE5MjAxYi1hNDYyLTRkYTYtYWZmNy1mN2ZhYTY0MjQ3YmUGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIh1jb25kacOnw7VlcyBkZSBwYWdhbWVudG8GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--8f786711cbd49788c1821a37316cd02b45236625) (<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017468312-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Condi%C3%A7%C3%B5es-de-Pagamento>)
