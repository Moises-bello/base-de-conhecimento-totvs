---
content_hash: 2ccf7a801fe2dffa7adadc74af084e7f132eac42f8b33a0e105acfbe1bcb3658
fetched_at: '2026-06-29T00:08:31.058470+00:00'
page_id: '272715006'
product: rm
source: tdn-rm
title: 575799 EDUCACIONAL01-34 DT Integração com nucleus o movimento não aparece
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272715006
version: 110
---

# Geração de Movimento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Geração de Movimento |
| **Situação/Requisito:** | O lookup que lista os movimentos que podem ser utilizados na geração de nota do educacional não estava listando algum movimentos que deveriam ser apresentados.    Identificamos que o campo "NF-e Estadual" parametrizado no tipo de movimento (etapa 67 ) quando esta parametrizado diferente de "Não Integrado" não estava sendo levado em consideração. |
| **Solução/Implementação:** | Melhoria no processo de geração de movimento para que sejam listado os movimentos em que o campo  "NF-e Estadual" (Etapa 67) esteja configurado como a opção diferente de "Não integrado".  Segue abaixo a regra para que os tipos de movimentos sejam apresentados no educacional:    - Tipos de movimento que o código comece com 2.1 ou 2.2  - As parametrizações do tipo de movimento definidas na etapa 67 devem estar:    NFS-e Municipal ou NF-e Estadual ou NFC-e --> For diferente de não integrado ou  NFS-e Municipal e NF-e Estadual e NFC-e --> Sejam igual a não integrado |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** | 575799 |
| **Requisito:** |  |

divs
