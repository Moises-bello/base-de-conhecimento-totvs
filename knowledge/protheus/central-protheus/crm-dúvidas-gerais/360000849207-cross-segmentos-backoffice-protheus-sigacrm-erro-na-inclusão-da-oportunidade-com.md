---
article_id: 360000849207
category: CRM - Dúvidas Gerais
content_hash: dfd80d0e66addacddc80b341263d5f62e79bded9903315d7e867860dcd7e4973
fetched_at: '2026-06-28T22:40:27.447976+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Erro na inclusão da oportunidade
  com o campo AD9_NOMCON
type: support-article
updated_at: '2024-04-25T12:10:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000849207-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Erro-na-inclus%C3%A3o-da-oportunidade-com-o-campo-AD9-NOMCON
---

**Ocorrência**

Ao incluir uma oportunidade, ocorre o erro: variable does not exist ACOLS on {|a,b,c| FWInitCpo(a,b,c),xRet:=(Posicione( "SU5", 1, xFilial( "SU5" ) + GDFieldGet( "AD9\_CODCON", Len( aCols ) ), "U5\_CONTAT" )),FWCloseCpo(a,b,c,.T.),FwSetVarMem(a,b,xRet),xRet }(PROTHEUSFUNCTIONMVC.PRX)  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGACRM - A partir da release 12  
  
**Causa**

O erro ocorre por que o x3\_relação do campo AD9\_NOMCON está com a validação: (Posicione( "SU5", 1, xFilial( "SU5" ) + GDFieldGet( "AD9\_CODCON", Len( aCols ) ), "U5\_CONTAT" ).

**Solução**  
Para solucionar essa ocorrência, ajuste as informações no campo: AD9\_NOMCON -X3\_RELAÇÃO para: **IIF(!INCLUI,AllTrim(Posicione("SU5",1,xFilial("SU5")+AD9->AD9\_CODCON,"U5\_CONTAT")),"")** que é o padrão do dicionário do sistema , para que o erro deixe de ocorrer.
