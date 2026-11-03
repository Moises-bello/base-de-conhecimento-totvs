---
article_id: 34975727614359
category: Escrita Fiscal - Configurador de Tributos
content_hash: b64477bad9968f1af895efcb12155e4e874cb788909f274100a98923801dd2ab
fetched_at: '2026-06-28T22:39:17.704798+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – ERROR.LOG cannot
  find function CHARGECK2 in AppMap on X170CARGA(FISA170.PRW) ao acessar o Configurador
  de Tributos
type: support-article
updated_at: '2025-11-04T21:17:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34975727614359-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-ERROR-LOG-cannot-find-function-CHARGECK2-in-AppMap-on-X170CARGA-FISA170-PRW-ao-acessar-o-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34975773028503) Tempo aproximado para leitura: **00:10 min**  
  
**Ocorrência**  
Ao acessar a rotina Configurador de Tributos é apresentado HELP e ERROR.LOG

**HELP:** Função: ChargeCK2 Called By X 170CARGA

**ERROR.LOG:** InterFunctionCall: cannot find function CHARGECK2 in AppMap on X170CARGA(FISA170.PRW)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**  
Para solucionar o error.log, é necessário realizar a aplicação do pacote abaixo:

12.1.2210:<https://r.totvs.io/p/1211908> ; 12.1.2310:<https://r.totvs.io/p/1211907> ; 12.1.2410:<https://r.totvs.io/p/1211906> ; 12.1.2510:<https://r.totvs.io/p/1211905> ;
