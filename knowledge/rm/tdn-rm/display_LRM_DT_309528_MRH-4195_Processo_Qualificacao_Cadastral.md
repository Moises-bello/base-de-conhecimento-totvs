---
content_hash: b69d32e48ead522d2d1a2cf2b6971c62c4b19edaf814374df6a36ec051935059
fetched_at: '2026-06-29T00:08:26.406388+00:00'
page_id: '271178168'
product: rm
source: tdn-rm
title: DT_309528_MRH-4195_Processo_Qualificacao_Cadastral
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_309528_MRH-4195_Processo_Qualificacao_Cadastral
version: 112
---

# Processo de qualificação Cadastral ESocial

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Qualificação Cadastral* |
| **Situação/Requisito:** | Ao gerar o processo de qualificação cadastral o sistema não estava levando um funcionário. |
| **Solução/Implementação:** | O erro ocorria pois o sistema estava buscando a quantidade de funcionários - 1, desta forma removendo o último funcionário da listagem, assim foi ajustado o sistema para processar todos os funcionários que foram retornados na listagem. |
| **Tickets relacionados:** | * 309528 |

divs
