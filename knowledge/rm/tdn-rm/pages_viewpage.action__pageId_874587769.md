---
content_hash: 1ccd42625a5be8c1ce28888697f394c131665c5241ec0f33bc0171c64686dcc9
fetched_at: '2026-06-29T00:11:59.645818+00:00'
page_id: '874587769'
product: rm
source: tdn-rm
title: DT - Processo para aprovar requisição após conclusão do atendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=874587769
version: 2
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Gestão de Pessoas |
| Função: | Integração entre TOTVS Gestão de Pessoas e TOTVS Aprovações e Atendimento |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHHCM-13876](https://jiraproducao.totvs.com.br/browse/DRHHCM-13876 "View this issue") |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2310.261,
* 12.1.2402.233,
* 12.1.2406.161,
* 12.1.2410.101 e superiores.

## **03. SITUAÇÃO/REQUISITO**

A  requisição não é aprovada de forma automática quando o avançar o fluxo é executado pelo TOTVS Aprovações e Atendimento. No TOTVS Aprovações e Atendimento quando é acionado o Avançar o Fluxo é executado somente a fórmula, com isso o status da requisição não é alterado e o parecer não é incluído.

## **04. SOLUÇÃO**

Foi criado o processo **Aprovar Requisição após conclusão do Atendimento** para concluir a requisição (que possui atendimento concluído) e inserir o parecer.

## **05. DEMAIS INFORMAÇÕES**
