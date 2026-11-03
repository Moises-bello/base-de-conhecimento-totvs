---
content_hash: 3bb4f34c430c0501457c9a6c53d1d00dd00d4404d9d03b1a1d138af4c1b3c344
fetched_at: '2026-06-29T00:10:10.065144+00:00'
page_id: '452719814'
product: rm
source: tdn-rm
title: Código de Cálculo 14 - Assistência Médica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719814
version: 4
---

Desconto do tipo valor. Este código de cálculo será usado para dedução de IRRF.

Para descontar a assistência médica específica da empresa (UNIMED, GOLDEN CROSS, etc), o usuário deverá criar um evento sem código de cálculo e cadastrar uma fórmula que atenda às suas necessidades.

O sistema buscará o total que "incide IRRF" e calculará 5% deste total.

Se o valor informado no código de cálculo 014 for superior ao resultado da operação anterior,

o sistema calculará a diferença e deduzirá do total que "Incide IRRF".

**Exemplo**

Valor total "inc. IRRF": 100,00

Valor do evento de código de cálculo 014: R$ 70,00

Cálculo:  
R$ 100,00 \* 5% = 5,00

R$ 70,00 - 5,00 = 65,00

R$ 100,00 - 65,00 = 35,00

R$ 35,00 serão aplicados na tabela de IRRF.

Veja também o TDN [Fórmulas / Funções – S - SALVAVALDEP](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719340) caso utilize fórmula que referencia essa função de fórmula.

---

Códigos de Cálculo
