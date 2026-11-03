---
content_hash: 6b5642dea59f4155666553db80f553140aa20bdd86a6ab171013cd97c6fb580e
fetched_at: '2026-06-29T00:10:51.590443+00:00'
page_id: '568949460'
product: rm
source: tdn-rm
title: DT - Fórmula Dados Bancários no Convênio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=568949460
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Totvs Gestão Financeira |
| Função: | Cadastro de Convênio, Borderô de Pagamentos |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FINANCEIRO01-15415 |

## **02. SITUAÇÃO/REQUISITO**

Facilitar a obtenção do melhor dados bancários para o lançamento a pagar na inclusão de Borderô de Pagamento para atender as regras customizadas. Desta forma, as regras de definição fica a cargo do usuário conforme suas necessidades

## **03. SOLUÇÃO**

Criação do campo "**Fórmula Dados Bancários**" no convênio onde o usuário poderá cadastrar uma fórmula contendo as suas regras específicas para a definição dados bancários que atende melhor ao lançamento financeiro a pagar na inclusão ou na vinculação ao Borderô de Pagamento. A fórmula deve retornar um Id presente no anexo "**Dados Bancários**" do cliente/fornecedor presente no lançamento.

ATENÇÃO

A fórmula irá considerar como contexto os dados correntes do **lançamento financeiro** antes da inclusão do Borderô de Pagamentos. A fórmula a ser executada será fórmula presente no convênio do lançamento selecionado e não o convênio informado na tela de processo. Na inclusão de Borderô de Pagamentos em Lote a fórmula a ser executada será do convênio presente no lançamento selecionado pelo filtro genérico.

## **04. DEMAIS INFORMAÇÕES**

No anexo de cadastro de Dados Bancários no cliente/fornecedor temos o campo "Forma de Pagamento".  Esse campo permite ao usuário selecionar a forma de pagamento para  dados bancários cadastrado que será informado no lançamento financeiro.

Desta forma, para facilitar o entendimento do valor desse campo, FormaPagamento , na tabela FDadosPgto. Segue uma tabela com o valor possíveis no campo e sua descrição.

|  |  |
| --- | --- |
| **Código** | **Descrição** |
| D | DOC (Compe) |
| T | Crédito em Conta Corrente no mesmo Banco |
| C | Cheque Administrativo |
| I | Título de Cobrança (Boleto) |
| N | Pagamento Eletrônico a Concessionários |
| P | Crédito em Conta de Poupança |
| R | Ordem de Pagamento à disposição |
| X | Crédito em Conta real time |
| Y | TED CIP |
| Z | TED STR |
| A | DARF |
| G | GPS |
| E | Débito Automático |
| M | Crédito em Conta Corrente de Mesma Titularidade |
| B | IPTU/ISS/Outros tributos municipais |
| F | DARJ |
| J | GARE - SP ICMS |
| L | FGTS - GFIP |
| O | GNRE e Tributos estaduais com código de barras |

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
.aui-tabs.horizontal-tabs>.tabs-menu>.menu-item.active-tab a::after {
background: #FF9900; !important
}
.menu-item.active-tab {
border-bottom: none !important;
}
]]>
