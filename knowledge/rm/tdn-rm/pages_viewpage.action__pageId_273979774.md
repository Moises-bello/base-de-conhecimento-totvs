---
content_hash: 447f9faee83a0e45472716d71f5f02b8b3043471cec57d40f4cb73dae205b422
fetched_at: '2026-06-29T00:08:31.984864+00:00'
page_id: '273979774'
product: rm
source: tdn-rm
title: 667444 FOPROTINAS01-35 DT GRCSU SEÇÕES identificadas por CPF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273979774
version: 112
---

# GRCSU

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Folha de Pagamento. |
| **Função:** | Calculo do campo Nosso Numero em que a seção é identificada por CPF. |
| **Situação/Requisito:** | Ao tentar gerar o relatório da GRCSU para seções identificadas por CPF o sistema apresenta o erro: O índice e o comprimento devem se referir a um local dentro da cadeia de caracteres. |
| **Solução/Implementação:** | Feito a tratativa na GRCSU para completar com zeros a esquerda uma vez que o CPF tem 11 dígitos e este valor é usado no campo nosso número que exige o tamanho de 12. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** | 667444 |
| **Requisito:** |  |

divs
