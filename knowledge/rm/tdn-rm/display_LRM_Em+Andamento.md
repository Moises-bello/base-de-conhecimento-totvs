---
content_hash: 1dd2646e9a5fdcfe086023641bcec20dac47a002d79a344e89a1fc5adc84a911
fetched_at: '2026-06-29T00:09:30.729935+00:00'
page_id: '425458491'
product: rm
source: tdn-rm
title: Em Andamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Em+Andamento
version: 3
---

**Em Andamento**   
O processo é responsável por inserir o atendimento no status do atendimento, mas antes de executar o processo  o sistema verifica se o mesmo pode ser executado, caso contrário uma mensagem é apresentada interrompendo a execução.  
   
Somente atendimentos com os status: Concluído a Responder, Concluído Respondido, Agendado a Responder, Agendado Respondido, Aguardando Terceiros, Despertado podem ser colocados em andamento. Caso o status do atendimento seja Concluído Automático (pelo sistema) ou Concluído Confirmado, esse processo somente poderá ser executado pelo chefe do responsável, ou por um atendente com permissão no perfil para colocar em andamento independente de ser chefe.   
   
Se o Prazo Limite do atendimento for maior que a data atual e o status for diferente de "Agendado", "Concluído a Confirmar" e "Aguardando Terceiros" então o novo status será "Despertado", caso contrário será "Em Andamento".  
   
Se o status atual do atendimento for "Despertado" então o novo status será "Em Andamento".  
   
Se o status atual do atendimento for "Agendado (a Responder)" então retorna a data de prazo limite para a data de prazo limite anterior (ou NULL caso ela não esteja preenchida).  
   
Os campos do atendimento são atualizados: Data de Fechamento, Prazo Limite anterior e Agendado para são alterados para NULL, Data de Início real é alterado para data atual (caso ela não esteja preenchida),  Data de Prazo Limite é alterado de acordo com a regra acima e novo status do atendimento é atualizado de acordo com a regra citada acima.  
   
No histórico de status um registro é inserido.
