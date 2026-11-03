---
content_hash: 3f88e2f449dc4e0c957d6986f72a781df5468513c841a72347f977cebb21701e
fetched_at: '2026-06-29T00:09:11.507349+00:00'
page_id: '407110556'
product: rm
source: tdn-rm
title: 3624679 FINANCEIRO01-8627 Ao gerar relatório fluxo de caixa o sistema soma
  o valor previsto no saldo inicial a cada mês
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=407110556
version: 3
---

# Fluxo de Caixa

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Fluxo de Caixa | Fluxo de Caixa |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Lançamento | Lançamento | | Extrato de Caixa | Extrato de Caixa | |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | FIN000255 |
| **País(es):** | Bra |
| **Banco(s) de Dados:** | SQLServer, Oracle |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Otimização na visualização do fluxo de Caixa referente a exibição dos valores para não gerar duplicidade do valor inicial com o valor operacional do dia. 

## Procedimento para Utilização

Com a alteração na exibição dos valores no fluxo de caixa, o saldo Inicial só será preenchido com valores que não são apresentados nas linhas, ou seja, dentro do período selecionado. Isto somente para os valores previstos. Já o realizado funciona da mesma maneira. Os valores previstos de linha, das naturezas que estão dentro do período selecionado, não será repassado para o saldo inicial para não duplicar os valores. Veja um exemplo mais exemplificado para o compreendimento: (Obs.: a cor da palavra referencia ao retângulo colorido na imagem)

* Criado lançamento um a receber de valor 100,00 no dia 12/09/2018.
* Criado um lançamento a receber de valor 100,00 no dia 13/09/2018.
* Baixado um lançamento a receber no valor 100,66 no dia 14/08/2018.

A partir dessas informações perceba que ao gerar o relatório, no período do dia 12/09/2018 até 16/09/2018,  podemos visualizar-lo da seguinte forma:

* O valor 100,00 consta uma operação do dia 12/09/2018 e que resulta no saldo final de 100,00. Porém perceba que o saldo final do dia que é exibido no relatório não é repassado para o saldo inicial por já constar no valor 200,00, assim deixando o saldo final correto.
* Já o valor 100,66 é representado de forma diferente por constar somente o saldo realizado daquela data em questão, no dia 14/09/2018. Desta forma, o valor final é reexibido no saldo inicial do próximo dia, 15/09/2018.

Agora ao gerar o relatório, no período do dia 13/09/2018 até 16/09/2018,  podemos visualizar-lo da seguinte maneira:

* O valor 100,00  consta uma operação do dia 12/09/2018 que resulta no saldo inicial de 100,00. Veja que o saldo final do dia que é exibido no relatório consta o valor do saldo inicial e da operação do dia 13/09/2018. Agora perceba que é repassado para o saldo inicia l o valor inicial de valor 100,00 do dia anterior marcado. Ou seja, todo saldo anterior a data de inicio, 13/09/2018, gerada no relatório é sempre exibida no saldo inicial em todos os períodos.
