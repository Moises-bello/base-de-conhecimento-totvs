---
content_hash: d987964fecc8f505ff9dcb01c6f56668381ea6f840300a73d1a27d348165050f
fetched_at: '2026-06-29T00:08:30.982430+00:00'
page_id: '272709575'
product: rm
source: tdn-rm
title: 691377 FINANCEIRO01-88 DT VALORCHEQUE
type: documentation
url: https://tdn.totvs.com/display/LRM/691377+FINANCEIRO01-88+DT+VALORCHEQUE
version: 106
---

# Ao emitir cheque parcial o sistema salva o campo FLAN.VALORCHEQUE incorretamente.

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Emissão/Recebimento de Cheque |
| **Situação/Requisito:** | Ao incluir vários cheques parciais para o mesmo lançamento o sistema está somando o campo VALORCHEQUE com o VALORCHEQUE já existe mais o novo cheque está sendo emitido. Desta forma ao tentar salvar um cheque o sistema estourou o tamanho do campo no SQL. |
| **Solução/Implementação:** | Otimizado o sistema para guardar corretamente o valor do cheque no lançamento. Gerado script corretivo para os lançamentos na base do cliente. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | FINANCEIRO01-88 FINANCEIRO01-100 |
| **Requisito:** | FIN000156 |

divs
