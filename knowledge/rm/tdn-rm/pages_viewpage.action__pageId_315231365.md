---
content_hash: 3a316093b220ad4e5873a49110659c0db5f0dddd7ac2939d41ad6bafb7cf2642
fetched_at: '2026-06-29T00:08:45.711100+00:00'
page_id: '315231365'
product: rm
source: tdn-rm
title: 1538271 FINANCEIRO01-3550 Falha no Cálculo de Valor Líquido no Retorno de Cobrança
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=315231365
version: 92
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Financeiro |
| **Função:** | Retorno de Cobrança Eletrônica |
| **Situação/Requisito:** | Foi apresentado erro de runtime ao executar o cálculo de valor líquido dos lançamentos associados aos boletos. O erro ocorreu porque um mesmo lançamento estava referenciado em mais de um boleto. |
| **Solução/Implementação:** | Foi implementado um tratamento defensivo que evita a falha do cálculo do valor líquido. Também foi tratado o motivo da geração de mais de um boleto para o mesmo lançamento. |
| **Conversores e Parâmetros:** | Não se aplica |
| **Tickets relacionados:** | Não se aplica |
| **Requisito:** | FIN000172 |

divs
