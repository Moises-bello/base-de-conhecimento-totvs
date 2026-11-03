---
content_hash: 5bff877594f1759590b1b3d9b3f4e7264ec9608b5b0c4b28e4ad86c777b7ebce
fetched_at: '2026-06-29T00:10:00.826697+00:00'
page_id: '452718585'
product: rm
source: tdn-rm
title: Código de Cálculo 26 - FGTS Quitação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718585
version: 3
---

Base de Cálculo do tipo valor. O sistema somará os proventos do mês que "incidem FGTS" e encontrará o valor de INC. FGTS. Este evento será calculado se a rescisão tiver como código de afastamento as referências 2 ou T . O calculo será feito da seguinte forma:

(INC. FGTS - ESTORNA BASES) \* 8%

O sistema calculará (INC. FGTS - ESTORNA BASES) e, sobre o valor encontrado, será aplicada a taxa de 8%.

**Observação**

O Evento de código de cálculo 062 – Aviso Prévio deverá ter sua prioridade menor que a prioridade do evento de código de cálculo 026 – FGTS Quitação para que este considere o valor do aviso prévio para cálculo.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
