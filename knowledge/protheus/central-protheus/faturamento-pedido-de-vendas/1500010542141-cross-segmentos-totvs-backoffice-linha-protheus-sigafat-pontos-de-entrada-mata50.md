---
article_id: 1500010542141
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 227ea03ba2167bf7295363fb3ea848309f56bd5b264b142927f4bda752ec40ab
fetched_at: '2026-06-28T22:38:41.161053+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Pontos de Entrada
  MATA500
type: support-article
updated_at: '2023-06-16T12:26:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010542141-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pontos-de-Entrada-MATA500
---

**Dúvida**

Quais os pontos de entrada disponíveis na rotina Eliminação de Resíduos (**MATA500**)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**

Segue pontos de entrada disponíveis na rotina Eliminação de Resíduos **(MATA500):**

**- MTA500FTR** **-** Acrescentar condição customizada à variavel cFilMarkb - [**https://tdn.totvs.com/x/poVn**](https://tdn.totvs.com/x/poVn)  
**- MTA500QRY** **-** Acrescentar condição customizada à variável cQuery - [**https://tdn.totvs.com/x/qIVn**](https://tdn.totvs.com/x/qIVn)  
**- MTA500PROC -** Eliminação de resíduos - **<https://tdn.totvs.com/x/p4Vn>**  
**- MTA500FIL -** Acrescentar condição customizada à cláusula WHERE - **<https://tdn.totvs.com/x/pYVn>**  
**- MT500ANT -** Executado antes da eliminação de resíduo por registro do SC6 - **<https://tdn.totvs.com/x/gYVn>**

**- MT500APO -** Executado após a eliminação de resíduo por registro do SC6 -**<https://tdn.totvs.com/x/goVn>**  
**- MA550NCI -** Alterações na geração de NCC - **<https://tdn.totvs.com/x/vBayAg>**

**- MT500GRNCC -** Verifica a necessidade da geração de uma NCC para o cliente (não localizada documentação no TDN)

**- MT500NCC -** Ponto de entrada após a geração da NCC (não localizada documentação no TDN)

**Saiba Mais**

**[Pontos de Entrada - Faturamento - Protheus 12](https://tdn.totvs.com/x/owQhH)**
