---
content_hash: 1ad46b1f1fd6bb0ca29f30559a722bb96e7c280214ab5214a4fbb769427d2ad1
fetched_at: '2026-06-29T00:08:12.822879+00:00'
page_id: '243650744'
product: rm
source: tdn-rm
title: TVCKO0_DT_Quadro_Horarios_Todos_Vazio
type: documentation
url: https://tdn.totvs.com/display/LRM/TVCKO0_DT_Quadro_Horarios_Todos_Vazio
version: 116
---

# QUADRO DE HORÁRIOS - PROFESSOR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Quadro de horários - Professor - Portal* |
| **Situação/Requisito:** | *Quando o período letivo não está informado nos parâmetros da secretaria, o quadro de horários no portal é buscado como "Todos" porém, nenhum horário é exibido. Caso seja selecionado o período letivo, o quadro de horário realiza a pesquisa, sendo que ao selecionar novamente a opção todos, os horários são carregados corretamente.* |
| **Solução/Implementação:** | *Foi identificado que na tela do quadro de horários, quando é carregada a primeira vez, a opção "todos" assume o período letivo que está definido nos parâmetros da secretaria, mesmo que este não seja o período do professor. Foi feito o ajuste na tela, para que ao carregar o quadro de horários na primeira vez, que por padrão carrega com a opção "Todos", o sistema realmente carregue todas as disciplinas ativas do professor, independente se for a primeira vez que a tela for aberta.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *TVFE83* |
| **Requisito (ISSUE):** | *N/A.* |

divs
