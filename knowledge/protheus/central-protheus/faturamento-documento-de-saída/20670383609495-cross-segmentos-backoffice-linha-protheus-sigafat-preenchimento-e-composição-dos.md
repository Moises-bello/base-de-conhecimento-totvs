---
article_id: 20670383609495
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: c95e88b42bab2a52bb6c4f96741e34547f025bc2b3724c0f3ddb5ce4c4e4bb80
fetched_at: '2026-06-28T22:38:43.984246+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Preenchimento e composição
  dos campos "Valor Fatura (F2_VALFAT)" e "Valor Bruto (F2_VALBRUT)"
type: support-article
updated_at: '2024-01-22T11:59:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20670383609495-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Preenchimento-e-composi%C3%A7%C3%A3o-dos-campos-Valor-Fatura-F2-VALFAT-e-Valor-Bruto-F2-VALBRUT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20670398189207) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Qual o cálculo de composição dos campos "Valor Fatura (F2\_VALFAT)" e "Valor Bruto (F2\_VALBRUT)"?

**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

**"Valor Bruto (F2\_VALBRUT)" é soma de:**

* **"Vlr. Total (D2\_TOTAL)" de todos os itens da nota fiscal de saída**
* **+ "Vlr. do INSS (D2\_VALINS)" de todos os itens da nota fiscal de saída**
* **+ "Vlr INSS Ad (D2\_VALINA)" de todos os itens da nota fiscal de saída**
* **+ "Valor do ISS (D2\_VALISS)" de todos os itens da nota fiscal de saída**
* **+ "Valor Pis (D2\_VALPIS)" de todos os itens da nota fiscal de saída**
* **+ "Valor CSLL (D2\_VALCSL)" de todos os itens da nota fiscal de saída**
* **+ "Valor Cofins (D2\_VALCOF)" de todos os itens da nota fiscal de saída**
* **+ "Vlr.IPI (D2\_VALIPI)" de todos os itens da nota fiscal de saída**
* **+ "Vlr. Fethab (D2\_VALFET)" de todos os itens da nota fiscal de saída**
* **+ "Vlr. Fabov (D2\_VALFAB)" de todos os itens da nota fiscal de saída**
* **+ "Vlr. Facs (D2\_VALFAC)" de todos os itens da nota fiscal de saída**

"Valor Fatura (F2\_VALFAT)" *é a mesma somatória acima porém multiplicado pela moeda faturada.*

* *Se a moeda do pedido for 1, caso seja diferente o sistema irá multiplicar pela taxa da moeda que foi faturado o documento de* *saída, "Moeda (C5\_MOEDA)" diferente de 1.*

**E****xemplo:** Se for Dólar por exemplo é vezes $5, ou seja, o resultado acima do campo **"Valor Bruto (F2\_VALBRUT)"** vezes 5.
