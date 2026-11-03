---
content_hash: 14e115f587dd764823f94cd8cc4203507ae4aaabdddb68f9cae9858292950585
fetched_at: '2026-06-29T00:10:37.159266+00:00'
page_id: '536714378'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-6772 DT Preenchimento da data de competência no lançamento
  de devolução de crédito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=536714378
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Educacional |
| Função: | Bolsa retroativa - Novo modelo |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : |  |

## **02. SITUAÇÃO/REQUISITO**

O cliente tem a necessidade de que se seja registrado o mês de competência do lançamento de crédito gerado pela inclusão de uma bolsa retroativa, através do novo modelo.

## **03. SOLUÇÃO**

O processo de inclusão/exclusão de bolsas retroativas foi ajustado para que seja possível a inclusão do mês de competência para o lançamento de devolução de crédito criado para o pagamento de valores pagos pelo responsável financeiro do aluno.

A aba "*Valores opcionais*" teve seu nome alterado para "*Dados adicionais*" e junto a ela foi incorporado o campo "*Mês de competência*" para definição do mês de competência dos lançamentos de devoluções de crédito.

A fim de dar uma flexibilização na inclusão do mês de competência, foi incluso um parâmetro para a definição do comportamento do processo para a inclusão da informação nos lançamentos de devoluções de crédito criados.

Através da aba "*Competência*", nos parâmetros da bolsa retroativa 2/3, foi incluso um parâmetro que permitirá a definição do comportamento do processo de inclusão de bolsa retroativa no preenchimento do mês de competência do lançamento de devolução de crédito.

Serão disponibilizadas as seguintes opções:

* **"Preenchimento no processo (Obrigatório)"**
  + *Essa opção fará com que o campo seja de preenchimento obrigatório durante o processo de inclusão/exclusão de bolsa de retroativa, mas somente na inclusão irá solicitar o preenchimento;*

* **"Preenchimento no processo (Opcional)"**
  + *Essa opção permitirá que o campo seja opcional durante a execução do processo e caso não seja preenchido, o lançamento será criado sem o mês de competência;*

* **"Preenchimento no processo, senão copia do vencimento do lançamento"**
  + *Essa opção permitirá que o campo seja opcional durante a execução do processo e caso não seja preenchido, o mês de competência será preenchido com o mês da data de vencimento do lançamento;*

* **"Preencher conforme a data de vencimento do lançamento"**
  + *Essa opção definirá que o mês de competência sempre será preenchido com o mês da data de vencimento do lançamento de devolução de crédito;*

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
