---
content_hash: 1a58d40c35f92b3a05ff32a6533d804f0c532180709891cdd6ebda4bdd191e82
fetched_at: '2026-06-29T00:10:09.390136+00:00'
page_id: '452719653'
product: rm
source: tdn-rm
title: S-1202 - Remuneração de Servidor Vinculado a Regime Próprio de Previd. Social
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719653
version: 2
---

São as informações da remuneração de cada servidor/militar no mês de referência. Este evento deve ser utilizado para os servidores filiados ao Regime Próprio de Previdência Social – RPPS pertencentes as categorias 301, 303 (sub judice no STF para parlamentares estaduais), 305 (desde que seja servidor público efetivo oriundo de ente que possua RPPS) e 307 (Militar).

Será gerado na fila de eventos quando o cadastro do funcionário contemplar uma das seguintes combinações:

1. Quando o "Código da Categoria" for igual a 3XX e o "Tipo de Regime Previdenciário" igual 2 - Regime próprio de Previdência Social - RGPS ou 3 - Regime de Previdência Social no Exterior;
2. Quando o "Código da Categoria" for igual a 410 e:
   1. Caso o "Tipo de Regime Previdenciário" relativo ao vínculo firmado com o órgão público **cedente/de origem** for igual a 2 - Regime próprio de Previdência Social - RGPS;
   2. Caso o "Tipo de Regime Previdenciário" for igual a 3 - Regime de Previdência Social no Exterior e o "Código da Categoria" relativo ao vínculo firmado com o órgão público **cedente/de origem** for igual a 3XX.

[**Mapeamento das informações do evento**](http://tdn.totvs.com/display/LRM/Evento+S-1202)

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Eventos Periódicos

Gerar XML
