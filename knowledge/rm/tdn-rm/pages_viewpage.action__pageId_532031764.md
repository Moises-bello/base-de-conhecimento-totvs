---
content_hash: c90a5831532d4011453d7ad817dbe82ea4830aeac2ced56d0b6568fa6c4b0949
fetched_at: '2026-06-29T00:10:36.286963+00:00'
page_id: '532031764'
product: rm
source: tdn-rm
title: DT - Valores de Integração Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=532031764
version: 10
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Totvs Gestão Financeira |
| Função: | Valores de Integração |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | 1. [FINANCEIRO01-14229](https://jiraproducao.totvs.com.br/browse/FINANCEIRO01-14229) 2. [FINANCEIRO01-14449](https://jiraproducao.totvs.com.br/browse/FINANCEIRO01-14449) |

## **02. SITUAÇÃO/REQUISITO**

Configurar os valores de integração que farão parte dos lançamentos do módulo Financeiro e interface para  informar os valores de integração no módulo Financeiro.

## **03. SOLUÇÃO**

A parametrização dos valores de integração será por coligada, permitido configurar nenhum, um ou vários valores de integração cadastrados na tabela de definição. Somente lançamentos com Aplicação igual a "Financeiro" carregarão os valores de integração do financeiro para os lançamentos. 

**Cadastro dos valores de integração**

Os valores de integração serão cadastrados através do menu Cadastros | Específicos | Valores de Integração.

**Parametrização dos valores de integração**

A parametrização será através do menu: Ambiente | Parâmetros | Totvs  Gestão Financeira | Contas a Pagar/Receber | Lançamentos | Valores de Integração

**Interface dos valores de integração no Lançamento Financeiro**

Os valores de integração cadastrados e parametrizados no Gestão Financeira serão apresentados no lançamento financeiro, aba Valores | Valores de Integração sendo possível informar valor numérico com duas casas decimais no campo, mas quando cadastrado valor de integração com fórmula a edição não será permitida.

**Cálculo do valor líquido**

Os lançamentos de aplicação de origem no Financeiro, compõem o valor liquido quando houver valores nos campos e serão considerados na baixa do lançamento.

## **04. ASSUNTOS RELACIONADOS**

* Tabelas Relacionadas:

FLANINTEGRACAO

FLANINTEGRACAODEF

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
