---
content_hash: d510055ec90a4f227b4960a2381f0417e25f68b846d87116ac43d2b1639e54c1
fetched_at: '2026-06-29T00:12:13.339634+00:00'
page_id: '954073868'
product: rm
source: tdn-rm
title: FISCAL01-25881 - NFE - Problema com envio de XML por e-mail
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-25881+-+NFE+-+Problema+com+envio+de+XML+por+e-mail
version: 1
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão de Estoque, Compras e Faturamento |
| Função: | Envio de XML por e-mail |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-25881 |

## **02. SITUAÇÃO/REQUISITO**

No processo de envio de XML/Danfe por e-mail está sendo retornada mensagem de erro no envio, porém a mensagem não é clara com relação ao erro apresentado.

## **03. SOLUÇÃO**

Ajuste para retornar log de erros no envio do XML por e-mail.   
O erro acontecia porque a coligada do cliente não estava com o campo e-mail preenchido em seu cadastro.

Disponível à partir da biblioteca 12.1.2410
