---
content_hash: 18ccccb7bf91e36f23100cdf9f7e96440af48c4c05915d354b87d778db5728a0
fetched_at: '2026-06-29T00:08:33.500109+00:00'
page_id: '274324131'
product: rm
source: tdn-rm
title: 525878 FINANCEIRO01-361 Baixa
type: documentation
url: https://tdn.totvs.com/display/LRM/525878+FINANCEIRO01-361+Baixa
version: 109
---

# Baixa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão Financeira. |
| **Função:** | Baixa |
| **Situação/Requisito:** | Ao baixar dois lançamentos juntos na sessão de caixa, o sistema não permite a alteração dos valores (juros e multa) do segundo registro envolvido na baixa. Caso seja baixado o 2° registro de forma isolada, os valores podem ser alterados normalmente. |
| **Solução/Implementação:** | Ajustado validação de alteração dos valores do lançamento, no formulário de baixa. Desta forma, quando o formulário estiver sendo utilizado pela Sessão de Caixa, irá obedecer as regras pertinentes ao processo. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000040. |

divs
