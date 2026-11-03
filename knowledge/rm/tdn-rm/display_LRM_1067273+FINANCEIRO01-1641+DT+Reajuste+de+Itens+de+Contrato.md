---
content_hash: 8267b9fd044d0d1556202301aaef005c1d7fc062f578cd3b8d840df194225410
fetched_at: '2026-06-29T00:08:39.971952+00:00'
page_id: '286027789'
product: rm
source: tdn-rm
title: 1067273 FINANCEIRO01-1641 DT Reajuste de Itens de Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/1067273+FINANCEIRO01-1641+DT+Reajuste+de+Itens+de+Contrato
version: 101
---

# Reajuste de Itens de Contrato

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Reajuste de Itens de Contrato. |
| **Situação/Requisito:** | No reajuste de contrato ao utilizar a função de fórmula "IUR" passando como parâmetro uma função de fórmula que retorne uma data, ocorre o erro abaixo:  Erro de compilação da fórmula Testing na linha 1! Valor do tipo 'RM.Lib.RMSFormulaDateTime' não pode ser convertido em 'Date' |
| **Solução/Implementação:** | Criado uma nova função de fórmula **IUR2 - Reajuste Valor Item de Contrato com Função de Data** que irá permitir como entrada uma outra função de fórmula que retorne uma data. Exemplos:  IUR2 (HOJE , 'IGPM' , 3 , 0 , 1),   IUR2 (DAT , 'IGPM' , 3 , 0 , 1),   IUR2 ( ‘20/09/2017’, 'SELIC' , 6 , 0 , 11) |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 1068754 |
| **Requisito:** | CTR000003 |

divs
