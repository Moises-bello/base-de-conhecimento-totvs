---
article_id: 28648242772887
category: ADVPL - Relatório
content_hash: b629f79e6652eeb558c82e87de6ed2626fe09d4b6260c49ddbe209b5e1cbbbbb
fetched_at: '2026-06-28T22:40:22.965816+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Chamada de SmartView
  em Menu do Protheus
type: support-article
updated_at: '2025-01-07T13:21:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28648242772887-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Chamada-de-SmartView-em-Menu-do-Protheus
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28648279954199)*Tempo aproximado para leitura: 00:02:00 min

**Dúvida**  
Existe alguma forma de chamar um relatório SmartView via advpl/tlpp?

**Ambiente**  
Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.2310

**Solução**  
Para realizar o processo da chamada pode ser utilizado dois métodos :

- Chamando um recurso diretamente via Menu do módulo dentro do Configurador (SIGACFG), realizando o processo de [**Amarração Protheus X SmartView**](https://tdninterno.totvs.com/pages/releaseview.action?pageId=708098869)a partir da Integração configurada entre SmartView e Protheus.

- Chamada da função **[CallSmartView](https://tdn.totvs.com/pages/releaseview.action?pageId=821179480)** para realizar o processo, onde você pode realizar a chamada de um ou mais relatórios/visão de dados/tabelas dinâmicas, utilizando os **[arquivos .TRP compilados](https://tdn.totvs.com/pages/releaseview.action?pageId=821195415)** como parâmetros da função, conforme o exemplo abaixo.

**Obs:** Importante reiniciar o Server após a compilação, para que o fonte seja devidamente compilado no ambiente REST e assim localize os arquivos .TRP.

**Exemplo**:

```
//Chama um único recurso do SmartView  
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
  
//Faz a chamada de recursos múltiplos do SmartView à partir do ID dos arquivos TRP  
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

[**Amarração Protheus x Smart View**](https://tdninterno.totvs.com/pages/releaseview.action?pageId=708098869)  
[**Padrão para nomenclatura dos arquivos .trp (layouts)**](https://tdn.totvs.com/pages/releaseview.action?pageId=821195415)  
[**Smart View - Gerando os recursos através de uma função**](https://tdn.totvs.com/pages/releaseview.action?pageId=725274049#SmartViewGerandoosrecursosatrav%C3%A9sdeumafun%C3%A7%C3%A3o-UnificandooMenu/Rotinacomrecursosdiferentes)  
[**Classe para execução dos recursos no Protheus**](https://tdn.totvs.com/pages/releaseview.action?pageId=821179480)
