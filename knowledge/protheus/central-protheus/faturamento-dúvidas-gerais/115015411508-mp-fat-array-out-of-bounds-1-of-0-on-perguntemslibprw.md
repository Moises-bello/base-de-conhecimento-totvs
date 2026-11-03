---
article_id: 115015411508
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: cc64dc6805153491d1e10a020e2586f72f60107a544f3ae465cdaf6ef87f069c
fetched_at: '2026-06-28T22:38:31.161150+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-array out of bounds ( 1 of 0 )  on PERGUNTE(MSLIB.PRW)
type: support-article
updated_at: '2023-01-16T20:00:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015411508-MP-FAT-array-out-of-bounds-1-of-0-on-PERGUNTE-MSLIB-PRW
---

**Ocorrência**   
  
Error.log quando entro na rotina de documento de saída (MATA460A):  
  
array out of bounds ( 1 of 0 )  on PERGUNTE(MSLIB.PRW) 28/06/2017 08:34:20 line : 2461  
  
[TOTVS build: 7.00.131227A-20170601 NG]  
Called from PERGUNTE(MSLIB.PRW) 28/06/2017 08:34:20 line : 2461  
Called from MATA460A(MATA461.PRX) 06/07/2017 15:24:43 line : 298  
Called from \_\_EXECUTE(APLIB090.PRW) 05/06/2017 17:10:02 line : 602  
Called from MDIEXECUTE(APLIB260.PRW) 04/04/2017 17:51:27 line : 820  
Called from STATICCALL(APLIB260.PRW) 04/04/2017 17:51:27 line : 820  
  
**Causa**  
  
A causa do erro são as perguntas 17 e 18 (“Romaneio de ?” e “Romaneio Ate ?”) estavam com o campo X1\_GSC em branco.   
  
**Ambiente**  
  
Microsiga Protheus - versão 11 e versão 12  
  
**Solução**  
  
Para solucionar  informe o Romaneio que deseja utilizar nas perguntas Romaneio de/até, exemplo “G” em ambos, para que assim,não gere mais o erro.
