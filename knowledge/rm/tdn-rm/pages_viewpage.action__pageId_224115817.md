---
content_hash: 47e755bb11b80310e0ea0e396e88e6ed609d3c66988cdcea2f09ceb86d7451a9
fetched_at: '2026-06-29T00:06:24.282363+00:00'
page_id: '224115817'
product: rm
source: tdn-rm
title: TTKDDB_DT_Contagem_Item_Inventário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224115817
version: 124
---

# INVENTÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *NUCLEUS* |
| **Função:** | *Inventário* |
| **Situação/Requisito:** | Data/hora da contagem do inventário carrega a data e hora do momento em que o inventário é salvo, e não a data e hora que o campo foi preenchido, como era feito no delphi |
| **Solução/Implementação:** | *O sistema passou a salvar a data e tempo (horas, minutos e segundos) quando a contagem é informada.*  *Para a data ser salva, o usuário precisa inserir a contagem e pressionar a tecla TAB. Caso o usuário inserir o mesmo valor a data não é alterada.*  *No grid dos itens do inventário também é possível informar a contagem e a data será atualizada*  *O valor somente será salvo no banco de dados quando o inventário for salvo.* |
| Versão: | 12.1.10 |

divs
