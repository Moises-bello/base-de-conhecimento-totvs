---
content_hash: b33e1274d93ed0c3d63b6db4d09d40f97d84e015fd5d78b905f6b319509dfa80
fetched_at: '2026-06-29T00:08:21.395788+00:00'
page_id: '268818239'
product: rm
source: tdn-rm
title: TWA177_DT_Transferencia_Sem_Levar_1aParcela13o
type: documentation
url: https://tdn.totvs.com/display/LRM/TWA177_DT_Transferencia_Sem_Levar_1aParcela13o
version: 112
---

# NA TRANSFERÊNCIA SEM LEVAR O EVENTO DE 1a PARCELA DE 13o, O VALOR NÃO É ABATIDO NA 2a PARCELA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *13o. Salário* |
| **Situação/Requisito:** | Quando o funcionário é transferido logo após o pagamento da 1º parcela de 13º salário e é feito o pagamento da 2ª parcela de 13º salário na nova chapa ativa, não está considerando o valor pago na 1ª parcela, pois a ficha financeira não é transferida no mês da transferência. |
| **Solução/Implementação:** | Foi criado um novo código de cálculo para levar para a chapa ativa o valor pago no evento de CC 9. Código de cálculo 355 - PRIMEIRA PARCELA 13º TRANSFERIDA PARA OUTRA FILIAL.  O evento com o CC 355 será inserido na movimentação do funcionário ativo somente se não for marcada a opção para transferir movimento do mês atual.  E no cálculo do CC 35 - ADIANTAMENTO PRIMEIRA PARCELA 13º SALÁRIO, será lançado o valor do CC 355, caso seja encontrado no ano corrente. |
| **Chamados relacionados:** | *TWA177* |

divs
