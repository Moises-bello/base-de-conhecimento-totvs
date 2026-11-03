---
content_hash: d304545668010de3e9a480445c7424f097d87e61bf3a5b73a12f4750af0ffaec
fetched_at: '2026-06-29T00:10:30.942153+00:00'
page_id: '520655857'
product: rm
source: tdn-rm
title: FOPCALCULO01-9004 - Alterações na tela do processo de geração TRCT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520655857
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Recursos Humanos |
| Módulo: | Folha de Pagamento |
| Função: | TRCT |
| Ticket: | 7404238 |
| Requisito/Story/Issue (informe o requisito relacionado) : | [FOPCALCULO01-9004](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-9004) |

## **02. SITUAÇÃO/REQUISITO**

Devido a quantidade de parâmetros contidos na tela de geração do TRCT é necessário que seja definida na máquina a resolução 1280 x 1024 para que todo o conteúdo da tela seja exibido. Algumas máquinas não possuem esta resolução e devido a isto as opções de 'Avançar' e 'Cancelar' não aparecem.

## **03. SOLUÇÃO**

Foi necessário a criação de uma nova aba 'Parâmetros ||', onde alguns parâmetros foram transportados para esta aba permitindo assim que a tela pudesse se adaptar á outras resoluções sem prejudicar a exibição de todos os parâmetros.

O comportamento do processo de geração do TRCT não foi alterado.

Seguem prints demonstrando a tela.

## **04. DEMAIS INFORMAÇÕES**

Outras ações/ações relacionadas 

## **05. ASSUNTOS RELACIONADOS**

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
