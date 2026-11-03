---
content_hash: 90a1ca2a1af643060f961bb18357cfcf9d46e9c69d36458cef4623e4ff61524a
fetched_at: '2026-06-29T00:10:30.400595+00:00'
page_id: '520093909'
product: rm
source: tdn-rm
title: FISCAL01-10380 DT - Consulta de Autorização do Evento R-1000 da Reinf
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520093909
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Consulta de Autorização do Evento R-1000 da Reinf |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10380 |

## **02. SITUAÇÃO/REQUISITO**

Consultar o Evento do R1000 e gravar a consulta no Histórico.

* Criar a arquitetura
* Seleção dos dados com PK (3 camadas será entregue depois)
* Gravar
* Teste
* Documentação
* Automação (se fizer sentido)

## **03. SOLUÇÃO**

Foi criado o processo de consulta de Autorização do Evento R-1000

* Criado uma estrutura base para ser reaproveitada para os demais Eventos
* O processo está funcionando somente selecionando os Eventos para consulta
* A gravação do processo ocorre corretamente emulando um resultado da receita onde: a cada 3 eventos consultados juntos, o primeiro será rejeitado, o segundo permanecerá pendente e o terceiro será autorizado
* Em todos os casos um histórico será gravado
* Em caso de Autorização os Eventos ficaram com o Status Autorizado. Eventos com status de pendente exclusão ficarão excluídos somente quando a consulta da exclusão for implementada.
* Caso em que o Evento ainda não tiver resposta, o status não será alterado e será informado que o Evento permanecerá pendente

## **04. DEMAIS INFORMAÇÕES**

Especificação do processo 

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
.aui-tabs.horizontal-tabs>.tabs-menu>.menu-item.active-tab a::after {
background: #FF9900; !important
}
.menu-item.active-tab {
border-bottom: none !important;
}
]]>
