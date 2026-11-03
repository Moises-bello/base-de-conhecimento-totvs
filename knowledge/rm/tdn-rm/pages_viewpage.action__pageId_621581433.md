---
content_hash: 45f4d8cfdd3894ad77f2e2387c69190372f82a4943b041a81c7a5b5b2be9a8cb
fetched_at: '2026-06-29T00:11:03.380942+00:00'
page_id: '621581433'
product: rm
source: tdn-rm
title: 'FISCAL01-15379 - DT Relatório ADRC-ST: Registro 1100'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=621581433
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS BackOffice |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15130 |

## **02. SITUAÇÃO/REQUISITO**

Construir uma consulta SQL Anexa no período de apuração ICMSST para exibir os Lançamentos Fiscais do período que serão considerados na ADRC-ST nos registros 1110 e 1120

## **03. SOLUÇÃO**

Criação das consultas disponíveis em ...ObjetosGerenciais\SQL

**FISSQLANEX0021 - ADRC-ST - Registro 1110.TotvsConsSQLAnex**

**FISSQLANEX0022 - ADRC-ST - Registro 1120.TotvsConsSQLAnex**

As mesmas devem ser anexadas ao período de apuração.

Obs: Devido a limitação da consulta, inicialmente os campos 13, 14, 15 e 16 não serão demonstrados.
