---
content_hash: cc032503104541cec0b10856d7bf071f2209f2b244f8e7ec1eee24bd37323419
fetched_at: '2026-06-29T00:08:24.622197+00:00'
page_id: '270899038'
product: rm
source: tdn-rm
title: 305625_DT_Inclusão_Bolsa_Retroativa_Aluno_Já_Tem_Bolsa_NãoEstá_Acumulando_Valor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270899038
version: 114
---

# Bolsa Retroativa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Bolsa Retroativa |
| **Situação/Requisito:** | Ao incluir uma bolsa retroativa para um aluno que já tenha uma bolsa o sistema não está acumulando o valor das duas bolsas no campo "Valor opcional" que representa o desconto da bolsa.  Exemplo:  Para o contrato X tem a parcela 1 com lançamento de 1000.00 e uma bolsa de 85 %.  Temos o lançamento com:  Valor original:1000,00  Valor opcional (valor bolsa):850,00.  Após executamos o processo de bolsa retroativa incluindo mais uma bolsa de 15%, o lançamento está ficando assim:  Valor original:1000,00  Valor opcional (valor bolsa):150,00.  O correto seria:  Valor original:1000,00  Valor opcional (valor bolsa):1000,00 (850,00+150,00). |
| **Solução/Implementação:** | Ajuste no processo de inclusão de bolsa retroativa para que os valores de bolsa no lançamento financeiro sejam acumulados corretamente quando o aluno já possuir uma bolsa. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** | *305625 / MEDU-1724* |
| **Requisito (informe o requisito relacionado):** |  |

divs
