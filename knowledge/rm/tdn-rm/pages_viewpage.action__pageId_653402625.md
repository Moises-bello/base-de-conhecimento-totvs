---
content_hash: a5bb16cff6bbbc2819ed55f16df87e26b0ad6cec3cb72ee7f3d6e0a73f98df83
fetched_at: '2026-06-29T00:11:12.452849+00:00'
page_id: '653402625'
product: rm
source: tdn-rm
title: DT – eSocial - S-2230 -  Não gerar gatilho para afastamentos (P e O) com duração
  inferior ao definido no MOS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=653402625
version: 7
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | S-2230 - Parâmetro "Não gerar gatilho S-2230 para afastamentos (P e O) com duração inferior ao definido no MOS" |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | DRHROTRM-1352 |

## **02. SITUAÇÃO/REQUISITO**

Com a liberação do leiaute S-1.0 o evento S-2230 com data inferior a quinze dias se tornar opcional, seu envio somente é obrigatório caso ocorra no período carência, a soma de mais afastamentos compondo o valor superior a 15 dias.

**03. SOLUÇÃO**

Ao marcar o parâmetro "Não gerar gatilho S-2230 para afastamentos (P e O) com duração inferior ao definido no MOS", o sistema irá gerar o gatilho somente quando o afastamento tiver o prazo superior a 15 dias, ou quando no período de carência a soma de todos os afastamentos compor o valor superior a 15 dias (todos os afastamentos serão enviados neste momento).

## **04. DEMAIS INFORMAÇÕES**
