---
content_hash: dc8436fcc3418fe1d5289d08eda6ec09a8ba41d00920f82271e0d067712f59ee
fetched_at: '2026-06-29T00:06:24.173885+00:00'
page_id: '224113825'
product: rm
source: tdn-rm
title: TTWMA4_DT_Lançamentos_De_Estorno_Não_Aparecem_Na_Contabilização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224113825
version: 125
---

# CONTABILIZAÇÃO POR COMPETÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Contabilização por competência* |
| **Situação/Requisito:** | *Ao realizar estorno de uma contabilização integrada ao lote zero, utilizando o novo modelo de contabilização, o sistema grava a identificação da operação de estorno apenas na tabela SCONTRATOCONT, porém ao gerar novamente a contabilização a operação é pesquisada na tabela SCONTRATO. Assim, uma nova operação é realizada e associada ao contrato e as contabilizações de estorno deixam de ser exibidas no anexo do contrato.* |
| **Solução/Implementação:** | *Foi realizada otimização do processo de contabilização por competência para o novo modelo, de forma a exibir corretamente os lançamentos contábeis estornados caso seja feito estorno da contabilização do contrato e em seguida a sua recontabilização.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *TUCPJ0* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *11.82.43* |
| **Versão Corrigida:** | *11.82.43* |
| **Versão Expedida:** | *11.82.43* |

divs
