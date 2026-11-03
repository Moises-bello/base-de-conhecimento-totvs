---
content_hash: 076d3d5b4cbb39565a99a4ea9811bfeda1b27772d67b6c913b5a2188547390a1
fetched_at: '2026-06-29T00:11:10.110095+00:00'
page_id: '641450115'
product: rm
source: tdn-rm
title: DT 12440352 FISCAL01-16608 - Tipo do Frete - SPED ICMS/IPI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=641450115
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED |
| País: | Brasil |
| Ticket: | 12440352 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16608 |

## **02. SITUAÇÃO/REQUISITO**

INTERPRETAÇÃO DA DEMANDA

Ao gerar o Sped Fiscal, o campo 17, que se refere ao Indicativo de Frete, está gerando com o valor 3, mas o aceito pelo PVA são apenas os valores 0, 1, 2 e 9.

Com isso, ao validar o arquivo, ocorre inconsistência dizendo que o valor 3 não é um valor válido.

TESTES REALIZADOS

Em base exemplo foi incluída uma nota de CT-e, e na aba Identificação do Lançamento, foi informado o frete como "Próprio Remetente", conforme cenário do cliente.

Ao gerar o Sped, o campo 17 gerou como 3, e o correto seria gerar como 1.

## **03. SOLUÇÃO.**

Ajuste no registro D100 campo 17. Tipo frete Próprio Remetente deve gerar código 1.

Conforme Manual:
