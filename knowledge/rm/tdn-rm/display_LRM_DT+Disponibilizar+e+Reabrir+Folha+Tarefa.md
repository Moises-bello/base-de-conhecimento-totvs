---
content_hash: 2ae2e094be03078c4f515365b74a4c0824d3562882a5e3556e6a2a40a3609567
fetched_at: '2026-06-29T00:10:27.036394+00:00'
page_id: '516197122'
product: rm
source: tdn-rm
title: DT Disponibilizar e Reabrir Folha Tarefa
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Disponibilizar+e+Reabrir+Folha+Tarefa
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Construção e Projetos |
| Módulo: | Gestão de Obras e Projetos |
| Função: | Disponibilizar Folha Tarefa para apontamentos  Retornar Folha Tarefa para Em Processamento |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | [TOPORCAPLAN001-8676](https://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-8676) |

## **02. SITUAÇÃO/REQUISITO**

Necessidade de unificar a disponibilização das Folha Tarefas com tipos de apontamentos Manual e Coletor Móvel.

Necessidade de fazer com que a Folha Tarefa possa retorna para o status de "Em Processamento" .

## **03. SOLUÇÃO**

O processo de "Disponibilizar para envio" que faz com que as Folhas Tarefas que tenham o tipo de apontamento definido como "Coletor Móvel" estejam disponíveis para serem associadas ao coletor passa a se chamar "**Disponibilizar Folha Tarefa para Apontamentos**", pois, sua execução passa a permitir com que Folhas Tarefas com o tipo de apontamento "Manual" possam ter o seu status alterado para "Pronto para Impressão", função que era utilizada na tela de edição de Folha Tarefa e não mais está presente.

Consistências:

* Folha Manual:

  + Se existe tarefa associada;
* Todas as Folhas:

  + Se o status for diferente de em processamento;
  + Se o tipo de apontamento é avulso;
  + Se o tipo de apontamento é coletor e não possui coletor associado;
  + Se o parâmetro de projeto "Considerar saldo da tarefa no Avanço Físico" estiver marcado;

    - Valida se a tarefa da folha já está em uma outra folha em andamento;
    - Valida se a quantidade planejada é zero;
    - Valida se a quantidade planejada é maior que o saldo da tarefa.

Através do processo de "**Retornar Folha Tarefa para Em Processamento**" é possível fazer com que a Folha Tarefa possa ser replanejada para uma possível disponibilização.

Consistências:

* Folhas não podem ter apontamentos em suas tarefas;
* Folhas com status que não permitem replanejar:

  + Em processamento;
  + Apontada;
  + Encerrada;
  + Cancelada.

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
]]>
