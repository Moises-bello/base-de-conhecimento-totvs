---
content_hash: 63bcad69394c9112cf540ff32202c80add5703ce674f7fa12dd35109d0bad83e
fetched_at: '2026-06-29T00:08:27.354471+00:00'
page_id: '271407997'
product: rm
source: tdn-rm
title: 98342 MEDU-326 Retorno Cobrança
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271407997
version: 111
---

# Integração Bancária - Retorno de Cobrança

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Gestão Financeira. |
| **Função:** | Integração Bancária - Retorno de Cobrança |
| **Situação/Requisito:** | Ao fazer baixa por retorno bancário, o sistema esta fazendo baixa parcial de lançamento com sobra de 0,01 centavo, sendo que o parâmetro para gerar baixa parcial esta setado para 1 real. |
| **Solução/Implementação:** | Ajuste no processo de retorno bancário, para boletos que agrupam vários lançamentos, onde o sistema está parametrizado para substituir os valores calculados pelo sistema, pelos valores informados no arquivo de retorno bancário. O cálculo da proporção de cada valor dos lançamentos compõem o boleto foi otimizado. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito (informe o requisito relacionado):** | FIN000169. |

divs
