---
content_hash: 61ec7e9c7434cf7234ecb8fee94ec0b3ed903bab0a88ab1b366df5b57750f6d2
fetched_at: '2026-06-29T00:11:50.661669+00:00'
page_id: '844262192'
product: rm
source: tdn-rm
title: DT - IRRF RRA - Valor dedutível por dependente e Dedução maior de 65 anos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=844262192
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Diferença Salarial / Diferença 13º salário / Diferença Férias |
| País: | Brasil |
| Ticket: | [Ticket #17880549](https://totvssuporte.zendesk.com/agent/tickets/17880549 "View ticket on the Zendesk portal") |
| Issue: | [DRHCALCRM-5430](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-5430) |

## **02. SITUAÇÃO/REQUISITO**

Cliente informa que identificou divergência referente ao cálculo de IRRF dos RRAs. No cálculo está considerando dedução de dependente, o que é divergente, visto que somente pode ser deduzido INSS e Pensão, conforme IN1500/2014 - ARTIGO 39.

## **03. SOLUÇÃO**

No cálculo do IRRF RRA não será deduzido valores de dependentes e de Maiores de 65 anos, visto que no Art. 39 da IN nº 1.500/2014 é exposto que somente é dedutível para a base de RRA: Pensão Alimentícia e contribuição de INSS.

## **04.** **ASSUNTOS RELACIONADOS**

* [Rendimentos Recebidos Acumuladamente (RRA)](https://tdn.totvs.com/pages/releaseview.action?pageId=715818269#1-4)
