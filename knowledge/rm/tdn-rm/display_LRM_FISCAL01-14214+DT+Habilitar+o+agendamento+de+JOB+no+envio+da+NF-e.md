---
content_hash: d1f5bca814396575fe03ab0a605742e859619ba93b86b7a83babeafe52a57b89
fetched_at: '2026-06-29T00:10:52.265978+00:00'
page_id: '571525554'
product: rm
source: tdn-rm
title: FISCAL01-14214 DT Habilitar o agendamento de JOB no envio da NF-e
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-14214+DT+Habilitar+o+agendamento+de+JOB+no+envio+da+NF-e
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Envio NF-e |
| Ticket: | - |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14214 |

## **02. SITUAÇÃO/REQUISITO**

O processo de envio da NF-e deve permitir o agendamento de Job.

* O campo data final deve permitir ficar em branco, sendo que o processo irá considerar a data da execução como data Final.
* O processo manual deve continuar sendo executado sem problemas.

## **03. SOLUÇÃO**

Ajustado processo manual de Envio de NF-e permitindo que seja possível o envio das notas sem a obrigatoriedade do preenchimento do campo Data Emissão Final. Caso o campo de Data Emissão Final esteja vazio será considerada a data e hora em que o processo foi executado.

Caso o campo de Data Emissão Final esteja preenchido será considerado a data selecionada.
