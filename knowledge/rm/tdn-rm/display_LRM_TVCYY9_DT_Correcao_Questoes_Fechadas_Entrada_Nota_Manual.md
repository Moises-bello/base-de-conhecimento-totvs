---
content_hash: afbccc8bec997fc34e5e743c3b316c3575f45b1c36b4db360f7258814618fa35
fetched_at: '2026-06-29T00:08:11.570423+00:00'
page_id: '243012999'
product: rm
source: tdn-rm
title: TVCYY9_DT_Correcao_Questoes_Fechadas_Entrada_Nota_Manual
type: documentation
url: https://tdn.totvs.com/display/LRM/TVCYY9_DT_Correcao_Questoes_Fechadas_Entrada_Nota_Manual
version: 110
---

# RANKING - CORRIGIR QUESTÕES FECHADAS DA PROVA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Avaliação e Pesquisa* |
| **Função:** | *Ranking - Corrigir questões fechadas da prova* |
| **Situação/Requisito:** | *O sistema está apresentando um erro de referência de objeto no Log de correção de questões fechadas da prova quando temos uma nota que foi importada através do processo de Entrada de Nota por Prova.* |
| **Solução/Implementação:** | *Foi identificado que o processo de entrada manual de notas, apaga as questões da prova, e insere uma questão genérica sem opções, quando o sistema tenta fazer a correção, não existe opções na questão, assim gerando o erro. Foi inserido uma validação para que se prova  tiver a nota inserida manualmente, o sistema não faz a correção da questão fechada e considera a prova como corrigida.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
