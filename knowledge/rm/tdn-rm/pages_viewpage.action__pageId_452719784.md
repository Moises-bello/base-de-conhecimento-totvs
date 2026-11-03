---
content_hash: 08f0279cb8d32a622ca741c3e44a6700488515b498f9feed7c8989144c1d263e
fetched_at: '2026-06-29T00:10:10.013069+00:00'
page_id: '452719784'
product: rm
source: tdn-rm
title: Código de Cálculo 15 - Ajuda de Custo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719784
version: 3
---

Provento do tipo valor com incidência conforme empresa.

O sistema irá lançar neste evento conforme informado no campo Ajuda de Custo do cadastro de Funcionários, pasta Base de Cálculo e fará proporcionalidade em relação a horas trabalhadas (Códigos de cálculo 01, 02 e 08).

O cálculo será feito da seguinte forma:

(CAMPO AJUDA DE CUSTO \* No. HORAS NORMAIS) / Nº. DE HORAS

O sistema buscará o valor informado no campo Ajuda de Custo, multiplicado pelo número de horas normais, e dividirá pelo número de horas informado para o evento com código de cálculo 01 (Horas Normais).

**Exemplo**

Ajuda de custo = 100,00

O funcionário trabalhou 220 horas, logo, o valor calculado será igual a 100,00.

Se o mesmo funcionário trabalhasse somente 110 horas, a ajuda de custo seria igual a 50,00.

É importante que o mesmo número de horas normais (código de cálculo 01) seja informado na movimentação do funcionário, antes ou simultaneamente com a ajuda de custo e que o evento de ajuda de custo tenha a prioridade maior.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
