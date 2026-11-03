---
article_id: 18031185451287
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: de61d34c5b012c0198b9f578c18bdfa9dafc1b90881c0b429965cce91cfafe98
fetched_at: '2026-06-28T22:39:09.510882+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - InterFunctionCall:
  cannot find function M010GRRSTRUCT in AppMap on VIEWDEF(MATA010.PRX) 06/09/2023
  16:09:34 line : 518'
type: support-article
updated_at: '2023-10-04T20:01:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18031185451287-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-InterFunctionCall-cannot-find-function-M010GRRSTRUCT-in-AppMap-on-VIEWDEF-MATA010-PRX-06-09-2023-16-09-34-line-518
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18031216680983) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**

Apresenta o error.log abaixo ao tentar alterar ou copiar um produto na rotina ***CADASTRO DE PRODUTOS (MATA010)***. Como ajustar?

InterFunctionCall: cannot find ***function M010GRRSTRUCT*** in AppMap on VIEWDEF(MATA010.PRX) 06/09/2023 16:09:34 line : 518

[TOTVS build: 7.00.210324P-20230531]  
Called from FWLOADVIEW(PROTHEUSFUNCTIONMVC.PRX) 23/05/2023 15:13:33 line : 3838  
Called from FWVIEWEXEC:LOADVIEW(FWVIEWEXEC.PRW) 23/05/2023 15:13:33 line : 559  
Called from FWVIEWEXEC:OPENVIEW(FWVIEWEXEC.PRW) 23/05/2023 15:13:33 line : 466  
Called from FWEXECVIEW(PROTHEUSFUNCTIONMVC.PRX) 23/05/2023 15:13:33 line : 4504  
Called from MA010ALTER(MATA010M.PRX) 15/09/2023 14:52:18 line : 847  
Called from A010ALTERA(MATA010.PRX) 06/09/2023 16:09:34 line : 1416  
Called from FWFORMBROWSE:EXECUTE(FWFORMBROWSE.PRW) 23/05/2023 15:13:33 line : 1147  
Called from {|| OSELF:EXECUTE("A010ALTERA", 4, 2,"ALTERAR", 4,"","ALTERAR","", 4) }(FWFORMBROWSE.PRW) 23/05/2023 15:13:33 line : 579  
Called from ::MSDIALOG:ACTIVATE  
Called from FWMBROWSE:ACTIVATE(FWMBROWSE.PRW) 23/05/2023 15:13:33 line : 700  
Called from MATA010M(MATA010M.PRX) 15/09/2023 14:52:18 line : 76  
Called from MATA010(MATA010.PRX) 06/09/2023 16:09:34 line : 96  
Called from \_\_EXECUTE(APLIB090.PRW) 23/05/2023 15:13:31 line : 721  
Called from MDIEXECUTE(APLIB260.PRW) 23/05/2023 15:13:31 line : 924

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Causa**

Esse incidente ocorre, devido ausência da Função ***M010GRRSTRUCT***  que consta no fonte **MATA010GRR**.

**Solução**

Para solucionar essa ocorrência, aplicar o pacote de atualização pontual da rotina abaixo, sugerimos aplicar primeiramente em base de homologação e testar antes de sua base oficial

***12.1.2210:<https://suporte.totvs.com/portal/p/10098/download?e=1120859> ;***

***12.1.2310:<https://suporte.totvs.com/portal/p/10098/download?e=1120861> ;***

***12.1.33:<https://suporte.totvs.com/portal/p/10098/download?e=1120860> ;***

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre CADASTROS E CONFIGURAÇÕES GERAIS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
