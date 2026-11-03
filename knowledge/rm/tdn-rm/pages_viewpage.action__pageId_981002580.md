---
content_hash: bfef3d601675d1232f0133fccdd4176bb8ca2027edc5db813fe3ecfcb3f20250
fetched_at: '2026-06-29T00:12:15.647831+00:00'
page_id: '981002580'
product: rm
source: tdn-rm
title: Informações relativas aos Impostos do CT-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=981002580
version: 11
---

# imp -  Informações relativas aos Impostos

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **imp** | **[infCte](https://tdn.totvs.com/pages/viewpage.action?pageId=981000770)** | **1-1** | **Grupo** | **Informações relativas aos Impostos** |
| **ICMS** | **imp** | **1-1** | **Grupo** |  |
| vTotTrib | imp | 0-1 | Elemento | A soma de todos os TITMMOVFISCAL.VLRTOTTRIB do Movimento |
| infAdFisco | imp | 0-1 | Elemento | Não será gerado |
| **ICMSUFFim** | **imp** | **0-1** | **Grupo** |  |
| **IBSCBS** | **imp** | **0-1** | **Grupo** |  |
| vTotDFe | imp | 0-1 | Elemento | Gerado somente se possuir os tributos CBS e IBS com base de calculo maior que zero.  Gerado com o valor do vTPrest do grupo de  A partir de  será gerado com o somatório do vTPrest e os valores dos tributos |
