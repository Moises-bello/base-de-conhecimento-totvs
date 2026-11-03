---
content_hash: a8053ecc850fcc8c70117780e4f09992740bbbae2e404a4030e8443c9e1118ba
fetched_at: '2026-06-29T00:11:56.473994+00:00'
page_id: '866528969'
product: rm
source: tdn-rm
title: FISCAL01- 23720 - EFD-ICMS/IPI - Registro 0221
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=866528969
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Sped Fiscal |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-23720 |

## **02. SITUAÇÃO/REQUISITO**

O sistema está gerando os registros 0200 e 0221 na ordem incorreta, sem criar a ligação entre registro filho (0200) e registro pai (0221).  
No exemplo abaixo, o sistema gera primeiro todos os registros 0200 e depois gera todos 0221.

## **03. SOLUÇÃO**

Correção na ordenação dos registros 0200 e 0221:

Disponível à partir da biblioteca 12.1.2310
