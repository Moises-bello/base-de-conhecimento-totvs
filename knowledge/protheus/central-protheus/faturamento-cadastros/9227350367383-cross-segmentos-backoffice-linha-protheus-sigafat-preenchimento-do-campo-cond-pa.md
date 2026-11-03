---
article_id: 9227350367383
category: Faturamento - Cadastros
content_hash: 77d214152222eb01a52b40bc0942983af0009c4ac4c0446cc78ee2b57980e12e
fetched_at: '2026-06-28T22:38:36.691132+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Preenchimento do
  campo "Cond. Pagto (E4_COND)"
type: support-article
updated_at: '2023-02-17T11:11:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9227350367383-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Preenchimento-do-campo-Cond-Pagto-E4-COND
---

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9227346768279/mceclip0.png)Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**

Como preencher o campo E4\_COND e para que este campo serve?

**Ambiente**Cross Segmento - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

Nesse campo é colocado a regra da condição de pagamento, que diz respeito ao conteúdo colocado no campo E4\_TIPO.

O conteúdo desse campo determina a geração das duplicatas, caso o pedido de venda gere títulos (F4\_DUPLIC = “S – Sim”)

**Aumentar o campo:** Pode ser aumentado até 254 caracteres para adequar diferentes condições de pagamento.

**Ao cadastrar algumas regras para condição de pagamento do Tipo 1:**

Exemplo 1 de um cadastro de condição de pagamento:

"Tipo" E4\_TIPO = 1 (pode ser da tipo 1 até 9 e a tipo B)

**"Cond. Pagto" E4\_COND = 00,** **30, 60, 90**

**OBS:** Nesse tipo de regra (**00,** **30, 60, 90**), gerará uma duplicata à vista, uma parcela após 30 dias da emissão da nota fiscal de saída (F2\_EMISSAO), a segunda parcela após 60 dias após a emissão e, a terceira e última após 90 dias da emissão.

Ou seja, uma parcela à vista + 3 parcelas (3x).

Exemplo 2 de um cadastro de condição de pagamento:

"Tipo" E4\_TIPO = 1

**"Cond. Pagto" E4\_COND =** **[30,60,90],[50,22.5,22.5]**

**OBS:** Apresentará o HELP Cond. Pagto:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11926830674327)

O campo **“Cond. Pagto\* [E4\_COND]“** não recebeu uma regra da condição de pagamento do Tipo 1, recebeu uma regra da condição de pagamento do Tipo 8 (**[30,60,90],[50,22.5,22.5]**).

**Saiba mais sobre as condições de pagamento:**

* **TDN: [FAT - Condições de Pagamento (MATA360)](https://tdn.totvs.com/x/PdpSDg)**
