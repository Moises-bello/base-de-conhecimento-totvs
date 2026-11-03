---
article_id: 360046086594
category: ADVPL - Ponto de Entrada
content_hash: dd0c76860d8a098f87449b0db8e6163b30e7e6c8dda2154559cbb07a621e94e8
fetched_at: '2026-06-28T22:40:12.936721+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL- utilização do ponto
  de entrada F550BCO em MVC
type: support-article
updated_at: '2021-12-30T18:18:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046086594-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-utiliza%C3%A7%C3%A3o-do-ponto-de-entrada-F550BCO-em-MVC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como gravar informações complementares com ponto de entrada F550BCO?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL– A partir da versão 12.1.25  
  
**Solução**Rotina FINA550 desenvolvida em MVC, desta forma para gravação de informações nas tabelas SE5/FK5 deve ser passado o conteúdo e campo para o modelo de dados na estrutura MVC.Exemplo:

```
User Function F550BCO()  
  
Local oModel    := FWModelActive()  
Local oSubFK5  
Local __lRet := .T.  
  
MsgAlert("Chamada do ponto de entrada: F550BCO")  
oSubFK5:= oModel:GetModel("FK5DETAIL")  
oSubFK5:SetValue( "FK5_HISTOR", "teste f550bco" )  
  
Return __lRet
```
