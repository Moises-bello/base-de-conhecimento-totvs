---
content_hash: 6451508b3a129dcc1b6e1666b9a4911257578241244045dfafec65db9d6c7b22
fetched_at: '2026-06-29T00:08:24.226741+00:00'
page_id: '270895512'
product: rm
source: tdn-rm
title: 246598_DT_Matricula_Online_valorBolsa_Maior_ValorOriginal
type: documentation
url: https://tdn.totvs.com/display/LRM/246598_DT_Matricula_Online_valorBolsa_Maior_ValorOriginal
version: 109
---

# Geração de Lançamento Financeiro

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Geração de Lançamento Financeiro |
| **Situação/Requisito:** | Ao realizar a matricula online o sistema estava apresentando a mensagem "O valor da bolsa não pode ser maior que o valor original do lançamento menos o desconto ". |
| **Solução/Implementação:** | Identificamos que a não conformidade estava ocorrendo na validação dos valores de bolsa ao gerar o lançamento financeiro.  Internamente o sistema validava se o valor total de bolsa ultrapassou o valor original do lançamento, para realizar esta validação é aplicado arredondamento no valor calculado conforme a quantidade de casas decimais parametrizada no módulo financeiro, porem este arredondamento estava sendo aplicando somente sobre o valor original e não sobre o valor de bolsa.  Como a bolsa era de 100% o valor de bolsa e valor original ficava igual, porem ao aplicar o arredondamento o sistema formatava o valor com duas casas decimais e neste caso o valor ficava diferente. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 246598 / MEDU-1665 |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
