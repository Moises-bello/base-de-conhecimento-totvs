---
content_hash: b13ef11391e4bf38458d7832a3f936df37b19b43fae8699effbf8d0f330e4a8d
fetched_at: '2026-06-29T00:08:33.067226+00:00'
page_id: '274301138'
product: rm
source: tdn-rm
title: TVLTPZ FOPROTINAS01-69 DT Comparativo Folha Analítica X Sefip Autônomos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274301138
version: 108
---

# COMPARATIVO FOLHA ANALÍTICA X SEFIP

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Comparativo Folha Analítica X Sefip |
| **Situação/Requisito:** | Funcionários autônomos não considerados na geração do comparativo da Folha Analítica X Sefip |
| **Solução/Implementação:** | Realizado o tratamento na geração do comparativo Folha Analítica X Sefip, para considerar os funcionários com código da categoria igual a 13 ou 14. Sendo que se a categoria for igual a 13 ou 14 a data de admissão não deve ser preenchida, e deve ser considerado o valor da base de INSS quando a categoria for igual a 13 ou 14 para preencher os campos Remuneração sem 13° e Remuneração 13°, pois para funcionários autônomos não é gerado base de FGTS na Folha Analítica. |
| **Tickets relacionados:** | TVLTPZ |

divs
