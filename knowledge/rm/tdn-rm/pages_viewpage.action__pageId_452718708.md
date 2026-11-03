---
content_hash: e51904a248595b3012b572a0605d533965798b919bba1efbf48e180239d9c038
fetched_at: '2026-06-29T00:10:01.376108+00:00'
page_id: '452718708'
product: rm
source: tdn-rm
title: Código de Cálculo 313 - Jornada Mensal Considerando Horas Trabalhadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718708
version: 2
---

O evento com este código de cálculo tem o mesmo tratamento de um evento sem código de cálculo, ou seja, são considerados os tipos (hora/dia/valor) e o percentual de incidência.  
 A diferença é quando o evento é do tipo hora, neste caso no cálculo do salário hora são consideras as horas efetivamente trabalhadas.  
 **Exemplo:**  
 Evento sem código de cálculo  
 O cálculo é feito com a divisão do salário mensal / jornada mensal informada no cadastro do funcionário.  
    
 Evento com código de cálculo 313  
 O cálculo é feito com a divisão do salário mensal / jornada efetivamente trabalhada.   
 Esta jornada verifica do primeiro ao último dia da competência, quantas horas efetivamente o funcionário trabalhou, sem considerar o intervalo noturno, dias de compensação e descanso e considerando feriados.

**Atenção:**

1. São excluídos os dias em que o funcionário está afastado ou de férias.   
    
 2. O valor da jornada efetivamente trabalhada é calculada pelo RMChronus.   
    
 3. Para quem não utiliza o RMChronus, a jornada é considerada como zero, e o evento com código de cálculo 313 não é calculado.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
