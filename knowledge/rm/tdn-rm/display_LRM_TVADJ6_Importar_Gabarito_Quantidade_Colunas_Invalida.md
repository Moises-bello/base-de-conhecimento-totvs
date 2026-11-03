---
content_hash: e0eb17847df260a6fab1f81a160cb8c0b119c1e6bc5d9aecd5d6d2b2f718d345
fetched_at: '2026-06-29T00:08:09.836446+00:00'
page_id: '240289108'
product: rm
source: tdn-rm
title: TVADJ6_Importar_Gabarito_Quantidade_Colunas_Invalida
type: documentation
url: https://tdn.totvs.com/display/LRM/TVADJ6_Importar_Gabarito_Quantidade_Colunas_Invalida
version: 112
---

# IMPORTAR GABARITOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Importar gabarito* |
| **Situação/Requisito:** | *Ao tentar importar um gabarito com mais ou menos colunas que o definido no layout, o sistema tenta fazer a importação sem alertar nada para o usuário, por exemplor, a prova de redação só permite duas notas, o cliente tentou importar com 3 notas, as duas primeiras foram importadas corretamente e a terceira prova ficou com nota zerada, só que o layout definido do sistema só permite duas notas.* |
| **Solução/Implementação:** | *Foi inserido uma mensagem de alerta caso o arquivo não possua o número de colunas corretos.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
