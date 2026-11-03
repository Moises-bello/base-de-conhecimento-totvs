---
article_id: 360024718113
category: Financeiro - Contas a Receber
content_hash: 4a3c96954fa3699edf42ab26dc6f920dd122a3526e9a5c4fc02f60ec3d9e674a
fetched_at: '2026-06-28T22:38:15.068386+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: 'MP - SIGAFIN - FINA460 - ERRORLOG - erro no parâmetroFWFormGridModel: Id FO1_VLABT
  inválido on FWFORMGRIDMODEL:LOADVALUE(FWFORMGRIDMODEL.PRX)'
type: support-article
updated_at: '2021-04-28T15:17:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024718113-MP-SIGAFIN-FINA460-ERRORLOG-erro-no-par%C3%A2metroFWFormGridModel-Id-FO1-VLABT-inv%C3%A1lido-on-FWFORMGRIDMODEL-LOADVALUE-FWFORMGRIDMODEL-PRX
---

**Ocorrência**Ao liquidar um título na rotina **FINA460**, apresenta a mensagem o erro no parâmetroFWFormGridModel: Id FO1\_VLABT inválido on FWFORMGRIDMODEL:LOADVALUE(FWFORMGRIDMODEL.PRX) 

**Ambiente**Microsiga Protheus - Financeiro - FINA460 - A partir da versão 12.1.17  
  
 **Causa**Esse error.log é apresentado pela falta do dicionário de dados sdfbra.txt  
  
 **Solução**Aplicar via UPDDISTR o dicionário de dados conforme arquivo em anexo.

Segue o procedimento para a atualização do dicionário de dados:   
<http://tdn.totvs.com/pages/releaseview.action?pageId=271415266>

**Importante:**Somente para sistemas Protheus Serie 3
