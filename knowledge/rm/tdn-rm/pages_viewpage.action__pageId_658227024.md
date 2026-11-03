---
content_hash: b0e7b51ca438bdcd10cfef6596d94ece8e0f0e698ad917ee48a413d667e72bac
fetched_at: '2026-06-29T00:11:13.184640+00:00'
page_id: '658227024'
product: rm
source: tdn-rm
title: FISCAL01-17203 DT - NF-e - Envio de Email Automático - Gravar o e-mail que
  foi enviado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=658227024
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Consulta NFe |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17203 |

## **02. SITUAÇÃO/REQUISITO**

Quando parametrizado para envio de Email automático o sistema apresenta somente a mensagem:

"Sucesso em enviar NF-e por email."

Porém se enviar o email pelo processo manual o sistema apresenta a mensagem para qual email foi enviado conforme exemplo abaixo:

Enviar XML por e-mail: O e-mail foi enviado para o endereço (email.mail@[totvs.com.br](http://totvs.com.br)) com sucesso.

Cliente deseja o mesmo comportamento para o envio de email automático.

## **03. SOLUÇÃO**

Implementação feita conforme situação do requisito, e-mail do destinatário também é gravado no histórico da NF-e no envio automático em ambiente de produção.
