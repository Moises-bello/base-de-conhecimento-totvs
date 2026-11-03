---
content_hash: 252fb4088b1d91df90cf9f05e85d6a975d26a31aae41942b3c6c2dba49b574cd
fetched_at: '2026-06-29T00:08:23.387053+00:00'
page_id: '270083952'
product: rm
source: tdn-rm
title: MEDU-1105_DT_Botoes_Habilitados_Abonar_Descontar_Multa_Item_Sem_Multa
type: documentation
url: https://tdn.totvs.com/display/LRM/MEDU-1105_DT_Botoes_Habilitados_Abonar_Descontar_Multa_Item_Sem_Multa
version: 112
---

# MOVIMENTAÇÕES - ALTERAÇÃO DEVOLUÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Bibliotecária* |
| **Função:** | *Movimentações - alteração de devolução* |
| **Situação/Requisito:** | *Foi identificado que ao realizar uma devolução e alterar uma devolução que não tenha multa, os botões de Abonar e Descontar multa ficam habilitados, mesmo que o empréstimo selecionado não tenha multa.* |
| **Solução/Implementação:** | *Foi identificado que não há validação com relação aos botões, sendo assim foi inserido uma validação para que identifique as devoluções marcadas, se possuem ou não multa e só habilitar os botões e exibir a tela de abono ou desconto se tiver multa para os itens de devolução.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
