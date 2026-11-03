---
content_hash: a2f5e36a125d2da8a36420daca646139f73e99d6acd3979794498a99429e3bb1
fetched_at: '2026-06-29T00:10:10.565896+00:00'
page_id: '452719877'
product: rm
source: tdn-rm
title: Gerar Gatilhos Afastamento/Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719877
version: 2
---

Esse processo permite gerar gatilhos de afastamento e férias do evento S-2230- Afastamento.   
    
 Gerar Gatilho de Férias  
 Ao marcar este parâmetro será habilitado os campos referentes ao períodos de férias:

* *Férias iniciadas e finalizadas no período*: Informe o período inicial e final de férias que deseja gerar o gatilho. Este período informado não pode ser superior a 60 dias. Caso o usuário informe uma data que ultrapasse esses 60 dias, o sistema emite uma mensagem de erro e não permite gerar o Gatilho de Férias.

**Exemplo**  
 01/06/2018 a 31/07/2018 - será gerado gatilhos de todos os funcionários que tiverem férias iniciadas e finalizadas dentro desta data.

* *Férias iniciadas entre*: Informe um período de inicio de férias que deseja gerar o gatilho. O sistema irá considerar todas as férias iniciadas dentro do período informado, independente da data final de férias.

**Exemplo**  
 01/06/2018 a 30/06/2018 - será consideradas todas os funcionários que tiveram férias iniciadas dentro desta data.

* *Férias finalizadas entre*: Informe um período de fim de férias que deseja gerar o gatilho. O sistema irá considerar todas as férias finalizadas dentro do período informado, independente da data inicial de férias.

**Exemplo**  
 01/06/2018 a 30/06/2018 - será consideradas todos os funcionários que tiveram férias finalizadas dentro desta data.  
 **Observação**  
 Quando é informado qualquer um dos períodos acima, os demais ficam desabilitados. Para habilitar outro período, basta limpar o período selecionado ou desmarcar e marcar o parâmetro 'Gerar Gatilho de Férias'  
 **Atenção:**

* Ao incluir um afastamento que já possua data de término o sistema irá gerar (02) dois gatilhos um de inclusão que levará somente os dados do início do afastamento e o outro de término para finalizar o afastamento.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Eventos Não Periódicos
