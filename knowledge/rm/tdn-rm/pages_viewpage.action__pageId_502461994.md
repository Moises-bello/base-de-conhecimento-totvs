---
content_hash: 36a062ab038cc812738dd344f0e449ebd4b5cbd1078afcb32c5f64db15b15876
fetched_at: '2026-06-29T00:10:25.320985+00:00'
page_id: '502461994'
product: rm
source: tdn-rm
title: DT Conversão de Cliente Fornecedor  para Global
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=502461994
version: 15
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Totvs Gestão Financeira |
| Função: | Conversão de Cli/For  para Global |
| Ticket: | Totvs0c783de1-186e-383b-975c-a1acd7d76cb5FINANCEIRO01-7034 |
| Requisito/Story/Issue (informe o requisito relacionado) : | Totvs0c783de1-186e-383b-975c-a1acd7d76cb5FINANCEIRO01-7034 |

## **02. SITUAÇÃO/REQUISITO**

Conversão de cadastro de cliente Fornecedor para global.

## **03. SOLUÇÃO**

O objetivo do processo de conversão de Cliente Fornecedor Global é migrar os registros de cliente/fornecedor da  tabela FCFO, de não global para global eliminando os cadastros repetidos existentes em outras coligadas.

O processo deve ser executado em um coligada, que será uma coligada base, assim nas demais coligadas os registros serão excluídos e vinculados ao registro pai (de mesmo código) para as tabelas referenciadas. Os registros das tabelas filhas com informações por coligada serão mantidos e vinculados ao registro correspondente da coligada pai.

Deve ser selecionado também quais campos serão usados para definir o registro de cliente/fornecedor correspondente nas demais coligadas. Sendo eles "Código do Cli/For" e "CNPJ/CPF", pelo menos um dos campos deve ser marcado ou ambos.

Passo 01, Passo 02, Passo 03, Passo 04passo1,passo2yespasso1nopasso2

2. Use quando for necessário descrever um passo a passo.

## **04. DEMAIS INFORMAÇÕES**

**Todos os registros não globais de todas as coligadas serão convertidos e o processamento é irreversível.IMPORTANTE!**

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
]]>
