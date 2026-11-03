---
content_hash: 452704fd1575f520acf64dbdb804301cc64232ae0602cd20e7f474347b75ee1f
fetched_at: '2026-06-29T00:09:29.387668+00:00'
page_id: '425442368'
product: rm
source: tdn-rm
title: FISCAL01-6837 DT - Correção da Assinatura do evento OnContextPropValueChanged
  nos ActionModuleControllers
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425442368
version: 2
---

Tempo aproximado para leitura:**01 min**

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | Gestão Fiscal |
| Função: | Alteração de Contextos |

**02. SITUAÇÃO/REQUISITO**

Muitos produtos, no seu ***ActionModuleController***, assinam o evento ***OnContextPropValueChanged*** do ***RMSContext***, porém não removem a assinatura. Isso gera vazamento de memória e replicação de execuções desnecessárias pois o *ModuleController*é destruído e recriado em vários momentos distintos na manipulação da MDI. 

**03. SOLUÇÃO**

Foi efetuado um ajuste para que no ActionModuleController atribua o OnStartup e remover no OnFinalize.

div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
