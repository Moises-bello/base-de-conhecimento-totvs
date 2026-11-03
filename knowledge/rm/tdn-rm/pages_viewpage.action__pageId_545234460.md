---
content_hash: bb381fab291ef4c8159568c4d76881405f86b7f045f4fde8b582d7cc5f74dc04
fetched_at: '2026-06-29T00:10:38.809897+00:00'
page_id: '545234460'
product: rm
source: tdn-rm
title: DT - Replicação de Produtos Compostos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=545234460
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Estoque |
| Função: | Cópia de Produtos entre Coligadas |
| Ticket: | 8570104 |
| Requisito/Story/Issue (informe o requisito relacionado) : | MATESTCNTFTOF01-7697 |

## **02. SITUAÇÃO/REQUISITO**

Após substituir um produto composto por outro no cadastro do produto, Anexos | Produtos Compostos e executar o processo Copiar Produto Entre Coligadas marcando a flag Substituir Registros no Destino, se eles já Existirem, na coligada destino o novo produto composto informado no produto será incluído corretamente, mas o produto composto que foi excluído, será mantido.

## **03. SOLUÇÃO**

Ajuste na cópia de produtos entre coligadas para atualizar as informações de produto composto.

## **04. DEMAIS INFORMAÇÕES**

Para que ocorre a atualização do produto composto, as coligadas de origem e destino devem estar parametrizadas para utilização do mesmo.

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
