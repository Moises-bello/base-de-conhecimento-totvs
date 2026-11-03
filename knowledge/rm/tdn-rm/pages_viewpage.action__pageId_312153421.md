---
content_hash: fa2c59ab16532ce0b9fb5ddec9158b23ff2fd38fa3ebbb158ed50fd739434c9a
fetched_at: '2026-06-29T00:08:45.685235+00:00'
page_id: '312153421'
product: rm
source: tdn-rm
title: 1538784 DEDUINTEGRACOES-798 DT Criação de parcelas em contratos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=312153421
version: 94
---

# CRIAÇÃO DE PARCELAS EM CONTRATOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Criação de parcelas em contratos |
| **Situação/Requisito:** | Sistema permitia a inclusão de parcelas para contratos do tipo acordo utilizando o Wizard de criação de parcela. |
| **Solução/Implementação:** | - Implementação de filtro de contratos para não mostrar contratos de acordo no wizard de criação de parcelas do contrato - Acrescentado no server a regra de se gerar Warnings para os contratos de acordo enviados para inclusão de parcelas. Isso pode acontecer via WebServices pois, na tela do processo, os contratos do tipo acordo não estão ficando disponíveis para processamento. - Elaboração de script para exclusão de parcelas de contratos de acordo que não possuem lançamentos gerados. Esse script fará o backup de todos os registros de SRESPONSAVEL e SPARCELA que serão excluídos antes da exclusão. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
