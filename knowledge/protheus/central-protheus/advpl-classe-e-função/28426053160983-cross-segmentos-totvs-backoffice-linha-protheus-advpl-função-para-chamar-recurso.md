---
article_id: 28426053160983
category: ADVPL - Classe e Função
content_hash: f433de98888c8c2e5873fd8568c031120138377142a13ed3f2e294d8c68f09d4
fetched_at: '2026-06-28T22:40:21.561132+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Função para chamar
  recurso SmartView no Protheus
type: support-article
updated_at: '2025-01-07T13:18:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28426053160983-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-para-chamar-recurso-SmartView-no-Protheus
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28426098687767)*Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**  
Existe alguma função para chamar um recurso do SmartView no Protheus?

**Ambiente**  
Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.2310

**Solução**  
Sim, para isso temos a função [CallSmartView](https://tdn.totvs.com/pages/releaseview.action?pageId=821179480), onde poderá realizar a chamada de um ou mais relatórios/visão de dados/tabelas dinâmicas em seu ambiente Protheus baseado nos arquivos (.TRP), integração SmartView ou o processo de [Amarração](https://tdninterno.totvs.com/pages/releaseview.action?pageId=708098869) [Smartview x Protheus.](https://tdninterno.totvs.com/pages/releaseview.action?pageId=708098869)  
  
**Exemplo CallSmartView**:

```
User Function callOne()  
Local lSuccess As logical  
    Local oSmartView As Object  
    oSmartView := totvs.framework.smartview.callSmartView():new("PEDIDOCOMPRA", "report")  
    lSuccess := oSmartView:executeSmartView()  
  
If !lSuccess  
Conout(oSmartView:getError())  
EndIf  
    oSmartView:destroy()  
Return .T.  
  
//Faz a chamada de recursos unificados no SmartView à partir do id  
User Function callMulti()  
Local lSuccess As logical  
    Local oSmartView As Object  
    oSmartView := totvs.framework.smartview.callSmartView():new("framework.sv.framework.pedidocompra")  
    lSuccess := oSmartView:executeSmartView()  
If !lSuccess  
Conout(oSmartView:getError())  
EndIf  
    oSmartView:destroy()  
Return .T.
```

**Saiba mais**

[Padrão para nomenclatura dos arquivos (.trp) (layouts)](https://tdn.totvs.com/pages/releaseview.action?pageId=821195415)  
[Smart View - Gerando os recursos através de uma função](https://tdn.totvs.com/pages/releaseview.action?pageId=725274049#SmartViewGerandoosrecursosatrav%C3%A9sdeumafun%C3%A7%C3%A3o-UnificandooMenu/Rotinacomrecursosdiferentes)  
[Classe para execução dos recursos no Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=821179480)
