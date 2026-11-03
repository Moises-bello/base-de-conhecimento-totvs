---
content_hash: 44799c9763bbe7858367972b42f2f8c84a25aaa4b48bf4af64f546701ebccc2a
fetched_at: '2026-06-29T00:09:09.194133+00:00'
page_id: '393347158'
product: rm
source: tdn-rm
title: 3258781 FOPCALCULO01-4341 - TRCT - Campo 63
type: documentation
url: https://tdn.totvs.com/display/LRM/3258781+FOPCALCULO01-4341+-+TRCT+-+Campo+63
version: 1
---

# TRCT

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | TRCT |
| **Situação/Requisito:** | Ao realizar rescisão para funcionária que ficou afastada 120 dias durante o ano corrente, o sistema lança 120 dias no evento código de cálculo 373, processo esse correto, porém ao gerar o relatório TRCT, campo 63, o sistema está retornando 12/12 avos, ao invés de retornar os avos correto, do evento código de cálculo 48.  Como o evento código de cálculo 373 tem a prioridade maior do que o evento código de cálculo 48, o sistema está retornado os dias do evento código de cálculo 373 |
| **Solução/Implementação:** | Ajuste no TRCT de Resilição para não considerar a referência do evento CC373 nos avos do campo 63. |
| **Tickets relacionados:** | 3258781 |
