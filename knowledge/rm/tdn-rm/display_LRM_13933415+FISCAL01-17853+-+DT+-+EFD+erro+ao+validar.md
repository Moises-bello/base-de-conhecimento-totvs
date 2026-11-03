---
content_hash: c4d657e859fdd101441d057bf49361c476974140eaee71567f311b9f2b224879
fetched_at: '2026-06-29T00:11:17.477947+00:00'
page_id: '680980108'
product: rm
source: tdn-rm
title: 13933415 FISCAL01-17853 - DT - EFD erro ao validar
type: documentation
url: https://tdn.totvs.com/display/LRM/13933415+FISCAL01-17853+-+DT+-+EFD+erro+ao+validar
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD Contribuições |
| País: | Brasil |
| Ticket: | 13933415 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17853 |

## **02. SITUAÇÃO/REQUISITO**

Ao validar a rotina EFD Contribuições, está retornando a mensagem: "CNPJ inválido. Informar no registro 0140 antes de utilizá-lo".  
É gerado o registro D200, porém o registro 0140 não está sendo gerado.

## **03. SOLUÇÃO**

Após a atualização do manual EFD Contribuições, a regra só foi ajustada no registro D200, mas não no 0140. Logo, foi ajustado no layout do gerador de saídas. O registro 0140 passa a gerar o modelo de documento 63.

Disponível a partir da versão 12.1.32
