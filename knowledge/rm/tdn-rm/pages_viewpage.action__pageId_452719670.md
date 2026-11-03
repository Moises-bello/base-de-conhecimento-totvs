---
content_hash: 99fb851b9b6ee8c1f0c26f5eb7c250d9288b1740a98f125d1f72897c9d02c881
fetched_at: '2026-06-29T00:10:09.445426+00:00'
page_id: '452719670'
product: rm
source: tdn-rm
title: Código de Cálculo 189 - Retificação de SEFIP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719670
version: 2
---

Neste evento será pago / informado o valor da diferença de remuneração referente ao período a ser retificado.   
 Evento tipo Provento, valor, calculado por fórmula e sem incidências em INSS e FGTS.  
 Para o caso de recolhimentos de diferenças pagas na competência atual (pois na época o pagamento foi menor) cujos valores de FGTS e/ou INSS devem ser recolhidos em atraso.   
 Evento tipo Base de Cálculo, valor, calculado por fórmula e sem incidências.  
 Para o caso de recolhimento efetuado a menor na época do pagamento, onde o pagamento foi feito corretamente, mas as bases informadas no SEFIP estavam incorretas.

**Observações**

1) Quando o evento com "Código de Cálculo 189-RETIFICAÇÃO SEFIP" for do tipo "Base de Cálculo", não poderá ter nenhuma incidência (INSS, FGTS, IRRF, INFORME DE RENDIMENTOS, RAIS, ETC), ou seja, os eventos de retificação (proventos ou descontos) sem o CC189, deverão ter a incidência em IRRF (estorna ou incide), porque estes eventos de retificação serão utilizados para pagamento/desconto do funcionário e depois somados por fórmula para serem informados nos eventos de base de cálculo com CC 189.

2) Os eventos com código de cálculo 189 e 190 não serão somados à base de INSS e FGTS na folha analítica, nas variáveis de fórmulas que busca as bases e nos encargos.

3) Os eventos com código de cálculo 189 do tipo provento ou desconto mesmo quando não incidirem em INSS terão o campo "Grupo AAS" habilitado, desde que o parâmetro "Usa AAS discriminado" existente em Opções | Parâmetros | RM Labore | Outros Parâmetros | Parâmetros II esteja habilitado. E é de extrema importância informar o grupo de AAS no evento.  
 Quando o parâmetro não estiver marcado, os eventos serão considerados no grupo 0.

**Dica**

Criar um evento para cada competência a que a retificação se referir.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
