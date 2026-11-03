---
article_id: 36621735495575
category: SIGAEST - MOVIMENTAÇÕES
content_hash: bd5e942e46c5def431907c07bd84122b8c7a86767555200e7acd808c8de4153d
fetched_at: '2026-06-28T22:38:54.027991+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - InterFunctionCall:
  cannot find function A240NUMDOC in AppMap on A241INCLUI(MATA241.PRX) 19/11/2025
  17:09:11 line : 804'
type: support-article
updated_at: '2025-11-27T16:15:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36621735495575-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-InterFunctionCall-cannot-find-function-A240NUMDOC-in-AppMap-on-A241INCLUI-MATA241-PRX-19-11-2025-17-09-11-line-804
---

O erro ao incluir uma Movimentação Interna (MATA241) ocorre porque a função A240NUMDOC não é encontrada, estando declarada na rotina MATA240 de 19/11/2025. A solução é aplicar o pacote correspondente ao release do ambiente, testando antes em homologação. Links para os pacotes 12.1.2310, 12.1.2410 e 12.1.2510 estão disponíveis para correção.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36621701150743) Tempo aproximado para leitura: **00:03:20 min**  
  
**Ocorrência**

Ao tentar incluir uma Movimentação Interna (MATA241) apresenta o error.log abaixo. Como resolver?

THREAD ERROR ([58456], TOTVS, TOTVS)   27/11/2025 08:09:01  
**InterFunctionCall: cannot find function A240NUMDOC in AppMap on A241INCLUI(MATA241.PRX) 19/11/2025 17:09:11 line : 804**

[TOTVS build: 7.00.240223P-20251030]  
Called from FWFORMBROWSE:EXECUTE(FWFORMBROWSE.PRW) 06/10/2025 16:18:49 line : 1148  
Called from {|| OSELF:EXECUTE("A241INCLUI",              3,             0,"INCLUIR",              3,"","INCLUIR","",               3) }(FWFORMBROWSE.PRW) 06/10/2025 16:18:49 line : 580  
Called from ::MSDIALOG:ACTIVATE  
Called from FWMBROWSE:ACTIVATE(FWMBROWSE.PRW) 06/10/2025 16:18:49 line : 719  
Called from FWMBROWSE(MSLIB.PRW) 06/10/2025 16:18:49 line : 10488  
Called from MBROWSE(MSLIB.PRW) 06/10/2025 16:18:49 line : 171  
Called from MATA241(MATA241.PRX) 19/11/2025 17:09:11 line : 236  
Called from \_\_EXECUTE(APLIB090.PRW) 06/10/2025 16:18:46 line : 736  
Called from MDIEXECUTE(APLIB260.PRW) 06/10/2025 16:18:46 line : 923  
  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões   
  
**Causa**

Esse incidente ocorre devido não encontrar a função interna A240NUMDOC, pois a mesma esta declarada na rotina MATA240 de 19/11/2025.  
  
**Solução**

Para solucionar essa ocorrência, aplicar o pacote abaixo para o release do ambiente que apresenta o incidente. Sugerimos aplicar em base de homologação e testar antes do ambiente de produção:

***12.1.2310:***[***https://r.totvs.io/p/1225744***](https://r.totvs.io/p/1225744)***;***

***12.1.2410:***[***https://r.totvs.io/p/1225742***](https://r.totvs.io/p/1225742)***;***

***12.1.2510:***[***https://r.totvs.io/p/1225745***](https://r.totvs.io/p/1225745)***;***

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES) 

[SIGAEST - Movimentos Internos (MATA241) campo de Controle de Numeração D3\_DOC incorreto após confirmar o Movimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36572308581399-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Movimentos-Internos-MATA241-campo-de-Controle-de-Numera%C3%A7%C3%A3o-D3-DOC-incorreto-ap%C3%B3s-confirmar-o-Movimento)
