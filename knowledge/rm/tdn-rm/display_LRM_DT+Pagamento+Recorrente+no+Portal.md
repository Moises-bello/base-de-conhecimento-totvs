---
content_hash: 2f26be07ad45cd8bc00bb33b66486ff2890c2fee72e7e71b9796051c01b6817d
fetched_at: '2026-06-29T00:10:37.797317+00:00'
page_id: '540889952'
product: rm
source: tdn-rm
title: DT Pagamento Recorrente no Portal
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Pagamento+Recorrente+no+Portal
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Educacional |
| Módulo: | Portal do Aluno |
| Função: | Novo Extrato Financeiro (Payments) |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUCONNECT-512](https://jiraproducao.totvs.com.br/browse/DEDUCONNECT-512) |

## **02. SITUAÇÃO/REQUISITO**

Foi solicitado a possibilidade de se habilitar a recorrência de pagamentos, desenvolvida no Meu eduCONNECT, também para o novo portal do aluno.

## **03. SOLUÇÃO**

Foram realizados ajustes no novo portal do aluno para permitir que a recorrência seja habilitada durante o pagamento utilizando o novo extrato financeiro.

Algumas regras devem ser seguidas:

* Para permitir que a recorrência funcione, o parâmetro "15.02 - Tesouraria | Geral 2/2 | Permitir habilitar pagamento automático" deve estar marcado.
* O pagamento recorrente só será exibido para cartões de crédito que já estejam cadastrados na carteira digital do aluno/responsável, ou caso o aluno/responsável esteja realizando o pagamento através de um novo cartão, indicando que o mesmo deva ser armazenado para futuros pagamentos.
* Ao selecionar a opção de pagamento recorrente, uma mensagem com instruções será exibida para o usuário, e o mesmo deverá indicar se permite ou não habilitar o pagamento recorrente.
* Caso já tenha sido cadastrado recorrência para o contrato, não será permitido habilitar novamente para outras parcelas desse mesmo contrato. Nesse caso a recorrência já estará habilitada, podendo ser identificada através do ícone de recorrência, ao lado do vencimento, no novo extrato financeiro.

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
