---
content_hash: a348cd806de46671d9dfb646d046b9efa0b56be131ede7f98bca80e0ec057b24
fetched_at: '2026-06-29T00:08:23.980272+00:00'
page_id: '270101099'
product: rm
source: tdn-rm
title: MEDU-1126_DT_Revisar_Questa_Valor_Questao_Prova_Associada
type: documentation
url: https://tdn.totvs.com/display/LRM/MEDU-1126_DT_Revisar_Questa_Valor_Questao_Prova_Associada
version: 111
---

# REVISAR QUESTÃO - VALOR DA QUESTÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs avaliação e pesquisa* |
| **Função:** | *Revisar questão - valor da questão* |
| **Situação/Requisito:** | *Quando é feito a revisão de uma questão que já está em uma prova e na revisão é alterado o valor da questão, o valor da questão não é refletido para as provas que tem a questão associada para novos candidatos, para candidatos que já executaram a prova é mantido o valor antigo corretamente.* |
| **Solução/Implementação:** | *Foi identificado que os dados da questão são alterados corretamente na revisão, porém não é alterado nas definições da questão nas provas que estão associadas. Foi feito uma alteração no processo para que ao alterar os dados da questão, altere também nas definições das provas que a questão está associada, assim, para novos candidatos, os dados serão exibidos corretamente, inclusive o valor da prova será contabilizado corretamente e para candidatos que já executaram provas que possuem a questão revisada, os dados e o valor da questão permanecerá o mesmo.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | **N/A** |
| **Requisito (ISSUE):** | *N/A* |

divs
