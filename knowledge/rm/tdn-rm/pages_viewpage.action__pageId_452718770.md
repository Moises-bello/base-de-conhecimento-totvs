---
content_hash: fe660c5785fe02e1a1f465ffb5e81942695f826e48ca1a67e4f7adf9dae5b572
fetched_at: '2026-06-29T00:10:01.544136+00:00'
page_id: '452718770'
product: rm
source: tdn-rm
title: Código de Cálculo 190 - Retificação de SEFIP 13º Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718770
version: 2
---

Neste evento será pago / informado o valor da diferença de remuneração de 13º salário referente ao período a ser retificado.   
 Evento tipo Provento, valor, calculado por fórmula e sem incidências em INSS13 e FGTS13.  
 Para o caso de recolhimentos de diferenças pagas na competência atual (pois na época o pagamento foi menor) cujos valores de FGTS13 e/ou INSS13 devem ser recolhidos em atraso.   
 Evento tipo Base de Cálculo, valor, calculado por fórmula e sem incidências.  
 Para o caso de recolhimento efetuado a menor na época do pagamento, onde o pagamento foi feito corretamente, mas as bases informadas no SEFIP estavam incorretas.

**Observações**

1) Quando o evento com "Código de Cálculo 189-RETIFICAÇÃO SEFIP" for do tipo "Base de Cálculo", não poderá ter nenhuma incidência (INSS, FGTS, IRRF, INFORME DE RENDIMENTOS, RAIS, ETC), ou seja, os eventos de retificação (proventos ou descontos) sem o CC189, deverão ter a incidência em IRRF (estorna ou incide), porque estes eventos de retificação serão utilizados para pagamento/desconto do funcionário e depois somados por fórmula para serem informados nos eventos de base de cálculo com CC 189.

2) Os eventos com código de cálculo 189 e 190 não serão somados à base de INSS e FGTS na folha analítica, nas variáveis de fórmulas que busca as bases e nos encargos.  
    
 **Dica**

Criar um evento para cada competência a que a retificação se referir.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
