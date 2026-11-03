---
content_hash: 9940996ba8a283bccd9d24e597c775858d9d282dbe64b4eb7e06f545d9e54577
fetched_at: '2026-06-29T00:09:30.780810+00:00'
page_id: '425458521'
product: rm
source: tdn-rm
title: Processo “Executar Operação de Telemarketing”
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458521
version: 1
---

**Processo "Executar Operação de Telemarketing"**

---

O processo consiste no registro do contato realizado com o cliente através da operação telefônica. Informações básicas do cliente (Nome, Nome fantasia e Telefone) são apresentadas como somente leitura apenas para consulta assim como o Script de Telemarketing, mas os campos: Não houve com o Cliente, Data de Agendamento, Motivo da Falta de Contato, Tipo de Ação, Retorno do Cliente, Conversa e Parâmetros são editáveis para que a operação possa ser executada e registrada.  
   
Caso a operação seja agendada, o registro passa a ser verificado através do filtro Clientes Agendados ou pode ser finalizada e passará para o filtro de Clientes Concluídos.  
   
A flag "Não houve contato com o Cliente" define quando o contato não foi possível ou quando o cliente deseja realizar esse contato em uma data futura.   
   
A "Data do Agendamento" deve ser utilizada para selecionar a data para o futuro contato que o próprio cliente solicitou ou porque o contato não foi feita com sucesso e será realizado na data selecionada, esse campo apenas será habilitado somente quando a flag "Não houve contato com o Cliente"  estiver **marcada.**  
   
"Motivo da falta de contato" informa o motivo do contato com o cliente não ter sido possível, esse campo também apenas será habilitado quando a flag "Não houve contato com o cliente" estiver **marcado**.  
   
"Tipo de ação" lista os tipos de ações que estão associadas a campanha que esta sendo realizada a operação de telemarketing, este campo estará habilitado somente se o campo "Não houve contato com o cliente" estiver **desmarcado**.  
   
"Retorno do cliente" deve ser selecionado de acordo com a resposta dada pelo cliente, esse campo apenas estará habilitado somente "Não houve contato com o cliente" estiver **desmarcado.**  
   
"Script de telemarketing" mostra o script associado ao tipo de ação. O script é um roteiro que pode ser usado pelo atendente durante a conversa com o cliente, esse campo não pode ser editado.  
   
"Adicionar script telemarketing" é um botão que quando acionado copia o texto do campo "Script de Telemarketing" para o campo "Conversa".   
   
"Conversa" campo de texto livre onde o atendente descreve como foi a conversa com o cliente ou qualquer outro detalhe que ele considere importante para essa operação de telemarketing.
