---
article_id: 360035791494
category: Escrita Fiscal - Error.log
content_hash: 379bd457de6fb43d3295a908ccb2ae03387783411f91efdb9cc8399cbc189810
fetched_at: '2026-06-28T22:39:32.917691+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: MP - FIS - Error.log - type mismatch on compare  on FISCHKDT(FISXFUN.PRX)
type: support-article
updated_at: '2021-04-28T21:08:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035791494-MP-FIS-Error-log-type-mismatch-on-compare-on-FISCHKDT-FISXFUN-PRX
---

**Dúvida**Ao reprocessar documento fiscal é apresentado o error.log abaixo:

type mismatch on compare on FISCHKDT(FISXFUN.PRX) 18/04/2018 14:50:52 line : 1823

Abaixo trecho da pilha de chamadas:

[TOTVS build: 7.00.131227A-20171204 NG]  
Called from FISCHKDT(FISXFUN.PRX) 18/04/2018 14:50:52 line : 1823  
Called from MA930PARAM(MATA930.PRX) 12/09/2019 18:53:27 line : 1032  
Called from MATA930(MATA930.PRX) 12/09/2019 18:53:27 line : 84  
Called from \_\_EXECUTE(APLIB090.PRW) 22/02/2018 16:52:33 line : 600  
Called from MDIEXECUTE(APLIB260.PRW) 22/02/2018 16:52:33 line : 819  
Called from STATICCALL(APLIB260.PRW) 22/02/2018 16:52:33 line : 819**Ambiente**  
Protheus – Livros Fiscais  – A partir da versão 11.80  
  
**Solução**

O error.log ocorre por motivo de não existir o parâmetro MV\_DATAFIS na base de dados ou quando o parâmetro existe, porém esta sem conteúdo.

Para solucionar, verificar os itens abaixo:

1-Verificar se o parâmetro MV\_DATAFIS existe para todas as filiais  
2-Verificar se todas as filiais estão com o parâmetro MV\_DATAFIS preenchido
