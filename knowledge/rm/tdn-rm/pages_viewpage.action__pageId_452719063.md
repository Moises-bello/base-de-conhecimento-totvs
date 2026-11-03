---
content_hash: cf5306eee5a0c04f62d4565acd103efacf81431d878728d1f92ff71f4130f2de
fetched_at: '2026-06-29T00:10:03.234424+00:00'
page_id: '452719063'
product: rm
source: tdn-rm
title: Código de Cálculo 352 - Salário Maternidade Complementar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719063
version: 2
---

Este código de cálculo corresponde à remuneração de um dia de trabalho para qualquer que seja a forma de pagamento. Para funcionários horistas, o sistema considera o número real de dias do mês ( 28 a 31 dias), para mensalistas o sistema considera sempre 30 dias e para empregados tarefeiros ou comissionistas puros sempre será considerado zero.

Provento do tipo hora com porcentagem de incidência igual a 1,00. O cálculo será feito da seguinte forma:  
 (SALARIO MES / HORAS MES) \* No. DE HORAS INFORMADO  
 O Sistema buscará o salário mensal em Cadastros | Funcionários | Base de Cálculo, dividirá pelo número de horas da jornada no mês (cadastro de Funcionários, mesma pasta citada anteriormente) e multiplicará pelo número de horas informado neste evento.  
 Para os funcionários mensalistas, mesmo que seja informado o número de horas da jornada mensal (mesmo cadastro já citado), automaticamente o sistema recalculará as horas, no caso de admissão, demissão e funcionários afastados.

**Observações:**

Durante o período de afastamento do tipo W - Licença Maternidade Complementar, a funcionária estava recebendo o salário através dos Códigos de Cálculo 1 ou 2.  
 Conforme a Lei, "A pessoa jurídica tributada com base no lucro real poderá deduzir do imposto devido, em cada período de apuração, o total da remuneração integral da empregada pago nos 60 (sessenta) dias de prorrogação de sua licença-maternidade, vedada a dedução como despesa operacional".  
    
 Com o cálculo sendo feito nos eventos de CC's 1 ou 2 ficava complicado de separar o valor para fazer a dedução.  
 Foi implementado o novo CC 352 - SALÁRIO MATERNIDADE COMPLEMENTAR, para lançar somente o valor referente ao período de afastamento tipo W.  
    
 Este evento terá as mesmas características dos eventos de remuneração, CC's 1 e 2, e será lançado automaticamente pelo sistema junto com estes CC's.
