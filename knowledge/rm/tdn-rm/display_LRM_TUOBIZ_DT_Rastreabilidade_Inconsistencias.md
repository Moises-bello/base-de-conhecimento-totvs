---
content_hash: 41455ebfb6a0ea064afc93d52975c07345722cf4279357aa49b5f0698cf96e0c
fetched_at: '2026-06-29T00:08:09.273313+00:00'
page_id: '239032535'
product: rm
source: tdn-rm
title: TUOBIZ_DT_Rastreabilidade_Inconsistencias
type: documentation
url: https://tdn.totvs.com/display/LRM/TUOBIZ_DT_Rastreabilidade_Inconsistencias
version: 117
---

# Rastreabilidade Inconsistências

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | **Rastreabilidade Inconsistências** |
| **Situação/Requisito:** | Erro ao realizar a importação devido à novas chaves estrangeiras adicionadas na tabela PEVENTO |
| **Solução/Implementação:** | Ajuste na rotina de Rastreabilidade de Inconsistências para ignorar referências de chaves estrangeiras FKPEVENTO\_SCLASSEVALORPROTHEUS, FKPEVENTO\_SITEMCONTABILPROTHEU na importação do arquivo. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TVA813 |
| **Requisito (ISSUE):** |  |

divs
