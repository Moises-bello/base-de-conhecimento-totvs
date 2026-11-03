---
article_id: 360017421032
category: ADVPL - Ponto de Entrada
content_hash: 1473f575378626548d09fa16a835d7630caf35a0b840bf2ac58df6729b26e53b
fetched_at: '2026-06-28T22:40:12.861695+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Qual ponto de Entrada
  para validar se irá abrir a tela ou não na Mata103
type: support-article
updated_at: '2021-12-30T17:10:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017421032-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Qual-ponto-de-Entrada-para-validar-se-ir%C3%A1-abrir-a-tela-ou-n%C3%A3o-na-Mata103
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Qual ponto de Entrada para validar se irá abrir a tela ou não para classificação na Mata103?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL– A partir da versão 11.80  
  
**Solução**O Ponto de Entrada responsável para validar se irá abrir ou não a tela de Classificação da **Mata103** (documento de Entrada) é o  **MT103PN.**

```
#include 'totvs.ch'  
  
User Function MT103PN()  
  
Local nOp := PARAMIXB  
Local bRet  
  
  
bRet := MsgNoYes('Deseja continuar?',"Bloqueio")  
  
  
return bRet
```

**Saiba Mais**[MT103PN](http://tdn.totvs.com/pages/releaseview.action?pageId=6784333)
