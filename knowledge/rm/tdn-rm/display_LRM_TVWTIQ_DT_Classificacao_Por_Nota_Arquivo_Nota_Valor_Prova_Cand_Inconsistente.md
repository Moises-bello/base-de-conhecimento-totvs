---
content_hash: e8348604ceba8b9fa64efe43984b589c01ad8006131d060eb0906b983bb55fb6
fetched_at: '2026-06-29T00:08:19.430489+00:00'
page_id: '267786184'
product: rm
source: tdn-rm
title: TVWTIQ_DT_Classificacao_Por_Nota_Arquivo_Nota_Valor_Prova_Cand_Inconsistente
type: documentation
url: https://tdn.totvs.com/display/LRM/TVWTIQ_DT_Classificacao_Por_Nota_Arquivo_Nota_Valor_Prova_Cand_Inconsistente
version: 112
---

# CLASSIFICAR CANDIDATOS - CLASSIFICAÇÃO POR NOTA - ARQUIVO DE NOTAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Processo Seletivo* |
| **Função:** | *Classificar candidatos - classificação por nota - arquivo de notas* |
| **Situação/Requisito:** | *Ao utilizar o processo de classificação de candidatos por nota utilizando arquivo de notas, quando uma prova possui o total da nota um valor decimal ocorre uma inconsistência na validação das notas do candidato com a avaliação, pois a comparação das notas ocorre com formato incorreto, a do candidato está correta utilizando o valor decimal, porém o total da prova é utilizando um valor inteiro, se a nota for decimal, só é retornado o valor inteiro da prova, assim gerando inconsistência na comparação entre as duas notas.* |
| **Solução/Implementação:** | *Foi feito um ajuste na função que retorna o valor da prova para que retorne o valor decimal correto, assim a comparação da nota do candidato com a prova poderá ser executada corretamente.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | **N/A** |
| **Requisito (ISSUE):** | *N/A* |

divs
