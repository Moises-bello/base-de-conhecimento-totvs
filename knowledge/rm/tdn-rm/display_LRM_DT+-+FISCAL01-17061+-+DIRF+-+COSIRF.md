---
content_hash: 5dcb59cb163d5e6669dc1f21bc1b7b7adc1749bec745b459be95b241bca3390c
fetched_at: '2026-06-29T00:11:12.550154+00:00'
page_id: '654714401'
product: rm
source: tdn-rm
title: DT - FISCAL01-17061 - DIRF - COSIRF
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+FISCAL01-17061+-+DIRF+-+COSIRF
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | DIRF |
| País: | Brasil |
| Ticket: | 12900230 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17061 |

## **02. SITUAÇÃO/REQUISITO**

Na Rotina da DIRF não considera Lançamentos de Entrada com CFOP igual a Fiscal, mesmo tendo o Tributo IRRF PJ, COSIRF E CSRF.

Alterar a Rotina da DIRF para considerar todos os Lançamentos de Entrada que tem os Tributos Tributo IRRF PJ, COSIRF E CSRF, independente se o CFOP é Fiscal ou Não Fiscal.

## **03. SOLUÇÃO**

O problema foi resolvido permitindo que o registro seja gerado independente da CFOP do lançamento ser fiscal ou não.

**Disponível a partir da biblioteca 12.1.32**
