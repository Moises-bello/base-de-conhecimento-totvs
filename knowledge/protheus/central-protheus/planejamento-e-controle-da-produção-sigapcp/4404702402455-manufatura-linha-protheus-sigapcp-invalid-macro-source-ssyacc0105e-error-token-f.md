---
article_id: 4404702402455
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: a6df260746fd80d0d1b6f2f2fc848dba0f3b355dd058a145c48f908c4cdf69d9
fetched_at: '2026-06-28T22:42:43.493673+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - invalid macro source (SSYacc0105e:
  Error token failed, no valid token):({|a,b,c| FWInitCpo(a,b,c),xRet:=(!),FWCloseCpo(a,b,c,.T.),xRet
  }) on FWBUILDFEATURE(PROTHEUSFUNCTIONMVC.PRX)'
type: support-article
updated_at: '2023-02-13T11:11:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404702402455-Manufatura-Linha-Protheus-SIGAPCP-invalid-macro-source-SSYacc0105e-Error-token-failed-no-valid-token-a-b-c-FWInitCpo-a-b-c-xRet-FWCloseCpo-a-b-c-T-xRet-on-FWBUILDFEATURE-PROTHEUSFUNCTIONMVC-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:00:38 min**  
**Ocorrência**Ao abrir a rotina **MATA098 - Codificação** é apresentado o erro: **invalid macro source (SSYacc0105e: Error token failed, no valid token):({|a,b,c| FWInitCpo(a,b,c),xRet:=(!),FWCloseCpo(a,b,c,.T.),xRet }) on FWBUILDFEATURE(PROTHEUSFUNCTIONMVC.PRX)**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**Há uma **!** no campo **X3\_PICTVAR - Form. Variavel,** no campo **BQ\_TIPDEF - Tp Definicao**.  
  
**Solução**Para que o erro não ocorra mais é necessário retirar a **!** do campo **X3\_PICTVAR**.
