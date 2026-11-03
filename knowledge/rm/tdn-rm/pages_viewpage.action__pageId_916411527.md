---
content_hash: 97c48433838ee3d9dc27801ff1880a40f8667e81beed4a5b49488d5c1d9c7c2d
fetched_at: '2026-06-29T00:12:06.866827+00:00'
page_id: '916411527'
product: rm
source: tdn-rm
title: FISCAL01-25165 - DT - Encerramento de Período de Apuração ICMS com DIFAL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=916411527
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Período de Apuração |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-25165 |

## **02. SITUAÇÃO/REQUISITO**

Ao encerrar o período de apuração de ICMS com o cálculo do diferencial de alíquota ativado, uma mensagem de erro de SQL era exibida.

O erro se dava pois era feita uma tentativa de gravar um registro do DIFAL para um mesmo estado duas vezes, um referente ao remetente e o outro ao destinatário.

O cálculo considerava apenas o estado gravado no lançamento na escrituração na coluna DLAF.CODETD.

## **03. SOLUÇÃO**

Quando o estado do remetente é igual ao destinatário no lançamento, se este estiver usando uma natureza interestadual, uma nova mensagem de erro será lançada impedindo o encerramento do período.

Foi alterada a forma de seleção do estado remetente do lançamento para o cálculo do DIFAL, considerando agora as colunas DLAFTRANSP.CODETDENTREGA e ORIGEMDESTINO.CODETD e por último o DLAF.CODETD.

Disponível a partir da biblioteca 12.1.2402
