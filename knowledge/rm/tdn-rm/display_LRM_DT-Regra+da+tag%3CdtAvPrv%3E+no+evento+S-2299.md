---
content_hash: d6c2e6341f48937d429958d6e7a5ff54bc06b0ab917378871a86be06a6305015
fetched_at: '2026-06-29T00:11:06.845214+00:00'
page_id: '635565748'
product: rm
source: tdn-rm
title: DT-Regra da tag<dtAvPrv> no evento S-2299
type: documentation
url: https://tdn.totvs.com/display/LRM/DT-Regra+da+tag%3CdtAvPrv%3E+no+evento+S-2299
version: 10
---

## ****01. DADOS GERAIS****

Linha RM​

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - Evento -S2299 |
| Função: |  |
| País: | Brasil |
| Ticket: | 12244776 |
| Requisito/Story/Issue (informe o requisito relacionado) : | DRHROTRM-1208 |

## **02. SITUAÇÃO/REQUISITO**

Para o eSocial no layout simplificado, a data do aviso prévio no evento S-2299, deve ser menor ou igual a data de demissão.  
Em alguns casos, como por exemplo quando o funcionário possui aviso indenizado, preenchíamos o campo com a data posterior a data de demissão. Esse fato estava gerando erro ao enviar a demissão ao governo.

**03. SOLUÇÃO**

 Ajuste na Tag<dtAvPrv> do evento S-2299 que será preenchida somente quando o aviso prévio for trabalhado ou misto.

Quando o aviso prévio for misto, será considerada a data de inicio do aviso trabalhado.
