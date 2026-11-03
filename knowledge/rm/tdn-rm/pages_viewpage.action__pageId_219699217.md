---
content_hash: bb6d524a1bae84a11327ff290e0ae2ee3fa7e2ea009b274ebcf818cb460727e2
fetched_at: '2026-06-29T00:06:19.567463+00:00'
page_id: '219699217'
product: rm
source: tdn-rm
title: TTRZ29_DT_Histórico_Assistência_Saúde_Registro_Negativo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=219699217
version: 2
---

# DIRF/Informe de Rendimentos

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *DIRF/Informe de Rendimentos* |
| **Situação/Requisito:** | No histórico de assistência à saúde aceita colocar valor negativo. Quando é gerado a DIRF em .net não é considerado o valor do desconto e assistência à Saúde do dependente. Em delphi é subtraído, porém é somado no valor de desconto do titular. |
| **Solução/Implementação:** | *Alterado o comportamento da DIRF .Net para que seja retirado o valor do dependente e considerado no valor do titular.* |
| **Chamados relacionados:** | *TTRZ29* |
| **Versões/Release:** | *11.82.43* |

divs
