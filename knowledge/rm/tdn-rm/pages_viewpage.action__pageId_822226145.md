---
content_hash: 30999ecbe9264ef87a10f86deab3899e13674be66690d3b3c79a536f3eef1df1
fetched_at: '2026-06-29T00:11:45.950330+00:00'
page_id: '822226145'
product: rm
source: tdn-rm
title: Recalcular Movimentação de Convênios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822226145
version: 4
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Recálculo do Movimento do Convênio do Funcionário**
   1. **Principais Campos e Parâmetros**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Este modulo executa o recalculo da movimentação de convênio dos funcionários.

Deverá ser executado o processo de recalculo quando for executado o cancelamento de alguma movimentação de convênios em que possui parcelas envolvidas ou até mesmo alteração na tabela de cálculo.

## **02. EXEMPLO DE UTILIZAÇÃO**

11Atualizando Tabela de Cálculo

A execução da rotina em questão passa a ser utilizada quando for alterado algum valor da tabela de cálculo ou quando houver o cancelamento de um dos convênios do funcionário, onde passa a ser necessário que aja a “reconstrução” dos valores e meses das parcelas para envio ao envelope.

Para entender um pouco melhor o que foi passado acima, vejamos um exemplo um pouco mais detalhado do processo.

Para o exemplo que será passado, considere que temos a formação final das parcelas conforme abaixo:

| **Convênio** | 05/2021 | 06/2021 | 07/2021 | 08/2021 | 09/2021 | 10/2021 | **Total** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Odontológico - Obturação | R$ 71,00 | R$ 49,00 | - | - | - | - | R$ 120,00 |
| Odontológico - Extração | - | R$ 22,00 | R$ 66,00 | - | - | - | R$ 88,00 |
| Odontológico - Canal | - | - | R$ 5,00 | R$ 71,00 | R$ 71,00 | R$ 13,00 | R$ 160,00 |
| **Total** | R$ 71,00 | R$ 71,00 | R$ 71,00 | R$ 71,00 | R$ 71,00 | R$ 71,00 | - |

Em relação a possibilidade de alteração da tabela de cálculo, a reconstrução das parcelas irá sofrer uma leve modificação quando passar a se enquadrar em outra faixa ou quando o valor limite para desconto do funcionário sofrer algum tipo de alteração.

Um exemplo desse cenário seria o acontecimento da mudança dos valores limites das parcelas, passando a possuir um valor limite de R$ 84,00 ao invés de R$ 71,00.

Após a execução do processo de “Recalculo do Movimento do convênio”, as parcelas passarão a ficar de acordo com a tabela abaixo:

| **Convênio** | 05/2021 | 06/2021 | 07/2021 | 08/2021 | 09/2021 | **Total** |
| --- | --- | --- | --- | --- | --- | --- |
| Odontológico - Obturação | R$ 84,00 | R$ 36,00 | - | - | - | R$ 120,00 |
| Odontológico - Extração | - | R$ 48,00 | R$ 40,00 | - | - | R$ 88,00 |
| Odontológico - Canal | - | - | R$ 44,00 | R$ 84,00 | R$ 32,00 | R$ 160,00 |
| **Total** | R$ 84,00 | R$ 84,00 | R$ 84,00 | R$ 84,00 | R$ 84,00 | - |

Veja que além dos valores terem sofrido alterações, a quantidade das parcelas diminuiu para 5, sendo a última no mês 09/2021.

2Cancelamento de algum dos convênios parcelados

Para o outro cenário, onde ocorre o cancelamento de algum dos convênios parcelados, o sistema irá precisar reestruturar o desconto das parcelas, um exemplo seria a necessidade de cancelamento do convênio “Odontológico – Extração”, onde sem o recalculo a estrutura de descontos das parcelas será algo como a tabela abaixo.

| **Convênio** | 05/2021 | 06/2021 | 07/2021 | 08/2021 | 09/2021 | Total |
| --- | --- | --- | --- | --- | --- | --- |
| Odontológico - Obturação | R$ 84,00 | R$ 36,00 | - | - | - | R$ 120,00 |
| Odontológico - Canal | - | - | R$ 44,00 | R$ 84,00 | R$ 32,00 | R$ 160,00 |
| **Total** | R$ 84,00 | R$ 36,00 | R$ 44,00 | R$ 84,00 | R$ 32,00 | - |

Repare que apenas foi removido o convênio desejado, impactando na quantia para desconto dos meses 04 e 05, onde respectivamente se encontram no valor R$ 36,00 e R$ 44,00, valores no qual situa-se a baixo do valor limite para desconto.

Executando então a rotina de recalculo, as parcelas para desconto passarão a ser algo como a tabela abaixo.

| **Convênio** | 05/2021 | 06/2021 | 07/2021 | 08/2021 | Total |
| --- | --- | --- | --- | --- | --- |
| Odontológico - Obturação | R$ 84,00 | R$ 36,00 | - | - | R$ 120,00 |
| Odontológico - Canal | - | R$ 48,00 | R$ 84,00 | R$ 28,00 | R$ 160,00 |
| **Total** | R$ 84,00 | R$ 84,00 | R$ 84,00 | R$ 28,00 | - |

Verifique que as quantidades de parcelas foram alteradas, diminuindo para um total de 4, como também o “recalculo” dos valores de desconto para cada mês.

## **03.** **TELA Recálculo do Movimento do Convênio do Funcionário**

****Principais Campos e Parâmetros****

| Campo | Descrição |
| --- | --- |
| Quebra de Seção | Informe a quebra de seção. |
| Seleção de funcionários | Seleção dos funcionários que deverão ser considerados para a execução do processo |
| Convênio | Informar qual convênio deverá ser considerado para o recalculo |
| Utilizar data atual para verificar tabela de cálculo | Optar pelo uso da data atual para que seja verificado a tabela de cálculo |
| Forma de exibição do log | Informar qual será a forma de exibição do log, podendo ser optado por uma exibição de log mais simples ou detalhada |

## **04. TABELAS UTILIZADAS**

* PFMOVCONVENIO
