---
content_hash: d7e8a461017f283d6a52f68faf6f5376ea993b54a5290d6394a3adc79f691a91
fetched_at: '2026-06-29T00:10:30.058295+00:00'
page_id: '518487454'
product: rm
source: tdn-rm
title: DT Melhoria na Ferramenta de Demonstração Contábil para se tornar multi-coligada.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=518487454
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BACKOFFICE |
| Módulo: | Totvs Gestão Contábil |
| Função: | Cadastro de Demonstrações Contábeis |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | CONTROLADORIA01-3779  CONTROLADORIA01-3780  CONTROLADORIA01-3783  CONTROLADORIA01-3802 |

## **02. SITUAÇÃO/REQUISITO**

* Permitir que a estrutura de demonstração contábil seja multi-coligada permitindo a consolidação dos valores das empresas consolidadas/controladas/controladoras.
* Configurar os fatos/colunas por coligadas quando o template do relatório for do tipo "Consolidado". Isto permitirá que seja possível configurar um relatório buscando saldos de diversas coligadas com suas respectivas contas contábeis.
* Ordenar a lista de contas por coligada e conta contábil.
* A aba de filtro complementar e as opções de filtro genérico, existentes no campo Origem de Valor, não serão exibidas se a estrutura de demonstração contábil permitir a consolidação de valores.

## **03. SOLUÇÃO**

Na tela de cadastro da estrutura de demonstração foi adicionado o campo "Consolidado". Ao marcar esse campo será possível utilizar contas contábeis de mais de uma coligada para compor o saldo dos fatos contábeis nas colunas que forem criadas para a estrutura.

Quando a estrutura possuir um fato cadastrado não será permitido marcar ou desmarcar esse campo

Foi adicionado o campo Coligada na aba Conta(s). Após selecioná-la o Lookup de contas irá exibir apenas as contas contábeis da coligada informada.

É importante frisar que após salvar as alterações a lista de contas será ordenada por coligada e conta contábil.

A aba de filtro complementar e as opções de filtro genérico, existentes no campo Origem de Valor, não estão sendo exibidas, pois essa é uma estrutura de consolidação.

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
