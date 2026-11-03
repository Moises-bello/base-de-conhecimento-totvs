---
article_id: 4412274451607
category: Comércio Exterior - Easy Export Control - Pedido - Export
content_hash: 08e02a5664e24e63edf140ea60d735652f8cdadedba3546b5a33cb6799f213e8
fetched_at: '2026-06-28T22:36:59.056155+00:00'
product: protheus
section_id: 1500001538181
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Ponto de entrada
  para replicar campos EE8_FABR e EE8_FALOJA  na tabela SC6
type: support-article
updated_at: '2021-11-04T21:02:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412274451607-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Ponto-de-entrada-para-replicar-campos-EE8-FABR-e-EE8-FALOJA-na-tabela-SC6
---

**Dúvida**Precisamos replicar os campos **EE8\_FABR** e **EE8\_FALOJA** do pedido de exportação (**EECAP100**) na tabela **SC6** de forma que ao criar o pedido de venda alimente automaticamente os dois campos. Temos algum ponto de entrada para esta situação?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**Neste caso você pode utilizar o ponto de entrada no fonte **EECAP100**, parâmetro **GRV\_PED**.  
Os valores necessários estarão nas variáveis **M->EE8\_FABR** e **M->EE8\_FALOJA**.  
  
**Saiba mais**[PE EECAP100 Pedido de Exportação](https://tdn.totvs.com/pages/releaseview.action?pageId=397378412)
