---
article_id: 360041217794
category: Escrita Fiscal - Impostos - ISS
content_hash: b997c88ca8d57884c7f389055a81e6b8edad6300d7dd06a8f8ae5b262337fc78
fetched_at: '2026-06-28T22:39:35.123532+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  Dedução do ISS na
  base de cálculo do PIS e COFINS apuração em operações de saída
type: support-article
updated_at: '2024-11-16T22:03:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041217794-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Dedu%C3%A7%C3%A3o-do-ISS-na-base-de-c%C3%A1lculo-do-PIS-e-COFINS-apura%C3%A7%C3%A3o-em-opera%C3%A7%C3%B5es-de-sa%C3%ADda
---

**Dúvida**Como eu faço para deduzir o ISS ou não da base de calculo do PIS e COFINS em operações de saídas.

**Ambiente**Protheus – Faturamento – A partir da versão 12.1.17  
  
**Solução**  
Para realizar essa tratativa será necessário alterar a condição do parâmetro MV\_DEISSBS conforme abaixo:

| **MV\_DEISSBS** |
| --- |
| Indica se o valor do ISS deve ser retirado da base de cálculo do PIS/COFINS/CSLL. |
| * **MV\_DEISSBS = .F.** - o ISS será descontado na base do PIS/COF/CSLL |
| * **MV\_DEISSBS = .T.** - o ISS não será descontado na base do PIS/COF/CSLL |

**Importante:**

O parâmetro **MV\_DEISSBS**é exclusivo para operações de saída.

Mais informações: <https://tdn.totvs.com/pages/releaseview.action?pageId=516201784>
