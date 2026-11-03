---
content_hash: c549466895df79691b36a258cdb06008e2049d93429172ae6edc8794b9638042
fetched_at: '2026-06-29T00:10:07.904312+00:00'
page_id: '452719468'
product: rm
source: tdn-rm
title: Atrasos
type: documentation
url: https://tdn.totvs.com/display/LRM/Atrasos
version: 1
---

**Atrasos**   
**Tipo da carência de atraso:** O Sistema permite a definição do tipo de desconto da carência de atraso do funcionário. Na caixa de listagem escolha um tipo de carência:

* **Diária:** para o sistema descontar a carência das horas de atraso (valor informado no campo número de horas) dia a dia do total de horas de atraso do funcionário no dia.
* **Semanal:** para ser descontada a carência do total de atraso em cada semana do período de apuração do ponto. Desta maneira, o sistema irá considerar para o cálculo dos atrasos, somente se o total de horas de atraso da semana exceder as horas de carência.
* **Período:** para ser descontada a carência do total de atraso no período de apuração do ponto. Desta maneira, o Sistema irá considerar para o cálculo dos atrasos, somente se o total de horas exceder as horas de carência.

Caso o atraso ultrapasse a carência ele será descontado integralmente.  
   
**Observação:**  
Este campo não será considerado para o funcionário que tiver horário do tipo flexível ou núcleo.  
Para a carência de atraso semanal, o fechamento da semana se dá no dia determinado pelo campo "Dia do DSR", presente na etapa DSR do parametrizador do Sindicato.  
   
**Número de horas da carência de atraso:** Significa o valor que será utilizado para a carência do número de horas de atraso do funcionário no dia, semana ou período de apuração do ponto, conforme estiver parametrizado no campo Tipo da Carência de Atraso.  
Este campo também não será considerado para o funcionário com horário flexível ou núcleo.  
   
**Exemplos:**  
Carência de atraso = Diária   
Número de Horas = 00:20  
   
Dia   Atraso   Atraso Calculado  
05/07   00:15   00:00  
07/07   00:25   00:25  
10/07   00:20   00:00  
Total de atraso no fim do período = 00:25  
   
**Observação:**  
O sistema não calculou atraso para os dias 05/07 e 10/07, pois nesses dias o atraso não ultrapassou a carência de atraso diária de 00:20. Já no dia 07/07, o sistema calculou 00:25 de atraso pois nesse dia foi ultrapassado o limite da carência.  
   
Carência de atraso =Período  
Número de Horas = 01:00  
   
Atraso  Atraso Calculado  
Mês 1   00:55   00:00  
Mês 2   01:15   01:15  
   
**Observação:**  
O sistema não calculou atraso para o Mês 1, pois nesse mês o atraso não ultrapassou a carência de atraso por período de 01:00. Já no mês 2, o sistema calculou 001:15 de atraso pois nesse mês foi ultrapassado o limite da carência.  
   
**Abate carência do total de atrasos:** Ao habilitar esta opção o sistema passará a abater a carência do atraso do funcionário informada no campo número de horas do atraso do funcionário para os tipos de carências Diárias, Semanais e Período.
