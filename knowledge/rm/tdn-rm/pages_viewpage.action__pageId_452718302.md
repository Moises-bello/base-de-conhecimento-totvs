---
content_hash: 39a26b49a205582418825c02904db5722075f94b10b0519c4f55835db4984bb7
fetched_at: '2026-06-29T00:09:59.332522+00:00'
page_id: '452718302'
product: rm
source: tdn-rm
title: Código de Cálculo 1 - Horas Normais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718302
version: 3
---

Este código de cálculo corresponde à remuneração de um dia de trabalho para qualquer que seja a forma de pagamento. Para funcionários horistas, o sistema considera o número real de dias trabalhados do mês ( 28 a 31 dias), para mensalistas o sistema considera sempre 30 dias e para empregados tarefeiros ou comissionistas puros sempre será considerado zero.   
Provento do tipo hora com porcentagem de incidência igual a 1,00. O cálculo será feito da seguinte forma:

(SALARIO MES / HORAS MES) \* No. DE HORAS INFORMADO

O Sistema buscará o salário mensal em Cadastros | Funcionários | Base de Cálculo, dividirá pelo número de horas da jornada no mês (cadastro de Funcionários, mesma pasta citada anteriormente) e multiplicará pelo número de horas informado neste evento.

**Observação**

Para os funcionários mensalistas, mesmo que seja informado o número de horas da jornada mensal (mesmo cadastro já citado), automaticamente o sistema recalculará as horas, no caso de admissão, demissão e funcionários afastados.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
