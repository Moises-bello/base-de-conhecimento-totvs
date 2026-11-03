---
content_hash: 63f9b31f0a0a6d6033856d93d52554ec6aa16ac005ef3968ec4797e319d9107c
fetched_at: '2026-06-29T00:11:13.387881+00:00'
page_id: '660109382'
product: rm
source: tdn-rm
title: FISCAL01-17320 - DT - FUNRURAL - Alterar o processo de geração de Guias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=660109382
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Geração de Guias Automaticamente |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17320 |

## **02. SITUAÇÃO/REQUISITO**

No Período de Apuração:

Iremos evoluir o processo de geração de guias automaticamente para considerar os Lançamentos Fiscais de Saída no caso do Tributo FUNRURAL.

O processo deverá somar os valores de entrada com os valores de saídas encontrados nos Lançamentos Fiscais. Contudo, deve ser respeitado o parâmetro do Fiscal sobre gerar as guias centralizadas ou por nota.

## **03. SOLUÇÃO**

No Período de apuração do FUNRURAL, Lançamentos de saída também serão considerados no processo "Geração de Guias Automaticamente", acrescendo o valor do Saldo Credor/Devedor.
