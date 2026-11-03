---
content_hash: 0fe0af7dd117bb7e3c9f5d3734f1f8a33a064759a9861ea8ed4d901b269a2a4e
fetched_at: '2026-06-29T00:06:29.341513+00:00'
page_id: '234606693'
product: rm
source: tdn-rm
title: TULQCK_DT_Contribuicao_Patronal_Secoes_Com_Prefixo
type: documentation
url: https://tdn.totvs.com/display/LRM/TULQCK_DT_Contribuicao_Patronal_Secoes_Com_Prefixo
version: 118
---

# RAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *RAIS* |
| **Situação/Requisito:** | *Informe a situação/requisito.* |
| **Solução/Implementação:** | *Alterado para considerar o valor da contribuição na RAIS conforme a quebra de prefixo. O sistema irá considerar a seção com a menor quantidade de dígitos, em caso de mais de uma seção sistema vai considerar a que tiver menor quantidade de dígitos.* |
| **Conversores e Parâmetros:** | Ao realizar a geração da RAIS para seções com vários prefixos RAIS, o sistema não está considerando os valores de contribuições sindicais (patronais) informados na seção centralizadora do prefixo. Através dos testes realizados o sistema parece considerar sempre os valores da primeira seção da quebra informada e leva esses valores para todos os prefixos. |
| **Chamados relacionados:** | *TULQCK, TUMNHD* |

divs
