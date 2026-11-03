---
content_hash: 58a6abaaaeb6c7bf954591663e460b3242867cd5518cb34919e633eb4042a398
fetched_at: '2026-06-29T00:10:53.277297+00:00'
page_id: '578057560'
product: rm
source: tdn-rm
title: DT - Data de Corte Novo Fluxo de Caixa
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Data+de+Corte+Novo+Fluxo+de+Caixa
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | RM |
| Segmento: | BACKOFFICE |
| Módulo: | Totvs Gestão Financeira |
| Função: | Menu Data Corte |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | 1. [FINANCEIRO01-16679](https://jiraproducao.totvs.com.br/browse/FINANCEIRO01-16679) |

## **02. SITUAÇÃO/REQUISITO**

Implementar no Novo Fluxo de Caixa campo com data específica para carregamento de saldo de extratos bancários.

**03. SOLUÇÃO**

Implementação de menu para informar Data de Corte na geração do Novo Fluxo de Caixa.

Passo 01, Passo 02, Passo 03, Passo 04passo1,passo2

Criado dentro do menu Gestão Financeira | Fluxo de Caixa a opção de processo "Data de Corte". Quando informada a data de corte toda geração do fluxo de caixa será a partir da data informada.

yespasso1

Quando definida a data de corte será carregado para o cadastro de conta caixa dois campos, "Data de Corte " e "Saldo Data de Corte" neste será preciso definir qual o valor de saldo da conta caixa para a data de corte e este será considerado nas movimentações geradas para geração do novo fluxo de caixa.

Quando gerado novo fluxo de caixa com data de corte todo carregamento será realizado com o valor de saldo da data de corte da conta caixa e da tada de corte.

## **04. DEMAIS INFORMAÇÕES**

Realizado tratamento de segurança de perfil de usuário para acesso ou restrição ao menu de Data de Corte.

**Use esse box para destacar informações relevantes e/ou de destaque.IMPORTANTE!**

## **05. ASSUNTOS RELACIONADOS**

* Coloque links com páginas de assuntos relacionados.

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
