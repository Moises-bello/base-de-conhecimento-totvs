---
content_hash: 42b8c6e2a5ba31f16a30d6d033094312860e2fff36a6b840f9540bfa9b3acc4b
fetched_at: '2026-06-29T00:09:58.889599+00:00'
page_id: '452718235'
product: rm
source: tdn-rm
title: Código de Cálculo 61 - IRRF de Férias Envelope
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718235
version: 2
---

O sistema calcula automaticamente este evento quando é processada a Diferença de Férias.

Caso o cálculo da diferença seja dentro do mesmo caixa do pagamento das férias, o evento com código de cálculo 61 é calculado sobre o total das férias e é deduzido o valor que já foi pago.

Se o cálculo é para o caixa seguinte ao pagamento das férias, o evento com código de cálculo 61 é calculado somente sobre a diferença de férias.

Evento do tipo Desconto e Valor.

**Atenção:**

Quando utiliza o Cálculo .Net este evento também é lançado no cálculo da rescisão. Esta mudança foi necessária para atender situações em que o funcionário tem rescisão no mesmo mês e período do lançamento das férias.  
 Sendo assim, quando utiliza Cálculo .Net a descrição do código de cálculo 61 foi alterada para 'IRRF de Férias Envelope'.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
