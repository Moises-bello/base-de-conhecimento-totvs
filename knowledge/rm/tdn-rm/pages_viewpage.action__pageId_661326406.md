---
content_hash: a2281281d18fd97f012efefe331b61d3603a37c696faa817597f8d5ad85c9fdd
fetched_at: '2026-06-29T00:11:13.505919+00:00'
page_id: '661326406'
product: rm
source: tdn-rm
title: 'FISCAL01-17354 - DT - R-2060: Alterar a Descrição do Ajuste'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=661326406
version: 3
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
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17354 |

## **02. SITUAÇÃO/REQUISITO**

No xml do evento r2060, a tag <**descAjuste>** é preenchida conforme uma padrão nosso. Ex: Lan.Fiscal:000008987**.** Porém o cliente deseja mudar esse padrão para uma maneira personalizável.

## **03. SOLUÇÃO**

Ajuste no Evento R2060 - Descrição Código de Ajuste:

Pode ser preenchido de acordo com o campo complementar: DESCCODAJUSTE. Caso o cliente não possua tal campo, o preenchimento será pelo número do documento do lançamento fiscal (forma padrão).
