---
content_hash: 64eff64d0dada0629ffcebc6818b321b6604f8cee10cf09b758828ecfe0009b6
fetched_at: '2026-06-29T00:10:26.899001+00:00'
page_id: '515296910'
product: rm
source: tdn-rm
title: 6809348 MATESTCNTFTOF01-6530 DT Cancelar Solicitação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=515296910
version: 11
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Integração |
| Função: | CancelRequest |
| Ticket: | 6809348 |
| Requisito/Story/Issue (informe o requisito relacionado) : | MATESTCNTFTOF01-6530 |

## **02. SITUAÇÃO/REQUISITO**

Ao tentar cancelar uma Ordem de Serviço que acabou de ser incluída no sistema Manutenção de Ativos (SIGAMNT - PROTHEUS) a mensagem de CancelRequest apresenta o erro interno:  
"Error:O nome de namespace ou o tipo 'MovimentosItensCancelar' não pôde ser encontrado. Precisa de uma diretiva using ou de uma referência de assembly?a5cgd1e5.0.cs (47,9)"

## **03. SOLUÇÃO**

Melhoria interna no adapter de recebimento da mensagem CancelRequest versão 1.000, utilizada pela integração Manutenção de Ativos x BackOffice RM.

Atualização de adapters de integraçãopasso1yespasso1

Será necessário apagar o código fonte do adapter CancelRequest versão 1.000 e executar novamente o Configurador de Integrações para a integração Manutenção de Ativos x BackOffice RM. Para proceder com este procedimento, consulte o documento para atualização de adapters de integração:  

## **04. DEMAIS INFORMAÇÕES**

Outras ações/ações relacionadas 

**Este recurso está disponível a partir da versão 12.1.25.132 da Biblioteca RM.IMPORTANTE!**

## **05. ASSUNTOS RELACIONADOS**

* Documento de referência: [Backoffice RM x Protheus SigaMNT](https://tdn.totvs.com/display/LRM/Backoffice+RM+x+Protheus+SigaMNT)
* Documento de integração: <https://tdn.totvs.com/display/public/INT/DI0001_TOTVS_Gestao_de_Frotas-BackofficeRMxProtheusSigaMNT>

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
