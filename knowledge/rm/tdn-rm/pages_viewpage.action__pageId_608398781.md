---
content_hash: 97d9706f83b793b1b698fa3a04f22d1628135f1becf0bc2172a6d2160a92a678
fetched_at: '2026-06-29T00:10:59.019183+00:00'
page_id: '608398781'
product: rm
source: tdn-rm
title: 'FISCAL01-15130 - DT Relatório ADRC-ST: Registro 1200'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=608398781
version: 1
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

Construir uma consulta SQL Anexa no período de apuração ICMSST para exibir os Lançamentos Fiscais do período que serão considerados na ADRC-ST nos registros 1210 e 1220

## **03. SOLUÇÃO**

Criação das consultas disponíveis em ...ObjetosGerenciais\SQL

**FISSQLANEX0002 - ADRC-ST - Registro 1210.TotvsConsSQLAnex**

**FISSQLANEX0003 - ADRC-ST - Registro 1220.TotvsConsSQLAnex**

As mesmas devem ser anexadas ao período de apuração.

Obs: Devido a limitação da consulta, inicialmente os campos 13, 14 e 15 não serão demonstrados.
