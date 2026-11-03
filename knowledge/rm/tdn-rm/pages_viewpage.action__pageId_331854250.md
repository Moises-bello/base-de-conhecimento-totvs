---
content_hash: 082e26795f5525a120b834a30d19b45f9c94eafae074ece5149dac2899e4dd07
fetched_at: '2026-06-29T00:08:49.677881+00:00'
page_id: '331854250'
product: rm
source: tdn-rm
title: 1882593 EDUCACIONAL01-3785 Habilitação Filial via Rest
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=331854250
version: 93
---

# HABILITAÇÃO FILIAL VIA REST

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Habilitação filial via Rest* |
| **Situação/Requisito:** | *Estamos utilizando o DataServerName “EduHabilitacaoFilialData” para retornar os dados da habilitação filial e os centros de custos com estão sendo preenchidos com valores nulos para os cursos mesmo quando existem valores cadastrados no banco de dados.* |
| **Solução/Implementação:** | *Foi acrescentado o campo SHABILITACAOFILIAL.CODCCUSTO na consulta de readview para que o retorno da chamada de GET via Rest tenha esse campo preenchido.* |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
