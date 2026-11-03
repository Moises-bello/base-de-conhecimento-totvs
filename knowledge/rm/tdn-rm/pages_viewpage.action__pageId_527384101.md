---
content_hash: dad64eb96d9b4a596cb796b9f80c506eb8150c99c2f98fc86cfbb6fcef69baec
fetched_at: '2026-06-29T00:10:32.591376+00:00'
page_id: '527384101'
product: rm
source: tdn-rm
title: DT Gestão do pagamento recorrente (Cancelamento) - eduCONNECT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=527384101
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | eduConnect |
| Função: | Pagamento recorrente |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUCONNECT-317](https://jiraproducao.totvs.com.br/browse/DEDUCONNECT-317) |

## **02. SITUAÇÃO/REQUISITO**

Necessidade de visualização e possibilidade de cancelamento de recorrência para contratos previamente habilitados para pagamento recorrente.

## **03. SOLUÇÃO**

Implementação do menu de Gerenciamento de pagamento automático  na tela de visualização do extrato financeiro.

Importante

Esse menu somente estará visível se o parâmetro "Permitir habilitar pagamento automático" estiver marcado nos parâmetros do Totvs Gestão Educacional → EduConnect

Implementação da tela de gerenciamento de pagamentos automáticos (recorrentes)

O usuário, além de visualizar os contratos em recorrência juntamente com o cartão que será utilizado para pagamento automático (recorrente), poderá cancelar a recorrência para o contrato e cartão através da mesma visualização.

Acréscimo do ícone de pagamento automático no boleto de um contrato com recorrência habilitada.

Tratamento para não habilitar o campo para "Habilitar pagamento automático" na tela de carteira digital e na tela de dados de endereço do cartão para títulos cujos contratos estão em recorrência

Mais detalhes sobre a gestão do pagamento recorrente, consulte o documento de referência: [10.6 - Gestão do pagamento recorrente](https://tdn.totvs.com/display/LRM/10.3+-+Gerenciamento+da+Carteira+Digital)

Mais detalhes sobre a adesão ao pagamento automático (recorrente), consulte o documento de referência: [10.5 - Adesão ao pagamento automático](https://tdn.totvs.com/pages/viewpage.action?pageId=525821739)

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
