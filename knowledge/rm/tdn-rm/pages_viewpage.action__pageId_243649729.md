---
content_hash: 254d93e61d27017e7bc64cd37cd1d1de1648ae64197798de82729bee74eae278
fetched_at: '2026-06-29T00:08:12.801111+00:00'
page_id: '243649729'
product: rm
source: tdn-rm
title: TVDQQ9_DT_Lançamento_Parcelamento_de_Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243649729
version: 116
---

# Lançamento - Parcelamento de Lançamentos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Financeira |
| **Função:** | Lançamento - Parcelamento de Lançamentos |
| **Situação/Requisito:** | Erro "startIndex não pode ser maior que o comprimento da cadeia de caracteres." ao informar mais de 9 parcelas no processo de parcelamento de lançamentos. |
| **Solução/Implementação:** | Otimização do processo para não acontecer o erro quando o número de documento possuir apenas 1 dígito ou o parâmetro "Completar número de documento com zeros" não estiver ativo. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | FIN000085 |

divs
