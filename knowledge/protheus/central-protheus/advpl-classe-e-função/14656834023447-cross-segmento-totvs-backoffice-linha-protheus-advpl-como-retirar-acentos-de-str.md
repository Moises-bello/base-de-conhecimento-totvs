---
article_id: 14656834023447
category: ADVPL - Classe e Função
content_hash: af920a0fa076ecd0e0d0f2f2a1ab40c4c65ce293b367347923a3eb7ff7fbe69e
fetched_at: '2026-06-28T22:40:20.627561+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL -  Como retirar acentos
  de strings?
type: support-article
updated_at: '2024-01-12T13:16:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14656834023447-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-retirar-acentos-de-strings
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **01:00:00 min** **Dúvida**Como realizar a retirada de acentos de strings?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Todas as Versões  
  
**Solução**

Pode-se utilizar as seguintes funções para tratar acentuação:

**NoAcento** Caso a *string*original esteja em formato ANSI é necessário converter a mesma para OEM, através da função Advpl AnsiToOem.  
   
**FwNoAccent** Retira acentos de uma *string*- *Defaut* "" - Sem necessidade de conversão.  
 

**FwCutOff** Função de apoio para retirar CR/LF/TAB de *strings*e eventualmente acentos.

**Outras funções uteis:** Para outro *caracteres*/*strings* não listadas acima***,*** pode utilizar funções como AT() StrTran() e SubStr() para substituir o caractere.

**Saiba Mais:  
[NoAcento](https://tdn.totvs.com/pages/releaseview.action?pageId=6814912)**

**[AnsiToOem](https://tdn.totvs.com/display/tec/ANSIToOEM)**

**[FwNoAccent](https://tdn.totvs.com/display/framework/FwNoAccent)**

**[FwCutOff](https://tdn.totvs.com/display/framework/FwCutOff)**

**[StrTran](https://tdn.totvs.com/display/tec/StrTran)**

**[SubStr](https://tdn.totvs.com/pages/releaseview.action?pageId=24347107)**

**[AT](https://tdn.totvs.com/pages/viewpage.action?pageId=27676809)**
