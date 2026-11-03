---
content_hash: f7854358ea3463fa2ed0780259c49f4781db19af4b765f7381902cb74342e25b
fetched_at: '2026-06-29T00:10:15.997172+00:00'
page_id: '465398921'
product: rm
source: tdn-rm
title: DT Campo Porte da Empresa disponível para Pessoa Física (Cliente/Fornecedor)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=465398921
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Financeira |
| Função: | Cadastro de Cliente/Fornecedor |
| Ticket: | Não se aplica |
| Requisito/Story/Issue (informe o requisito relacionado) : | [FINANCEIRO01-9156](http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-9156) |

## **02. SITUAÇÃO/REQUISITO**

Com a finalidade de atender a demanda do e-Social, o campo Porte da Empresa deve estar disponível, permitindo que seja selecionada a opção "Microempreendedor Individual".

## **03. SOLUÇÃO**

O campo Porte da Empresa se tornou acessível, independente se o cliente/fornecedor é Pessoa Física, ou Pessoa Jurídica. Quando uma pessoa física seleciona o lookup de Porte da Empresa, apenas as opções "Normal" e "Microempreendedor Individual" serão permitidas pelo critério de validação do campo. Ao incluir um lançamento a "Pagar", com tipo de documento "Gerador de INSS", onde o cliente/fornecedor selecionado seja "Pessoa Física", e no porte da empresa esteja indicado tratar-se de um "Microempreendedor Individual", o sistema não calculará valor de INSS para Empregado, gerando apenas o INSS para o Empregador.

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
