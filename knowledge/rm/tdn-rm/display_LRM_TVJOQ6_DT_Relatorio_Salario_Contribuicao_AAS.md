---
content_hash: edb60f839452f7b10e8bfc036fe615f67643584fbdd245763a056178845b379f
fetched_at: '2026-06-29T00:08:14.253300+00:00'
page_id: '244445031'
product: rm
source: tdn-rm
title: TVJOQ6_DT_Relatorio_Salario_Contribuicao_AAS
type: documentation
url: https://tdn.totvs.com/display/LRM/TVJOQ6_DT_Relatorio_Salario_Contribuicao_AAS
version: 116
---

# RELATÓRIO SALÁRIO CONTRIBUIÇÃO (AAS)

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Relatório de Salário Contribuição (AAS) |
| **Situação/Requisito:** | Ao gerar o relatório de salário contribuição , foi constatado que o sistema não estava realizando corretamente o cálculo de discriminação das parcelas do salário de contribuição ao realizar a liberação de competência. O sistema estava realizando o cálculo de descontos no seu valor total e não por grupo AAS. |
| **Solução/Implementação:** | Alteração na consulta responsável por realizar o cálculo. O sistema passa a trazer os proventos e descontos por grupo AAS, desta forma, realiza o cálculo corretamente. |
| **Chamados relacionados:** | TVJOQ6; TVKQEG |

divs
