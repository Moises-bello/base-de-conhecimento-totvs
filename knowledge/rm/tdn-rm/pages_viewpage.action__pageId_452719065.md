---
content_hash: 136d7aed92cad6f388b543f1c1cc54503ba59bacaeb3bf227cd2308e60e0980e
fetched_at: '2026-06-29T00:10:03.238774+00:00'
page_id: '452719065'
product: rm
source: tdn-rm
title: Código de Cálculo 50 - Salário Hora Mês Anterior
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719065
version: 4
---

Provento do tipo hora/dia com porcentagem de incidência.

O cálculo será feito da seguinte forma:

Tipo Hora:

((SAL. MES ANT. / No. HORAS) \* No. HORAS INFORMADAS) \* PERC.INCIDENCIA

Tipo Dia:

((SAL. MES ANT. / 30) \* No. HORAS INFORMADAS) \* PERC.INCIDENCIA

O sistema buscará o salário do mês anterior dividido pela Jornada (em Cadastro | Funcionários | pasta Base de Cálculo), multiplicará pelo número de horas informado e pelo percentual de incidência.

**Exemplo**

*Ref.             Descrição                                         CC       Perc. Inc.*  
 89    Hora Extra 50% Mês Anterior           50         1,50

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
