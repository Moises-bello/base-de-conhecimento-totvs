---
content_hash: a990f71e4073fc081b4e575c199ad23f312d287281391eb38c4f5edb8c4af738
fetched_at: '2026-06-29T00:09:10.514285+00:00'
page_id: '398755468'
product: rm
source: tdn-rm
title: 3601025 FINANCEIRO01-8595 DT Campos de valor indevidos no filtro
type: documentation
url: https://tdn.totvs.com/display/LRM/3601025+FINANCEIRO01-8595+DT+Campos+de+valor+indevidos+no+filtro
version: 1
---

# Ao realizar filtros com campos calculados o sistema apresenta mensagem de erro.

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Filtro na visão de Lançamentos |
| **Situação/Requisito:** | Ao criar um filtro com campos que são cálculos o sistema apresenta mensagem de erro relatando que o campo é inválido. "Invalid Column Name" |
| **Solução/Implementação:** | Removido todos os campos de valores do filtro que são calculados e não salvos no lançamento.  Campos: VALORBASEINSSEMPREGADOR, VALORINSSEMPREGADOR, VALORLIQUIDO, VALORTOTALALGEBRICO |
| **Tickets relacionados:** | 3601025 |
| **Requisito:** | FIN000254 |
