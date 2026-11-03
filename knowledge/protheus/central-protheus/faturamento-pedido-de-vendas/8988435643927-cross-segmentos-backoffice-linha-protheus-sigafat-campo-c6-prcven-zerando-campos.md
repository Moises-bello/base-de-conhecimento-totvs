---
article_id: 8988435643927
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: a6b5ddcde45ca28a89fdf96956cab1c4e8b079466a06ec723137f789e736658c
fetched_at: '2026-06-28T22:38:42.485023+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Campo C6_PRCVEN zerando
  campos C6_NUMLOTE e C6_LOTECTL.
type: support-article
updated_at: '2023-01-17T13:52:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8988435643927-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Campo-C6-PRCVEN-zerando-campos-C6-NUMLOTE-e-C6-LOTECTL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:45 min****Ocorrência**No pedido de vendas, ao alterar o campo "**[C6\_PRCVEN] Prc Unitario**" está apagando os campos "**[C6\_LOTECTL] Lote**" e "**[C6\_NUMLOTE] Sub-Lote**".  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Todas as versões  
  
**Causa**Isso ocorre quando o pedido de vendas é Devolução de Compras [**C\_TIPO = 'D'**].

A nota fiscal de saída de devolução deve ser idêntica á de entrada, podendo variar a quantidade devolvida "[**C6\_QTDVEN**] **Quantidade**" e a "**[C6\_TS] Tipo Saida**".

Ao mudar o preço unitário (**C6\_PRCVEN**) o sistema retira o lote como forma de prevenção para não ocorrer retornos errados. Ao colocar o lote (**C6\_LOTECTL**), é gatilhado exatamente o preço da nota fiscal de entrada para aquele produto.

**OBS:** Os campos **C6\_QTDVEN** e/ou **C6\_TS** não alteram apagando os campos **C6\_LOTECTL** e **C6\_NUMLOTE**.

**Saiba mais:**

* **[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Lista de Pontos de Entrada da rotina de Pedidos de Venda (MATA410)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022359872-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Lista-de-Pontos-de-Entrada-da-rotina-MATA450A-An%C3%A1lise-de-Cr%C3%A9dito-Cliente)**
* **[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Nota sobre configuração de faturamento para sugerir quantidade de lote mínimo](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXJknzAQQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB2mh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDY0MjMxMzU3NjctQ3Jvc3MtU2VnbWVudG8tVE9UVlMtQmFja29mZmljZS1MaW5oYS1Qcm90aGV1cy1TSUdBRkFULU5vdGEtc29icmUtY29uZmlndXJhJUMzJUE3JUMzJUEzby1kZS1mYXR1cmFtZW50by1wYXJhLXN1Z2VyaXItcXVhbnRpZGFkZS1kZS1sb3RlLW0lQzMlQURuaW1vBjsIVDoOc2VhcmNoX2lkSSIpYWI5NjAxNWItMWExNC00NzdhLTlmM2EtZWY5MjU4NTNlMDI3BjsIRjoJcmFua2kIOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIPQzZfTE9URUNUTAY7CFQ6EnJlc3VsdHNfY291bnRpAfE%3D--c107c9baa47f3a8cce3f7c3f70e9f708502dc948)**
