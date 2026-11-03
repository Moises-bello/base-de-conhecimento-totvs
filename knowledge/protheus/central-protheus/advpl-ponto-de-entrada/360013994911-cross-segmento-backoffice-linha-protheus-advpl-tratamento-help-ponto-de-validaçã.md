---
article_id: 360013994911
category: ADVPL - Ponto de Entrada
content_hash: d38aa1c35dc06bf058833ab2b0f95a3c1195817d86b769fa60e33f40aa261d21
fetched_at: '2026-06-28T22:40:11.584621+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Tratamento help ponto
  de validação MVC
type: support-article
updated_at: '2021-12-21T19:50:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013994911-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Tratamento-help-ponto-de-valida%C3%A7%C3%A3o-MVC
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Ao retornar false o formulário do MVC gera uma tela em branco, Help retornado em branco, quando o retorno é falso no formulário MVC.  
  
**Ambiente**Cross Segmento - Backoffice (Linha Protheus) - ADVPL – A partir da versão 11.80  
  
**Causa**Retorno .F. nas validações MVC.  
  
**Solução**O Help é padrão do MVC e neste caso precisa ser tratado, pois ao executar pontos de entrada em rotinas MVC e retornar false o formulário, será gerado obrigatoriamente um Help.

Essa mensagem é possível de ser customizada conforme exemplo abaixo:

```
ElseIf cIdPonto == 'FORMPOS'  
    Help(NIL, NIL, "HELP", NIL, "Informe a data", 1, 0, NIL, NIL, NIL, NIL, NIL, {"MENSAGEM"})  
    xRet := .F.  
EndIf
```
