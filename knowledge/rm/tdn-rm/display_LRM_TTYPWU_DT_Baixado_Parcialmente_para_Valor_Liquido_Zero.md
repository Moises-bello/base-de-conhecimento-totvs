---
content_hash: 343e09accc7604f7fa9761cbe31ec5d5e6dc100a44c97bfa3b2f5dc8900a2c1e
fetched_at: '2026-06-29T00:06:23.119457+00:00'
page_id: '223933450'
product: rm
source: tdn-rm
title: TTYPWU_DT_Baixado_Parcialmente_para_Valor_Liquido_Zero
type: documentation
url: https://tdn.totvs.com/display/LRM/TTYPWU_DT_Baixado_Parcialmente_para_Valor_Liquido_Zero
version: 122
---

# GERAR CONTABILIZAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Totvs Gestão Educacional |
| **Função:** | Gerar Lançamento |
| **Situação/Requisito:** | Ao gerar lançamento, o status ficava incorretamente com "Baixado Parcialmente" quando a parcela tinha bolsa 100%, multa por atraso e está marcado o parâmetro "Baixar automaticamente lançamentos com valor liquido zero". |
| **Solução/Implementação:** | Otimizado processo de "Gerar Lançamento", quando o mesmo possui multa por atraso, e está marcado o parâmetro "Baixar automaticamente lançamentos com valor liquido zero". O sistema deverá gerar o lançamento com status "Em aberto" quando seu valor liquido não é zero devido à multa. |
| **Conversores e Parâmetros:** | *NA* |
| **Chamados relacionados:** | *NA* |
| **Requisito (ISSUE):** | *NA* |
| **Versões/Release:** | *12.1.10* |
| **Versão Corrigida:** | *12.1.10* |
| **Versão Expedida:** | *12.1.10* |

divs
