---
content_hash: 81c3a84dc76b71f06a2823d154a746a675bedf17650e8abfde3b981a9ccdb62c
fetched_at: '2026-06-29T00:08:51.025455+00:00'
page_id: '336398829'
product: rm
source: tdn-rm
title: 1596596 RMFIN-963 - Controle de Recebimento Erro ao Aplicar o Desconto
type: documentation
url: https://tdn.totvs.com/display/LRM/1596596+RMFIN-963+-+Controle+de+Recebimento+Erro+ao+Aplicar+o+Desconto
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Gestão Hospitalar |
| **Função:** | Controle de Recebimento |
| **Situação:** | Ao Lançar uma baixa com um desconto que totalizará a fatura. E esta fatura possuir uma integração com o RM-Fluxus. O Sistema esta apresentando um erro em relação ao calculo da da fatura. |
| **Solução:** | Efetuada correção no calculo. |

Segue um exemplo de como se aplica um desconto.

Em uma fatura com valor a Receber de R$1.436,45, irá se conceder um desconto de de R$436,65 e será recebido os R$1.000,00 em Dinheiro.

Ao fazer o recebimento deve-se:

* Informar o valor de R$1.000,00 em **Valor Recebido**
* Definir a **Forma de Recebimento**
* Informar o valor de R$436,45 em **Desconto**

**OBSERVAÇÃO:** Se for Inserido no campo **Valor Recebido** o valor total de R$1.436,45 e o **Desconto** de R$436,45 ao tentar incluir o RMFluxus retonará um erro que o valor não recebido está inválido por sem maior que o valor liquido esperado.
