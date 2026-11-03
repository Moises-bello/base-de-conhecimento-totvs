---
content_hash: 77c91e3fb016fb1a6e1a647b89e63b4fbafaacdb935b3a11b0ea7503fa09f6da
fetched_at: '2026-06-29T00:09:38.771659+00:00'
page_id: '431664029'
product: rm
source: tdn-rm
title: 4118175 FISCAL01-6966 DT Escrituração Fiscal - Escrituração Fiscal Erro no
  campo de desconto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=431664029
version: 1
---

# Escrituração de Lançamentos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Escrituração de Lançamentos |
| **Situação/Requisito:** | Ao escriturar um Movimento que possui desconto em um item e este desconto não afeta o movimento, este desconto está indo negativamente para um item de outra situação tributária. |
| **Solução/Implementação:** | A rotina de escrituração estava, erroneamente, considerando o desconto total das Situações Tributárias para ajuste do último item, comparando com o desconto existente no Movimento. Como não existe desconto no Movimento (somente no item), ao efetuar essa comparação estava ficando negativa e este valor sendo atribuído ao último item do Lançamento Fiscal. |
| **Requisito:** | FIS000236 |
