---
content_hash: 1b3a2e7c4bf5efb905786cd64db97ee4804c66d4f0473bcdb7456087aac69f81
fetched_at: '2026-06-29T00:09:59.410127+00:00'
page_id: '452718342'
product: rm
source: tdn-rm
title: Código de Cálculo 70 - Descanso Semanal Perdido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718342
version: 2
---

Quando este evento for lançado pelo RM Labore deve ser:

Desconto do tipo dia, com percentual de incidência igual a 1,00 (um). Você deverá lançar o número de dias. Quando houver pagamento do total do DSR em um evento de provento e a discriminação do desconto no evento de CC70.

Quando este evento for lançado pelo RM Chronus deve ser:

Desconto do tipo hora quando o pagamento do DSR for o total do mês (Utilizando fórmula no RM Chronus) e o desconto discriminado no movimento do funcionário no evento de CC70.

**Ou**

Base de Cálculo do tipo hora com chave desativada quando o lançamento do DSR for o valor realmente devido já deduzido do DSR Perdido e o valor demonstrado neste evento for informativo. A finalidade deste evento é registrar quantos dias de descanso semanal serão deduzidos para o funcionário.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
