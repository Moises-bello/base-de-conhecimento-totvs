---
article_id: 360018382512
category: Ativo-Fixo - Error log
content_hash: 968728c5f7784bafaaace035a096646ffc75207fd70fc49279fefed56be5ff81
fetched_at: '2026-06-28T22:41:54.825783+00:00'
product: protheus
section_id: 1500001547442
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - Como corrigir o erro
  "variable does not exist NOPC on {|a,b,c| FWInitCpo(a,b,c),lRet:=(If(FindFunction("AF190When"),AF190When(nOpc),.T.)),FWCloseCpo(a,b,c,lRet,.T.),lRet
  }(PROTHEUSFUNCTIONMVC.PRX)"
type: support-article
updated_at: '2023-11-30T19:42:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018382512-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Como-corrigir-o-erro-variable-does-not-exist-NOPC-on-a-b-c-FWInitCpo-a-b-c-lRet-If-FindFunction-AF190When-AF190When-nOpc-T-FWCloseCpo-a-b-c-lRet-T-lRet-PROTHEUSFUNCTIONMVC-PRX
---

**Dúvida**Como corrigir o erro "variable does not exist NOPC on {|a,b,c| FWInitCpo(a,b,c),lRet:=(If(FindFunction("AF190When"),AF190When(nOpc),.T.)),FWCloseCpo(a,b,c,lRet,.T.),lRet }(PROTHEUSFUNCTIONMVC.PRX) 20/09/2016 09:31:15"

**Ambiente**Protheus – Ativo Fixo – A partir da versão 11.80  
  
  
**Solução**

Para corrigir o erro e necessário retirar a validação do X3\_WHEN dos campos: "ND\_ITEM", "ND\_CODRESP", "ND\_DTINI", "ND\_DTFIM",  da tabela SND através do configurador.

**Importante**

Para impedir que erros como esse ocorram e necessário que mantenha o ambiente atualizado com as ultimas versões do dicionário diferencial (SDF.BRA) que deve estar na pasta systemload e o UPDDISTR deve ser executado.
