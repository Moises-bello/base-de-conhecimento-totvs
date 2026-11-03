---
article_id: 360018012952
category: ADVPL - Ponto de Entrada
content_hash: 601d8efc0cbe12601aa3e923e9df43a7b1a815bdb456a5f4d4a095a4aec0cbf5
fetched_at: '2026-06-28T22:40:11.704443+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Inibe opção de inclusão
  na Consulta Padrão
type: support-article
updated_at: '2021-12-29T13:20:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018012952-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Inibe-op%C3%A7%C3%A3o-de-inclus%C3%A3o-na-Consulta-Padr%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como desabilitar a opção de incluir na consulta padrão?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Ponto de Entrada utilizado para efetuar validação que inibe a apresentação da opção de inclusão na **Consulta Padrão**.

Com a utilização do exemplo abaixo, são possíveis os seguintes cenários:

1 - Se a consulta padrão executada for a **SA1** ou **SB1**, o botão Incluir não será apresentado.

2 - Se for uma outra consulta:

* Se o acesso "Inclusão de dados via F3" estiver habilitado, o botão será apresentado;
* Se o acesso "Inclusão de dados via F3" estiver desabilitado, o botão não será apresentado.

```
#include "protheus.ch"  
  
User Function CPDBTNINS()  
  
Local cCons := Alltrim(ParamIXB[1])  
  
Local lRet := .T.  
  
// Se a consulta padrão que estiver sendo executada for a SA1 ou SB1, não apresenta o botão de inclusão.  
  
If cCons $ "SA1|SB1"      
  
ApMsgAlert("Usuário: "+ __cUserID + " abriu a consulta: " + cAlias + " e o botão Incluir não vai ser apresentado.")  
  
    lRet := .F.  
  
EndIf  
  
Return lRet
```

**Saiba Mais**

[CPDBtnIns - Inibe opção de inclusão na Consulta Padrão](http://tdn.totvs.com/pages/releaseview.action?pageId=6815177)
