---
content_hash: 1d89aee671addf2cc591c178bf1724ba6c9b4df82ed43bcba27aec2c98d1be61
fetched_at: '2026-06-29T00:08:55.815909+00:00'
page_id: '351016901'
product: rm
source: tdn-rm
title: 2399384 DEDUINTEGRACOES-2163 DT Erro na geração de lançamentos com bolsa 100%
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=351016901
version: 88
---

# GERAÇÃO DE LANÇAMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Geração de lançamentos |
| **Situação/Requisito:** | Ao gerar um lançamento financeiro para uma parcela com bolsa de 100%, quando o sistema está parametrizado para não dividir o valor do crédito entre as parcelas calculadas por crédito e parametrizado para calcular multa sem incidir sobre o valor de bolsa, o valor calculado para a multa pode ficar negativo, caso o sistema também esteja parametrizado para trabalhar com 2 casas decimais e o valor dos créditos financeiros utilize 4 casas decimais. |
| **Solução/Implementação:** | Foi realizada otimização do processo de geração de lançamentos, de forma que o sistema, faça o arredondamento do valor original, conforme a parametrização do sistema financeiro, caso não seja feita a divisão dos valores de crédito entre as parcelas do contrato. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
