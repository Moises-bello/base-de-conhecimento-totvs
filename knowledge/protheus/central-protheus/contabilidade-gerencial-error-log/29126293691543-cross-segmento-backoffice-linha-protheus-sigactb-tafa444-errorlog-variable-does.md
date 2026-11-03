---
article_id: 29126293691543
category: Contabilidade Gerencial - Error log
content_hash: 908322c23554d74abcbcf35ef2f09542290f6605ae239683d35b1ceb4c57c374
fetched_at: '2026-06-28T22:40:52.027580+00:00'
product: protheus
section_id: 1500001537581
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - TAFA444 - Error.log
  "Variable does not exist CSLL"
type: support-article
updated_at: '2025-01-10T17:58:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29126293691543-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-TAFA444-Error-log-Variable-does-not-exist-CSLL
---

**Ocorrências:**Ao gerar o documento de arrecadação pela rotina TAFA444 é apresentando o error.log "variable does not exist CSLL"

**Ambiente:**Cross Segmento - TOTVS Backoffice Linha Protheus - Contabilidade Gerencial - a partir da release 12.1.2210 

**Solução:**A geração dos títulos a pagar no módulo SIGAFIN será gerado mediante configuração dos parâmetros MV\_IRF e MV\_CSLL para definição das naturezas. O Conteúdo dos parâmetros MV\_CSLL e MV\_IRF deve estar entre aspas duplas, conforme o exemplo a baixo:  
  
**MV\_IRF:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29126303212823)  
  
**MV\_CSLL:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29126293666455)  
  
**Saiba mais:**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=269087163#>  
<https://tdn.totvs.com/pages/releaseview.action?pageId=851297204>
