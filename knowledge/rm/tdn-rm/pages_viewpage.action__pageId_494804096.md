---
content_hash: bf3bfc6b02974500013f12b0c30363da312cd4df0f787044d01fa218f5987210
fetched_at: '2026-06-29T00:10:21.894339+00:00'
page_id: '494804096'
product: rm
source: tdn-rm
title: DEDUANALYTICS-1009 DT Ajuste nos itens do parametrizador para aceitar um número
  maior de registros.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=494804096
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Educacional |
| Módulo: | TOTVS Fast Analytics |
| Função: | Parametrizador |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | DEDUANALYTICS-1009 |

## **02. SITUAÇÃO/REQUISITO**

A lista de destino, dentro dos itens do parametrizador do Fast Analytics, não estava aceitando um número muito grande de registros, devido à uma limitação do tipo do campo onde os valores eram salvos.

## **03. SOLUÇÃO**

Foi realizada uma alteração na tabela HCPARAMETROS, com a criação do campo VALORTEXT. Esse campo agora será utilizado para registrarmos os valores parametrizados no Fast Analytics.

## **04. DEMAIS INFORMAÇÕES**

**Existe um script, que deverá ser solicitado para a equipe do Fast Analytics, através do suporte, que faz a alteração na tabela citada anteriormente, além de copiar os valores do campo antigo para o campo novo.IMPORTANTE!**

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
