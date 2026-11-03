---
content_hash: 1e321abb4379e86c77e4177d8533874d4bf2a8ecd9e6cd44d55353c710be1c4d
fetched_at: '2026-06-29T00:10:15.117687+00:00'
page_id: '463810866'
product: rm
source: tdn-rm
title: DT Controle Orçamentário para Receita
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=463810866
version: 9
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Controle Orçamentário |
| Função: | Orçamento de Receita |
| Ticket: | Não se aplica |
| Requisito/Story/Issue (informe o requisito relacionado) : | [FINANCEIRO01-10158](http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-10158) |

## **02. SITUAÇÃO/REQUISITO**

Hoje apenas os lançamentos A Pagar estavam integrados ao Controle Orçamentário, que controlavam apenas as contas de Despesa do Orçamento. Com o objetivo de ter efeito completo no Orçamento, passaremos a também integrar os lançamentos A Receber, que terão efeito nas contas de Receita do Orçamento.

## **03. SOLUÇÃO**

No parametrizador (Controle Gerencial | Controle Orçamentário | Integração Financeira), passou a determinar ações especificas ao exceder o orçamento. Lançamentos A Pagar incidem sobre as Despesas do Orçamento, e em caso de exceder o orçamento o sistema permite as ações: Barra, Avisa, Bloqueia e Não Avisa. Lançamentos a Receber incidem sobre as Receitas do Orçamento e em caso de exceder o orçamento o sistema permite as ações: Avisa e Não Avisa.

Visando determinar com mais assertividade a Ação determinada pelo campo "Efeito sobre o Orçamento", o novo campo "Afeta Orçamento Para" permitirá escolher uma natureza do lançamento (A Pagar, A Receber, A Pagar e A Receber) que deve afetar o Orçamento. Este campo somente será apresentado quando o o campo "Pagar ou Receber" da aba "Identificação" for "A Pagar ou A Receber".

Ao incluir novo lançamento A Receber, se seu tipo de documento estiver indicado uma ação sobre o orçamento conforme os campos "Efeito sobre o Orçamento" e "Afeta Orçamento Para", ocorrerá um efeito sobre o Orçamento definido no Nucleus. Se houver um excedente no orçamento (ultrapassar o limite estabelecido), e estiver configurado no parametrizador a opção "Avisa" no campo "Ação sobre Lançamento ao Exceder Receita", será apresentado um diálogo informando o efeito, conforme abaixo:

## **04. DEMAIS INFORMAÇÕES**

O efeito sobre o orçamento ocorre na inclusão do lançamento, assim os processos de Alteração Global e Lançamento Padrão também são afetados pelo novo Controle Orçamentário de Receita.

**Os processos de Geração de Acordo e Parcelamento não afetam o orçamento, assim os lançamentos gerados por acordo e os gerados pelo parcelamento, não incidem sobre o Orçamento de Receita .IMPORTANTE!**

## **05. ASSUNTOS RELACIONADOS**

* Módulo de Orçamento do RM Nucleus

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
