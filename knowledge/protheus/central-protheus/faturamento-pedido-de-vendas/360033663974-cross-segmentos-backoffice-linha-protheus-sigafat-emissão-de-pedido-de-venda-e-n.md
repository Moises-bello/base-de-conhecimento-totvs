---
article_id: 360033663974
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 294e7f88d19099d5cdfb2afebda4f1cdf808c0f45e09e5d48d3022d02276dff7
fetched_at: '2026-06-28T22:38:39.582751+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Emissão de Pedido
  de Venda e Nota Fiscal com Valor Zerado
type: support-article
updated_at: '2026-03-25T20:23:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033663974-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Emiss%C3%A3o-de-Pedido-de-Venda-e-Nota-Fiscal-com-Valor-Zerado
---

**Dúvida**

Emissão de Pedido de Venda e Nota Fiscal com Valor Zerado.

**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

Para que o ambiente de faturamento permita a emissão de **Pedidos de Vendas** e **Notas Fiscais** com o **valor zerado**, basta realizar a **configuração** do **TES** (**MATA080**) de forma que o campo **"Vlr. Zerado" (F4\_VLRZERO) = "Sim"**.

Dessa forma o sistema permitirá o registro zerado na **SC6** **(C6\_PRCVEN)** e posteriormente na **SD2 (D2\_PRCVEN)**, levando o valor zerado para o **XML** e para o **DANFE**.

**Saiba Mais**:

[**FAT0144 Emissão de Pedido de Venda e Nota Fiscal com Valor Zerado**](https://tdn.totvs.com/x/ECv2Dw)
