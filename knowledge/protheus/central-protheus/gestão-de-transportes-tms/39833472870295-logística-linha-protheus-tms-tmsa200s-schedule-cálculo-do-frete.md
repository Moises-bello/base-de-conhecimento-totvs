---
article_id: 39833472870295
category: Gestão de Transportes (TMS)
content_hash: 3a5bc6ab6ea47ad7d5391b4ba1f99aed359dec7e0829db39ee84eddb7660978e
fetched_at: '2026-06-28T22:45:33.414685+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - TMSA200S - Schedule Cálculo do Frete
type: support-article
updated_at: '2026-04-20T13:22:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39833472870295-Log%C3%ADstica-Linha-Protheus-TMS-TMSA200S-Schedule-C%C3%A1lculo-do-Frete
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39833422522263) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como funciona o **Schedule do Cálculo do Frete** no **TMS Protheus**?   
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**  
A rotina **TMSA200S - Schedule Cálculo do Frete** tem o objetivo de automatizar o cálculo do frete de documentos gerados pelo **TMS Protheus**, agilizando o processamento dos documentos de entrada.  
  
Ao implementar esta rotina no **Schedule**, o usuário não precisará mais realizar o cálculo do frete de forma manual, pois o schedule assumirá essa função.

Caso ocorra um erro de digitação e o cálculo do lote precise ser estornado, será necessário fechar o lote manualmente no menu **Outras Ações > Fechar Lote** para que o Sistema processe novamente o lote e realize o novo cálculo de forma automática.  
  
O usuário poderá configurar quais os tipos de lotes, **DTP\_TIPLOT** que serão calculados automaticamente pelo **TMSA200S**, para isso, utilizar o parâmetro **MV\_CALTPLT** - Tipo de lote para cálculo automático com:

* 1 - Normal
* 2 - Eletrônico
* 3 - Todos

**Saiba mais**  
[Schedule Cálculo do Frete (TMSA200S - SIGATMS)](https://tdn.totvs.com/pages/viewpage.action?pageId=630371310)  
[DLOGTMS02-19539 DT Cálculo Automático do Lote Normal](https://tdn.totvs.com/pages/releaseview.action?pageId=655865652)  
[PE TM200SQRY Permite manipular a query de execução do TMSA200S.](https://tdn.totvs.com/pages/viewpage.action?pageId=872691756)
