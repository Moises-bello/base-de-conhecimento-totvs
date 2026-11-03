---
article_id: 28295585287063
category: ADVPL - Classe e Função
content_hash: 4e2077e397e0aad17ffc53160d5c6f0643b57bdec0c0f6b6594a05b71ce6d136
fetched_at: '2026-06-28T22:40:21.625819+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - FwExecStatement
  - SetIn
type: support-article
updated_at: '2024-12-13T13:12:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28295585287063-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-FwExecStatement-SetIn
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28295568470039) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como utilizar o método SetIn da classe FwExecStatement?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**O método SetIn disponível na classe FwExecStatement, é herdado da classe FwPreparedStatement e é utilizado para instruções 'IN' do SQL. Segue exemplo abaixo:

Exemplo:

```
#INCLUDE "Protheus.ch"   
#INCLUDE "RWMAKE.CH"   
#INCLUDE "TBICONN.CH"   
  
  
user Function myExec()   
  
    Local cQuery as character   
    Local cAlias as character   
    local oExec as object   
  
    PREPARE ENVIRONMENT EMPRESA '01' FILIAL '01'   
  
    cQuery := "SELECT A1_FILIAL, A1_COD, A1_LOJA, A1_NOME FROM SA1010 WHERE A1_FILIAL = ? AND A1_COD IN (?) "   
    cQuery := ChangeQuery(cQuery)   
    oExec := FwExecStatement():New(cQuery)   
  
    oExec:SetString(1,'01')   
    oExec:SetIn(2,{'000001','000003'})   
    cAlias := oExec:OpenAlias()   
    Conout(cQuery)   
    cFinalQuery := oExec:GetFixQuery()   
    (cAlias)->(DbCloseArea())   
    oExec:Destroy()   
    oExec := nil   
  
    RESET ENVIRONMENT   
  
Return
```

**Saiba mais  
[FWExecStatement](https://tdn.totvs.com/display/public/framework/FWExecStatement)  
[FWPreparedStatement](https://tdn.totvs.com/display/public/framework/FWPreparedStatement)**
