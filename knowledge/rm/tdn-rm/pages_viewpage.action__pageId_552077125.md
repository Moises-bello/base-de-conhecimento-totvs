---
content_hash: 6836fa41f07abaffea1307da8bdd126a3e5a7b80149aec84a6bf1e5feb495880
fetched_at: '2026-06-29T00:10:44.004351+00:00'
page_id: '552077125'
product: rm
source: tdn-rm
title: 7154278 FISCAL01-11239 DT - Job para Gerar Movimento de NFS-e com o número
  da prefeitura
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=552077125
version: 6
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Gerar Movimento de NFS-e com o número da prefeitura |
| Ticket: | 7154278 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11239 |

## **02. SITUAÇÃO/REQUISITO**

Ao executar o processo de Gerar Movimento com Numero da Prefeitura Automático (Job), sem executar um filtro de tela, o ERP apresenta um erro com a seguinte mensagem: "Movimento fora das datas parametrizadas de movimentação". Foi identificado que o job é executado para todas as notas fiscais autorizadas, com movimento do tipo 2.1.XX e que a movimentação está com Status de 'A Faturar'. Neste caso, o job é executado também para notas com a data de emissão fora do período de movimentação parametrizado, apresentando a inconsistência em questão

## **03. SOLUÇÃO**

O Job responsável por gerar movimentos 2.2.xx a partir de Notas autorizadas no movimento 2.1.xx foi modificado para ser executado somente para movimentos dentro do período de movimentação definido nos parâmetros gerais do Módulo de Faturamento e apenas para a coligada corrente

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
