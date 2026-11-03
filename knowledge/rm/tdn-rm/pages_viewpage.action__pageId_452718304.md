---
content_hash: c8f27c4894a5a806c46db463338d99cbd2d07195d8b1220b088c3fdd2acbb4ee
fetched_at: '2026-06-29T00:09:59.337462+00:00'
page_id: '452718304'
product: rm
source: tdn-rm
title: Código de Cálculo 22 - Insalubridade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718304
version: 2
---

Provento do tipo hora com porcentagem de incidência igual a 10,00. Para efetuar o lançamento, informe o número que, multiplicado por 10 (dez), corresponde ao percentual de insalubridade pago pela empresa.

O cálculo será feito da seguinte forma:

**Tipo hora:**

((SAL. MIN. \* PORC. INC. INSAL.) / 100) \* (H/INF. NA INSAL. / No. H/MES) \* No. DE H/NOR.

O sistema multiplicará o valor do salário mínimo pela porcentagem de incidência informada e dividirá por 100 (cem). O valor encontrado será multiplicado pelo número de horas informado na insalubridade, dividido pelo número de horas- mês (campo Jornada em Cadastros | Funcionários | pasta Base de Cálculo) e multiplicado pelo número de horas normais.

**Tipo dia:**

(((SAL. MIN. / 30) \* POR INCID.) \* No. HORAS INF.) \* Número. HORAS NORMAIS

**Observação**

As empresas que têm como rotina agregar o valor da Insalubridade ao salário para outros cálculos (ex: Hora Extra) deverão colocar marcar a opção em "incide salário".

**Atenção**

Para calcular insalubridade código de cálculo 22 sem utilizar fórmula é necessário que o funcionário tenha na movimentação o evento com código de cálculo 1 hora normal ou 2 dias trabalhados, e o evento de insalubridade deverá ter a prioridade maior.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
