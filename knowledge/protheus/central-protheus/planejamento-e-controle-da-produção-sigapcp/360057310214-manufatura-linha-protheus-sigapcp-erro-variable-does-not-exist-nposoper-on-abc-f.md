---
article_id: 360057310214
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: a589c72f95df72804fe56e4980460f055aad746646092f0ab2fbfd498db3e98d
fetched_at: '2026-06-28T22:42:42.296080+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Erro variable does not exist NPOSOPER
  on {|a,b,c| FWInitCpo(a,b,c),xRet:=(Soma1(aCols[n-1,nPosOper],2)),FWCloseCpo(a,b,c,.T.),FwSetVarMem(a,b,xRet),xRet
  }
type: support-article
updated_at: '2021-08-06T14:21:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057310214-Manufatura-Linha-Protheus-SIGAPCP-Erro-variable-does-not-exist-NPOSOPER-on-a-b-c-FWInitCpo-a-b-c-xRet-Soma1-aCols-n-1-nPosOper-2-FWCloseCpo-a-b-c-T-FwSetVarMem-a-b-xRet-xRet
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:07 min**  
**Ocorrência**Ao tentar cadastrar um roteiro de operação no **MATA632 - Roteiros e Operação** é apresentado o erro **variable does not exist NPOSOPER on {|a,b,c| FWInitCpo(a,b,c),xRet:=(Soma1(aCols[n-1,nPosOper],2)),FWCloseCpo(a,b,c,.T.),FwSetVarMem(a,b,xRet),xRet }(PROTHEUSFUNCTIONMVC.PRX)**  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**O erro ocorre pois há informação **Soma1(aCols[n-1,nPosOper],2)**, no**X3\_RELACAO - Inic. Padrão**, do campo **G2\_OPERAC - Operação.**  
  
**Solução**Para que o erro não ocorra, deve-se limpar o conteúdo **Soma1(aCols[n-1,nPosOper],2)**, do **X3\_RELACAO**, do campo **G2\_OPERAC**, da tabela **SG2 - Roteiros e Operação.  
  
Importante**  
Lembramos que a partir da **versão 11.8** o programa **MATA630 - Roteiro e Operações** foi substituído pelo **MATA632**, por gentileza fazer um novo teste utilizando este programa.
