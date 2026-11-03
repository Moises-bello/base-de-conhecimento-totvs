---
content_hash: 52a2795946376397ba13ad70fca790b7a73e1c677a11fea781c9758c7c1c3504
fetched_at: '2026-06-29T00:11:49.652286+00:00'
page_id: '836067646'
product: rm
source: tdn-rm
title: Exemplo Saldo de Fluxo de Desembolso
type: documentation
url: https://tdn.totvs.com/display/LRM/Exemplo+Saldo+de+Fluxo+de+Desembolso
version: 2
---

Neste exemplo simples é possivel visualizar o que cada etapa esta considerando ao calcular o saldo de fluxo de desembolso.

Considerando apenas uma tarefa no planejamento abaixo a tarefa foi planejada para quatro períodos com compras contratadas apenas em dois meses (abril e maio).

|  |  | Abril | Maio | Junho | Julho | Total |
| --- | --- | --- | --- | --- | --- | --- |
|  | Tarefa 001.01.01 | 125,00 | 125,00 | 125,00 | 125,00 | 500,00 |
| **Abril** | Contrato 0012024 | 20,00 |  |  |  |  |
| **Maio** | Contrato | 20,00 | 20,00 |  |  |  |
|  |  |  |  |  |  |  |

Diante deste cenário temos:

|  |  | 1 | 2 | 3 | 4 | Total |
| --- | --- | --- | --- | --- | --- | --- |
|  | **Linha Base** | 125,00 | 125,00 | 125,00 | 125,00 | 500,00 |
|  | **Histograma** | 105,00 | 125,00 | 125,00 | 125,00 | 480,00 |
|  | **Histograma** | 105,00 | 105,00 | 125,00 | 125,00 | 460,00 |
|  |  |  |  |  |  |  |

Planejando a tarefa

Gerando a linha Base

Ao gerar o saldo  o valor de desembolso segue o mesmo do histograma inicial.

Após criar um contrato e contratar R$20,00 como exemplificado acima ao executar novamente as etapas do processo de saldo de fluxo de desembolso percebemos que o histograma passa a considerar a previsão informada no contrato .

**É importante destacar que sempre que se fizer alguma alteração no contrato deve-se calcular o mesmo para que seja considerado atualizado ao executar o saldo de fluxo de desembolso**

Totalizando a soma neste momento em R$605,00

Sendo

Histograma inicial = 500,00

Valor adicionado previsto em contrato = 125,00

Valor associado em contratos a ser abatido do histograma = 20,00

Agora foi  medido/consumida  a tarefa e entao passa a ser considerada a previsão dessa medição

Passando o log a ficar da seguinte forma:

Valor Histograma inicial = 500,00

Valor associado em contratos a ser abatido do histograma = 20,00

Valor adicionado previsto em contratos = 125,00

Valor medido dos contratos a ser abatido na previsão = 20,00

Valor do desembolso - 585,00

simplificando = (histograma + previsto ) - (valor associado + medido)

Liberando o contrato para backoffice e faturando o mesmo ...

é gerando o lançamento no financeiro que abate o que de fato foi pago .

Ao executar o processo de saldo de fluxo de desembolso novamente o valor é atualizado
