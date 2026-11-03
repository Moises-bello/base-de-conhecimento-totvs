---
content_hash: f1f3cf2017563dd4f5541fa3fb8be2c7f4e7bd4863bb911de8ca5c02d17e6329
fetched_at: '2026-06-29T00:09:59.794750+00:00'
page_id: '452718390'
product: rm
source: tdn-rm
title: Código de Cálculo 380 - Diferença Indenização Tempo de Serviço de Safrista
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718390
version: 2
---

Este código de cálculo foi criado para lançar a diferença de Indenização de tempo de serviço para funcionário safrista, no processo de cálculo da rescisão complementar. Este evento é lançado somente se no recalculo do rescisão do safrista for recalculado o evento com o CC 379 e encontrado diferença entre o que foi pago na rescisão e o novo valor calculado.  
    
 **Observação**  
 Este evento não verifica se o parâmetro 'Lança indenização por tempo de serviço de safrista (rural)' está marcado, mas somente se o evento de CC 379 se encontra na ficha financeira, no período de recalculo da rescisão.   
 Caso o evento  de  CC 379 não tenha sido pago na rescisão e antes de calcular a rescisão complementar o parâmetro 'Lança indenização por tempo de serviço de safrista (rural)' é marcado, o sistema calcula o evento de CC 379 e lança o valor encontrado no evento de CC 380.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
