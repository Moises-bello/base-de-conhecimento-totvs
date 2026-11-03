---
content_hash: 6df41dde977f02a31e0f5f7cd1fc559964c9ec2a38b7a7b4dccb7e08e9332d9c
fetched_at: '2026-06-29T00:10:37.053634+00:00'
page_id: '533755634'
product: rm
source: tdn-rm
title: DT - Inativar condição de pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=533755634
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão de Estoque, compras e faturamento |
| Função: |  |
| Ticket: | 8193773 |
| Requisito/Story/Issue (informe o requisito relacionado) : | MATFATCMPCRM01-10622 |

## **02. SITUAÇÃO/REQUISITO**

Sistema não deve permitir inativar condições de pagamento caso existam movimentos pendentes.

## **03. SOLUÇÃO**

Foi criada uma consistência ao inativar condições de pagamento utilizadas em movimentos que ainda podem ser faturados.

* É verificado movimentos que estão parametrizados para "Gerar Movimento" com status diferente de "Faturado" e "Cancelado".
  + Localização do parâmetro "Gerar Movimento" → Etapa 'Compra/Venda - Características' → 'Gera Movimento de Compra'.

* ***Observação***:

  Ao inativar uma condição de pagamento (por tela), se houver movimentações pendentes o usuário será alertado podendo ver a quantidade de movimentos pendente e listar movimentos.

  Ao inativar uma condição de pagamento (por DataServer), se houver movimentações pendentes o usuário vai ser alertado e informado sobre a quantidade de movimentos pendentes.

  Os movimentos já incluídos com a condição de pagamento inativa não serão afetados, continuarão a apresentar a condição de pagamento. Mas se este movimento for editado e a condição de pagamento for modificada não será possível selecioná-la novamente.

Passo 01, Passo 02, Passo 03, Passo 04passo1,passo2yespasso1

1. Use quando for necessário descrever um passo a passo.

nopasso2

2. Use quando for necessário descrever um passo a passo.

## **04. DEMAIS INFORMAÇÕES**

Outras ações/ações relacionadas 

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
