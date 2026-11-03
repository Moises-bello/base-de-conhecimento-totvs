---
content_hash: edf513488d6feeccbcc4dd0de11e482aceaee660ea8387a64fa4d9ecf532ce94
fetched_at: '2026-06-29T00:11:21.276696+00:00'
page_id: '691453950'
product: rm
source: tdn-rm
title: DT - Rescisão Intermitente -  Multa 40%
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=691453950
version: 6
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | Plataforma RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Rescisão |
| País: | Brasil |
| Ticket: | [13642547](https://totvssuporte.zendesk.com/agent/tickets/13642547 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-2014](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-2014) |

## **02. SITUAÇÃO/REQUISITO**

Ao realizar a rescisão de um funcionário intermitente com o tipo 2 - Iniciativa do Empregador sem justa causa, esta sendo calculado a multa de FGTS (CC28) com 20%, sendo que o correto seria 40%.

## **03. SOLUÇÃO**

Atualização da Legislação de funcionário intermitente para retorno da multa de FGTS para 40% no caso de demissão sem justa causa.

Rescisão Tipo 2 - Sem justa Causa, Rescisão Tipo V - Comum Acordo, Passo 03, Passo 04passo1,passo2

Cadastro do Funcionário:

yespasso1

Após o cálculo da rescisão, o evento de CC28 considerou a aliquota de 40%:

No Lançamento Financeiro também foi considerado a aliquota de 40%:

Retorno da GRFC:

nopasso2

Após o cálculo da rescisão, o evento de CC28 considerou a aliquota de 20%:

Lançamento Financeiro também foi considerado a aliquota de 20%:

Retorno da GRFC:
