---
content_hash: 7447c1b215567ba9c1efa1008f5dc0a0dbebe15de962492bda14b477f5810e7e
fetched_at: '2026-06-29T00:09:00.964234+00:00'
page_id: '370613381'
product: rm
source: tdn-rm
title: 2601509 CONTROLADORIA01-1298 DT Arredondamento Integração Aquisição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=370613381
version: 2
---

# Integrar Aquisições Compras

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Totvs Gestão Patrimonial |
| **Função:** | Integrar aquisições de compras |
| **Situação/Requisito:** | Ao realizar a integração de patrimônios, marcado a opção "Incluir patrimônio mantendo as quantidades informadas nos itens da nota", a quantidade fracionada está sendo arredonda (0,75 está ´sendo arredondando para 1). |
| **Solução/Implementação:** | O processo de integração de aquisições de compras foi alterado para que, ao marcar a opção "Incluir patrimônio mantendo as quantidades informadas nos itens da nota", a quantidade fracionada seja mantida.  Ex: Se o item da nota possuir quantidade igual a 0,75 então o patrimônio integrado deverá possuir quantidade igual a 0,75.  Caso o usuário deseje arredondar as quantidades inferiores a 1 será necessário marcar a nova opção que foi adicionada na tela de processo, "Arredondar quantidade dos itens caso ela seja inferior a um". Vale ressaltar que ela só ficará habilitada se a opção "Incluir patrimônio mantendo as quantidades informadas nos itens da nota" estiver marcada.  Ex: Se o item da nota possuir quantidade igual a 0,75 então o patrimônio integrado deverá possuir quantidade igual a 1. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |
| **Documento de Referência:** | N/A. |
