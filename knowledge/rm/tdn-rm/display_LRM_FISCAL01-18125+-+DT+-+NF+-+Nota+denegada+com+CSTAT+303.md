---
content_hash: 42c6e66326ae3068d1d46f15cc0aa232824c364f774800b536ca9cc7a9a6d5de
fetched_at: '2026-06-29T00:11:21.234087+00:00'
page_id: '689866515'
product: rm
source: tdn-rm
title: FISCAL01-18125 - DT - NF - Nota denegada com CSTAT 303
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-18125+-+DT+-+NF+-+Nota+denegada+com+CSTAT+303
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Documentos eletrônicos - NF-e |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17998 |

## **02. SITUAÇÃO/REQUISITO**

Ausência do código 303 para notas denegadas;  
O serviço de cancelamento de movimento não era consumido quando o status da nota era Denegada.

## **03. SOLUÇÃO**

1 - Adição do código 303 no método que verifica se a nota é denegada;

2 - Tags xml que poderiam ser vazias antes da função de cancelar o movimento foram tratadas, para apenas retornar um valor caso a tag exista. Isso estava quebrando o código antes do cancelamento do movimento ser chamado.

Disponível a partir da versão 12.1.34
