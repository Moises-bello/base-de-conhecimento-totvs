---
content_hash: 46a3afe71825526e77634c7432aec7ae80b50e93179f5bc417656bd99baba76e
fetched_at: '2026-06-29T00:10:25.066171+00:00'
page_id: '501458300'
product: rm
source: tdn-rm
title: MATESTCNTFTOF01-5945 DT Atualização de Produto via Conceito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=501458300
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM. |
| Segmento: | BackOffice. |
| Módulo: | Gestão de Estoque, Compras e Faturamento. |
| Função: | Importação/Exportação de Produtos. |
| Ticket: | - |
| Requisito/Story/Issue (informe o requisito relacionado) : | MATESTCNTFTOF01-5945. |

## **02. SITUAÇÃO/REQUISITO**

Ao exportar um produto pelo **Gerador de Saídas**, o layout não possui campo para a **Classificação do Serviço** (**Cadastro do Produto > Anexos > Dados Fiscais do Produto**) nem o conceito **CONEST0004 - Produto** possui tal campo para importação. Por isto, se o produto possuir a classificação informada e houver uma atualização de registros pelo conceito, atualizando qualquer outro campo do cadastro, o valor do campo **Classificação de Serviço** será apagado.

## **03. SOLUÇÃO**

Melhoria realizada nos arquivos de Exportação / Importação de Produto. Foi disponibilizado no layout de exportação **ESTLAY0004 - Produtos - v4.TotvsGen** e no conceito de importação **CONEST0004 - Produto - V4.concept** os campos **Código Atividade Econômica** e **Classificação do Serviço** do cadastro de **Dados Fiscais do Produto**.

## **04. DEMAIS INFORMAÇÕES**

Na **Exportação de Produtos (Gerador de Saídas)** os novos campos são gerados em Dados Fiscais do Produto nas posições:

Código Atividade Econômica posição: 134-148

Classificação do Serviço posição: 149 - 158

Na **Importação de Produtos (Conceito)** os novos campos são utilizados em Destino: Produto > ImportacaoProduto.item.DadosFiscais

**Este recurso está disponível a partir da versão 12.1.25.103 da Biblioteca RM. É necessário realizar a importação dos Objetos Gerenciais que contêm os novos campos.IMPORTANTE!**

## **05. ASSUNTOS RELACIONADOS**

* [Importação/Exportação de Produtos](http://tdn.totvs.com.br/pages/releaseview.action?pageId=423938138)

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
