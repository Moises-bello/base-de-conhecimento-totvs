---
content_hash: c03b6212f9a105c23db3e2aa27b16e83b34e1c8fbe957370c34d7dfd705d50f8
fetched_at: '2026-06-29T00:10:32.634169+00:00'
page_id: '527388561'
product: rm
source: tdn-rm
title: DT - Tratamento na Folha Analítica e GPS para incidência exclusiva do segurado
  e exclusiva do empregador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=527388561
version: 6
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | Tratar na Folha Analítica e GPS a Incidência exclusiva do segurado e exclusiva do empregador |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : |  |

## **02. SITUAÇÃO/REQUISITO**

Necessidade de tratamento na **Folha Analítica**e**GPS**para atender os campos de **INSS** (Incidência Exclusiva do Segurado e Incidência Exclusiva do Empregador) e **INSS 13**° (Incidência Exclusiva do Segurado) existentes no cadastro de eventos.

## **03. SOLUÇÃO**

Tratamento na **Folha Analítica**e**GPS**para atender os campos de **INSS** (Incidência Exclusiva do Segurado e Incidência Exclusiva do Empregador) e **INSS 13**° (Incidência Exclusiva do Segurado) existentes no cadastro de eventos.  
   
**Folha****A****nalítica**

Foram criados dois campos, sendo eles:

**Base INSS - Envelope**

**Base INSS 13° - Envelope**

Além disso, foram adaptados os cálculos e descrições dos campos:

**Base INSS**  descrição alterada para **Base INSS - GPS**

**Base INSS 13°**descrição alterada para **Base INSS 13° - GPS**

Regra para cálculo dos campos:

**Base INSS - GPS**: o sistema considera os valores dos eventos que tem incidência de INSS ou incidência exclusiva do empregador.  
**Base INSS - Envelope**: o sistema considera os valores dos eventos que tem incidência de INSS ou incidência exclusiva do segurado.  
**Base INSS 13° - GPS**: o sistema considera os valores dos eventos que tem incidência de INSS 13°.

**B****ase INSS 13° - Envelope:** o sistema considera os valores dos eventos que tem incidência de INSS 13° ou incidência exclusiva do segurado.

   
**GPS**

Ajustado o cálculo para sempre considerar os valores dos eventos que tem somente incidência **INSS** ou **Incidência Exclusiva do Empregador** ou no caso da GPS de 13° considerar a incidência de **INSS 13°**.  

## **04. ASSUNTOS RELACIONADOS**

* #### [Folha analítica e GPS - Incidência Exclusiva do segurado no 13° salário.](https://tdn.totvs.com/pages/viewpage.action?pageId=520671442)
* #### [Folha analítica e GPS - Incidência Exclusiva do segurado e Incidência Exclusiva do Empregador](https://tdn.totvs.com/pages/viewpage.action?pageId=520101874)

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
