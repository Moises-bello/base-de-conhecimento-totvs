---
content_hash: ab41ff99cc75140f90b55ca225ee5c759b65a80b028c6467229c2915b83500dc
fetched_at: '2026-06-29T00:08:08.630665+00:00'
page_id: '239015443'
product: rm
source: tdn-rm
title: TV3326_Importar_Gabarito_Prova_Sem_Questoes
type: documentation
url: https://tdn.totvs.com/display/LRM/TV3326_Importar_Gabarito_Prova_Sem_Questoes
version: 112
---

# IMPORTAR GABARITOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Importar gabarito* |
| **Situação/Requisito:** | *Ao tentar importar o gabarito de uma prova que não possui questões o sistema completa o processo de importação e informa que o gabarito foi importado com sucesso.* |
| **Solução/Implementação:** | *Foi identificado que o sistema não validava se a prova possui questões ou não, caso não exista, o processo prossegue e a prova finalizada. Foi feito o ajuste para verificar e interromper o processo para o candidato corrente caso a prova não possua questões e será exibido no log do processo a mensagem de alerta.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
