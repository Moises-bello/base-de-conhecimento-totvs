---
article_id: 360019859292
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 85763da7bb7a10a3e9cbbe86e077eb1b46807e9964c888447f649aed26c81c37
fetched_at: '2026-06-28T22:39:30.516166+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Alíquotas com asteriscos
  no documento de entrada (MATA103).
type: support-article
updated_at: '2021-07-29T14:28:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019859292-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Al%C3%ADquotas-com-asteriscos-no-documento-de-entrada-MATA103
---

**Dúvida**

Cliente destacou problema de visualização no campo alíquota, aba impostos, no documento de entrada após escriturar uma nota fiscal com impostos (PIS,COFINS,IPI OU ICMS). Ao invés de aparecer a alíquota correspondente, o sistema destaca as alíquotas com asteriscos.

**Ambiente**

Protheus – Fiscal – A partir da versão 11.80.  
  
  
**Solução**

Caso o cliente tenha alterado o tamanho dos campos no configurador, é necessário ativar o conteúdo do parâmetro MV\_DECALIQ para .T.
