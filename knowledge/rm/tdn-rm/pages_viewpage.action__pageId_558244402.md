---
content_hash: 4abb5367e428ecee16c5bb4e234ede384d762ba5997df84da2cc95d25d2eb3fd
fetched_at: '2026-06-29T00:10:47.521365+00:00'
page_id: '558244402'
product: rm
source: tdn-rm
title: DT - Cancelamento de Empréstimo de EPI/EPC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=558244402
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | RH |
| Módulo: | Segurança e Saúde Ocupacional |
| Função: | Fornecimento Automático de EPI/EPC |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | RHU01-11344 - Cancelamento de Empréstimos de EPI/EPC |

## **02. SITUAÇÃO/REQUISITO**

Após o fornecimento de EPI para funcionários, ocorrem situações onde é necessário realizar o cancelamento deste fornecimento, visto que o funcionário não chegou a fazer uso do mesmo, isso é válido tanto para itens descartáveis quanto não descartáveis.

## **03. SOLUÇÃO**

Para solucionar essa demanda foi necessário criar uma nova funcionalidade que é o **Cancelamento** do fornecimento.

## **04. DEMAIS INFORMAÇÕES**

Esse traz consigo duas novas ações que é a possibilidade de efetivar o cancelamento com a opção "**Cancelar**" ou manter o empréstimo com a opção "**Não Cancelar**".

Além disso é importante reforçar que caso seja escolhida a opção **Cancelar** significa que o histórico deste fornecimento será apagado e esse procedimento é **irreversível** isso é informado ao usuário através da mensagem abaixo:

Outro detalhe é que quando trabalhar integrado ao **TOTVS Gestão de Estoque, Compras e Faturamento** (RM Nucleus) ao realizar o cancelamento, será gerado um movimento de devolução, independente do item ser ou não descartável.

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
