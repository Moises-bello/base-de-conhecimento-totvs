---
content_hash: 2ce1172701471692c44fc384f6347695359ed98c3ffef430f6fbafe292e0f099
fetched_at: '2026-06-29T00:08:58.084658+00:00'
page_id: '359470363'
product: rm
source: tdn-rm
title: 2623743 CONTROLADORIA01-1343 DT Fato Contábil gerado pela ECD (Sped Contábil)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=359470363
version: 89
---

# Fato Contábil gerado pela ECD (Sped Contábil)

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Fato Contábil gerado pela ECD (Sped Contábil) |
| **Situação/Requisito:** | Ao criar a DRE através da estrutura de demonstrações contábeis para ser enviada para o Sped, foi criado alguns fatos contábeis utilizando expressões (exemplo: "fato1 – fato2" onde o fato1 é uma expressão e fato2 e o resultado direto de uma ou mais contas contábeis. Ao gerar a demonstração, os valores batem corretamente, porém ao gerar o Sped, o registro J150 é criado com os valores diferentes pelos apresentados no sistema. |
| **Solução/Implementação:** | Mudança na forma como a rotina do SPED calcula os Fatos Contábeis baseados em Expressão em que a mesma é o resultado de uma operação entre Expressão e Fato Contábil que recupera o resultado direto de uma ou mais contas. Neste caso será levado em consideração o sinal parametrizado na coluna do Fato Contábil. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados**: | N/A |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
