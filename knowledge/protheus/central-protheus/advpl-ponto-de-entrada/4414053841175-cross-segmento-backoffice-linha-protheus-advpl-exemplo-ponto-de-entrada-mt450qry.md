---
article_id: 4414053841175
category: ADVPL - Ponto de Entrada
content_hash: 4dce128aaade6890c15ffc68a351676f16f59243ec011b2464ed33283c04388d
fetched_at: '2026-06-28T22:40:11.548419+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Exemplo ponto de entrada
  MT450QRY
type: support-article
updated_at: '2021-11-24T17:20:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414053841175-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Exemplo-ponto-de-entrada-MT450QRY
---

**Dúvida**  
Há um exemplo para utilização do Ponto de Entrada **MT450QRY**?  
  
**Ambiente**Cross Segmento - BackOffice (Linha Protheus) - ADVPL - A partir da versão P12  
  
**Solução**Para utilizar o ponto de entrada **MT450QRY** temos o exemplo abaixo:

```
#INCLUDE "Protheus.ch"  
  
User Function MT450QRY()  
  
    Local cFiltro := PARAMIXB[1]  
  
    Local cConsulta := cFiltro + " AND SC5.C5_CONDPAG = '001'"  
  
    Alert("Passou pelo PE MT450QRY")  
  
Return cConsulta
```

**Saiba mais**  
[MT450QRY - Filtro de seleção de pedidos](https://tdn.totvs.com/pages/releaseview.action?pageId=6784373)
