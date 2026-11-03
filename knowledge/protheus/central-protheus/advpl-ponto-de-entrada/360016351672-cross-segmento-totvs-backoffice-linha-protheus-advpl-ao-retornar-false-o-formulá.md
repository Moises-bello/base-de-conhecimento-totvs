---
article_id: 360016351672
category: ADVPL - Ponto de Entrada
content_hash: 337d0e8d97b0a6771cbdef9370155da898bc1fac5b631eff0c5baa8513135fdd
fetched_at: '2026-06-28T22:40:11.639938+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ao retornar false
  o formulário do MVC gera uma tela em branco
type: support-article
updated_at: '2022-06-21T18:00:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016351672-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ao-retornar-false-o-formul%C3%A1rio-do-MVC-gera-uma-tela-em-branco
---

**Ocorrência**Ao retornar *False* o formulário do **MVC**, é apresentado uma tela com a mensagem Problema.  
*Help* retornado em branco, quando o retorno é falso no formulário **MVC****Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**Ao executar o ponto de entrada em rotinas **MVC** e retornar *false* o formulário, será gerado obrigatoriamente um *Help*.

![](http://tdn.totvs.com/download/attachments/333780529/image2018-2-15_15-8-9.png?version=1&modificationDate=1518714490000&api=v2)  
**Solução**Essa mensagem é possível de ser **customizada** conforme exemplo abaixo:  
Para solucionar essa ocorrência, realize os seguintes passos:

`ElseIf cIdPonto == 'FORMPOS'`

`Help(NIL, NIL, "HELP", NIL, "Informe a data", 1, 0, NIL, NIL, NIL, NIL, NIL, {"MENSAGEM"})`

`xRet := .F.`

`EndIf`

![](http://tdn.totvs.com/download/attachments/333780529/image2018-2-15_15-9-4.png?version=1&modificationDate=1518714545000&api=v2)

**Saiba mais**[HELP](http://tdn.totvs.com/display/PROT/Help)
