---
content_hash: 1f519055b54db96d3d2d67d1046d9ace64dc404052207a21d97fe0dfe450f786
fetched_at: '2026-06-29T00:06:15.524497+00:00'
page_id: '211058923'
product: rm
source: tdn-rm
title: DT_Usa_Regime_Tempo_Parcial
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Usa_Regime_Tempo_Parcial
version: 3
---

# USA REGIME DE TEMPO PARCIAL

## Características do Requisito

  

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Parâmetros* | *Férias: Cálculo* | |
| **Versões/Release:** | *12.1.4* |

## Descrição

Essa implementação consiste na validação do flag “Uso de regime de tempo parcial” também no portal. Era possível marcar mais do que 30 dias de férias apenas utilizando o “Regime de tempo parcial” pela MDI. Assim, o portal foi evoluído para comportar conforme a MDI.

## Procedimento para Utilização

Tem no produto o flag de “Usa regime de tempo parcial”. Com ele marcado é possível determinar para cada funcionário os dias de direito de férias superior a 30 dias.

1º Flag “Usa regime de tempo parcial”

2º Determina a quantidade de dias de férias por funcionário

3º - Nos cadastros de férias o sistema assume o novo saldo

Contudo, no portal o funcionário não conseguia agendar férias maiores do que 30 dias. Esta implementação adequou o mesmo comportamento da MDI para o portal.
