---
content_hash: ce9ab94402e2bf4262ff3af23c346fd6c7bf3121054a21835b77ddbda587182d
fetched_at: '2026-06-29T00:08:16.345950+00:00'
page_id: '244938787'
product: rm
source: tdn-rm
title: TVNNE3_DT_Prova_Nao_Confidencial_Periodo_Confidencial
type: documentation
url: https://tdn.totvs.com/display/LRM/TVNNE3_DT_Prova_Nao_Confidencial_Periodo_Confidencial
version: 114
---

# PROVAS - PERÍODO CONFIDENCIAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Avaliação e Pesquisa* |
| **Função:** | *Provas - período confidencial* |
| **Situação/Requisito:** | *Quando a opção de confidencial está marcada para um determinado período da prova (somente para provas do tipo pesquisa de opinião), mesmo a prova não sendo confidencial, o sistema não executa a prova de forma confidencial, somente na tela inicial do executor que é exibido que é confidencial, porém ao concluir a avaliação, na tela de ranking é exibido os dados do candidato.* |
| **Solução/Implementação:** | *Foi identificado que o sistema só considerava o período como confidencial ao carregar os dados iniciais da avaliação, ao finalizar a prova, a mesma era considerada como não confidencial, só era considerada caso a prova fosse confidencial. Foi feito o ajuste no momento de carregar a avaliação, caso a prova seja confidencial, a mesma será mantida, porém se não for, o sistema irá verificar se o candidato possui período atribuído e se este é confidencial, caso for, a prova será confidencial, ou seja, os dados da pessoa são apagados ao finalizar a prova.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
