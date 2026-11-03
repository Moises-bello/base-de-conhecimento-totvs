---
content_hash: dbdb502f9440c4fc6657a1224ab4ef06d17eb0632c8901abd7f0ec8f99bcdf66
fetched_at: '2026-06-29T00:08:37.051256+00:00'
page_id: '284866589'
product: rm
source: tdn-rm
title: 931403 PORTALMOBILE01-754 DT Lançamento de notas de avaliação com fórmula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284866589
version: 100
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Lançamento de notas de avaliação |
| **Situação/Requisito:** | Ao realizar o lançamento de notas de avaliação quando há fórmula, o sistema apresenta inconsistência de chave duplicada. |
| **Solução/Implementação:** | Verificado que a inconsistência ocorria na inclusão do log de notas que tem como chave a data de inclusão. Foi adicionado 1 segundo para cada registro, dessa forma a inconsistência não ocorre. |

divs
