---
content_hash: 95a979b1cc26a0ff1346330a47d7f665659b9ce668fd27bc2fca9691184f17ee
fetched_at: '2026-06-29T00:08:31.963473+00:00'
page_id: '273979036'
product: rm
source: tdn-rm
title: 739155 FINANCEIRO01-166 DT Baixa de Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273979036
version: 108
---

# Baixa de Lançamentos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Baixa de Lançamentos |
| **Situação/Requisito:** | Ao tentar efetuar a baixa de um lançamento que não possui data de previsão de baixa e está parametrizado para que a data de baixa seja a data de previsão de baixa, está ocorrendo erro de "Referência de objeto não definida" |
| **Solução/Implementação:** | Melhoria na baixa de lançamento para que não ocorra erro ao tentar baixar um lançamento que não possui data de previsão de baixa e o parâmetro de data baixa default seja igual data de previsão |
| **Conversores e Parâmetros:** | Parâmetro "Contas a Pagar | Baixa | Manutenção de Baixa | Baixa a Pagar | Data Default da Baixa a Pagar"  Parâmetro "Contas a Receber | Baixa | Manutenção de Baixa | Baixa a Receber | Data Default da Baixa a Receber" |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000040 |

divs
