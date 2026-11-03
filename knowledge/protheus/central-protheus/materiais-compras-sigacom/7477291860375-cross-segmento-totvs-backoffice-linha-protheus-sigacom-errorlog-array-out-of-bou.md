---
article_id: 7477291860375
category: Materiais - Compras (SIGACOM)
content_hash: fbf691749ebb798e688d909e8bcfe26e4716d26194e52a43b2fb63e3d6423d20
fetched_at: '2026-06-28T22:41:11.636965+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Error.log array
  out of bounds  on { | U | IF( PCOUNT() == 0, AINFADIC[18], AINFADIC[18] := U ) }(MATA103X.PRX)
type: support-article
updated_at: '2023-01-10T11:16:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7477291860375-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Error-log-array-out-of-bounds-on-U-IF-PCOUNT-0-AINFADIC-18-AINFADIC-18-U-MATA103X-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao utilizar a opção Tracker na rotina do Pedido de Compras (MATA121) é apresentado o error.log:  
array out of bounds on { | U | IF( PCOUNT() == 0, AINFADIC[18], AINFADIC[18] := U ) }(MATA103X.PRX)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**Para atender uma demanda na release 33, foram criados os campos:

F1\_INDPRES  
F1\_CODA1U  
F1\_ESTPRES

O erro pode ser apresentado por não ocorrer a compatibilização do Dicionário e a não criação dos campos, após rodar o UPDDISTR.

Para correção, o pacote pode ser acessado no endereço:

12.1.2210:<https://suporte.totvs.com/portal/p/10098/download?e=1073806> ; 12.1.27:<https://suporte.totvs.com/portal/p/10098/download?e=1073804> ; 12.1.33:<https://suporte.totvs.com/portal/p/10098/download?e=1073805> ;

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
