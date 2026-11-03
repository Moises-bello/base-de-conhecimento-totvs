---
content_hash: b09d7409be3dfb7e68b765118d8a91977dc2a6bcc0171670c064ad505451e23b
fetched_at: '2026-06-29T00:10:26.057143+00:00'
page_id: '510505029'
product: rm
source: tdn-rm
title: FISCAL01-10231 Registro R-1070 - API Validações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=510505029
version: 1
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | EFD Reinf |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10231 |

**02. SITUAÇÃO/REQUISITO**

A inclusão do registro R-1070 será realizada conforme a estrutura padrão dos eventos da EFD-REINF, porém com os detalhes abaixo.

## Validações

* O campo Id. Processo só poderá ser editado quando o Evento estiver com o Status "Não Transmitido", "Inconsistente" ou "Rejeitado";
* Os campos Início do Período e Fim do Período devem estar compreendidos no inicio e fim do período do R-1000 associado.

**03. SOLUÇÃO**

Foi criada a API referente ao registro R-1070 com as seguintes validações:

* O campo Id. Processo só poderá ser editado quando o Evento estiver com o Status "Não Transmitido", "Inconsistente" ou "Rejeitado";
* Os campos Início do Período e Fim do Período devem estar compreendidos no inicio e fim do período do R-1000 associado.

**03. DEMAIS INFORMAÇÕES**

Url para acesso da API de validação do R-1070:

GET Todos: <http://localhost:8052/api/fiscal/v1/eventoreinf/>  
GET 1: [http://localhost:8052/api/fiscal/v1/eventoreinf/1|1](http://localhost:8052/api/fiscal/v1/eventoreinf/1%7C1)  
POST: <http://localhost:8052/api/fiscal/v1/eventoreinf>  
PUT: [http://localhost:8052/api/fiscal/v1/eventoreinf/1|1](http://localhost:8052/api/fiscal/v1/eventoreinf/1%7C1)  
PATCH: [http://localhost:8052/api/fiscal/v1/eventoreinf/1|1](http://localhost:8052/api/fiscal/v1/eventoreinf/1%7C1)  
DELETE: [http://localhost:8052/api/fiscal/v1/eventoreinf/1|1](http://localhost:8052/api/fiscal/v1/eventoreinf/1%7C1)

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
