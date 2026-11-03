---
article_id: 360019796551
category: BI - Business- Intelligence - Workflow
content_hash: a4bb90ed51ab739afef3a8b4bf40981b8853ab1aee1b7c4e5221ab85eeac03ce
fetched_at: '2026-06-28T22:37:03.021022+00:00'
product: protheus
section_id: 1500001550762
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Customizar a tela de
  aprovação  do Workflow via Link
type: support-article
updated_at: '2022-02-15T19:04:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019796551-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Customizar-a-tela-de-aprova%C3%A7%C3%A3o-do-Workflow-via-Link
---

**Dúvida**Como fazer para customizar a tela de aprovação do Workflow via LInk?  
  
**Ambiente**Protheus – Workflow– A partir da versão 11.80  
  
**Solução**Para customizar a tela de aprovação via Link deverá utilizar o ponto de entrada **WFPE007**

**Exemplo do Ponto.**

```
User Function WFPE007()  
  
Local cHTML := ""  
 Local plSuccess := ParamIXB[1]   
 Local pcMessage := ParamIXB[2]   
 Local pcProcessID := ParamIXB[3]  
   
 If ( plSuccess )   
 //-------------------------------------------------------------------  
 // Mensagem em formato HTML para sucesso no processamento.   
 //-------------------------------------------------------------------   
 cHTML += 'Processamento executado com sucesso!'  
 cHTML += '<br>'  
 cHTML += pcMessage  
 Else   
 //-------------------------------------------------------------------  
 // Mensagem em formato HTML para falha no processamento.   
 //-------------------------------------------------------------------   
 cHTML += 'Falha no processamento!'  
 cHTML += '<br>'  
 cHTML += pcMessage  
 EndIf  
   
 conout('FIM')  
   
Return cHTML
```

**Saiba Mais**

**[Help Workflow](https://cms.totvs.com/mktfiles/tdiportais/helponlineprotheus/portuguese/sigaworkflow.htm)**

**[WFPE007](http://tdn.totvs.com/display/PROT/WFPE007)**
