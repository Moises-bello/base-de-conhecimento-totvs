---
content_hash: bfa1f90e1695737b82996b379469c47d9d8d91016937c7835c0838451d6521fb
fetched_at: '2026-06-29T00:11:17.440309+00:00'
page_id: '680243817'
product: rm
source: tdn-rm
title: FISCAL01-17792 - DT - Ajuste na Escrituração do Campo Data Vencimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=680243817
version: 4
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD-REINF |
| País: | Brasil |
| Ticket: | [13787041](https://totvssuporte.zendesk.com/agent/tickets/13787041 "Visualizar o Ticket no portal do Zendesk"), [12583948](https://totvssuporte.zendesk.com/agent/tickets/12583948 "Visualizar o Ticket no portal do Zendesk") |
| Requisito/Story/Issue (informe o requisito relacionado) : | [FISCAL01-16729](https://jiraproducao.totvs.com.br/browse/FISCAL01-16729 "Escrituração - Aba Dados Financeiro "), [FISCAL01-17671](https://jiraproducao.totvs.com.br/browse/FISCAL01-17671 "Re: Data de Vencimento - escrituração") |

## **02. SITUAÇÃO/REQUISITO**

* Ao escriturar movimentos de entrada, produto e/ou serviço para o TOTVS Gestão Fiscal a aba lançamento fiscal | Integrações | Dados Financeiro o campo **data previsão de baixa** não é preenchido ([FISCAL01-16729](https://jiraproducao.totvs.com.br/browse/FISCAL01-16729 "Escrituração - Aba Dados Financeiro ")). Vamos passar a escriturar esta data para todos os Movimentos com COSIRF.
* Ao escriturar notas de importação o campo Data Vencimento não é preenchido ([FISCAL01-17671](https://jiraproducao.totvs.com.br/browse/FISCAL01-17671 "Re: Data de Vencimento - escrituração")).

## **03. SOLUÇÃO**

1. Para naturezas que se iniciam com 3 e 7;

* Se não existe lançamento financeiro: Data Vencimento recebe por padrão a Data de Emissão do movimento.
* Se existe lançamento financeiro: Data Vencimento recebe a **menor** data de vencimento dos lançamentos financeiros.

       2. COSIRF

* Somente entrará na regra se existir lançamento financeiro para o tributo.

* + Irá preencher o campo Data previsão baixa do lançamento fiscal de acordo com a menor data de previsão de baixa do lançamento financeiro vinculado ao movimento.
  + Obs.: O mesmo deve estar preenchido.

Disponível a partir da 12.1.34
