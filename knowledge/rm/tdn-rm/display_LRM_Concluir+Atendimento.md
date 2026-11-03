---
content_hash: 87e23d9943cdeab1f60bee78ac23e54aade17008064d20eebadbff16ff453b8b
fetched_at: '2026-06-29T00:09:30.704252+00:00'
page_id: '425458473'
product: rm
source: tdn-rm
title: Concluir Atendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Concluir+Atendimento
version: 1
---

**Concluir Atendimento**   
Este processo indica que a solicitação do atendimento foi solucionada e que deve ser informado ao cliente. Ele exige o preenchimento do campo solução onde deve ser detalhado os procedimentos para a solução da solicitação ou, se havia algum problema com o produto, o que foi feito para solucioná-lo. Pode ocorrer soluções paliativa antes do acerto definitivo no produto.   
   
Então o atendimento é encaminhado para o atendente responsável pelo contato com o cliente afim de que o mesmo seja avisado da finalização/solução de sua solicitação.  
Para executar o processo, os atendimentos que serão sofrer a conclusão devem ser selecionados e o processo executado, o sistema apresentará uma interface com a lista de atendimentos que foram selecionados e com o campo atendente disponível para preencher o responsável pela conclusão.   
   
Caso o campo do atendimento "Atendente que Concluiu" esteja preenchido, o campo "Atendente Responsável pela Conclusão" virá preenchido com esse valor.  Essa regra aplica-se apenas para conclusão de atendimentos individuais, ou seja, caso tenha sido selecionado mais de um atendimento para conclusão, esse campo virá em branco.  
   
 É verificado se o atendimento pode ser concluído a responder, caso não seja, a execução do processo é interrompida e gerada uma mensagem de aviso;  
   
Verifica se os campos solicitação e solução estão preenchidos, caso contrário o processo é interrompido enviando uma mensagem sobre o preenchimento de tais campos;  
   
 Verificado o número de mensagens na caixa postal do atendimento. Se houverem mensagens então o processo é interrompido e uma mensagem relacionada é enviada;  
   
Ele altera o status no histórico de status;  
   
Repassa o atendimento para o atendente responsável pelo contato com o cliente para que o mesmo possa avisá-lo sobre a conclusão do atendimento(que foi dada uma solução para a solicitação);  
   
Atualiza o status do atendimento para concluído a responder e o percentual de concluído para 100%.
