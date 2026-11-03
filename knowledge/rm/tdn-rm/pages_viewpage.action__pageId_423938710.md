---
content_hash: 02e610cccd2bbd82c90cba324c8f9451b82f2d19e44d91e4f62641635889ea33
fetched_at: '2026-06-29T00:09:28.570755+00:00'
page_id: '423938710'
product: rm
source: tdn-rm
title: Agendamento de Mão-de-Obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938710
version: 4
---

O agendamento técnico da OS tem como objetivo o controle de agenda do técnico que irá realizar os serviços nas OS. Com esse controle poderá ser definido a data para agendamento da execução do serviço pelo técnico no momento de alocação de mão de obra no serviço.  
    
 **Parametrização**

Para que esta funcionalidade possa ser utilizada é necessário marcar o parâmetro "Controla Agendamento Técnico" que se encontra no menu Opções | Parâmetros | Sistema | aba Ordem de Serviço.  
Para que este parâmetro fique visível para o usuário marca-lo, será necessário marcar também o parâmetro "Controla Alocação de Mão de obra".   
Além de marcar o parâmetro o usuário deverá ter permissão de acesso para Inserir, editar e excluir um agendamento, essa permissão é dada no menu Cadastro | Segurança | Perfil escolhendo o perfil do usuário.

**Processo de Agendamento Técnico**

Para realizar um agendamento técnico basta acessar a tela de alocação de mão de obra, selecionar a mão de obra e clicar em "Agendamento de Mão Obra".   
O sistema irá abrir um WIZARD. Na primeira tela serão exibidos na grid os agendamentos realizados para a mão de obra selecionada, clique em avançar.   
Na próxima tela será feito o agendamento. Selecione uma data inicial e uma data final e preencha o campo observação.   
O sistema irá calcular a data final de acordo com o tempo previsto para a realização do serviço cadastrado na aba Integração, no campo "Tempo de serviço" no cadastro de produtos/serviços.  
Se o usuário não quiser seguir o tempo calculado pelo sistema com base no tempo de realização do serviço ele poderá alterar esse tempo no momento de inserir os dados do agendamento.  
Depois que o agendamento é criado ele pode ser visualizado através do menu Mão de Obra | Agenda da Mão de Obra.   
Ao clicar nesse menu será aberto uma grid com todos os agendamentos realizados. É possível visualizar o numero da OS, a data de início e fim do agendamento, o serviço dentre outros dados. Selecionando o agendamento e clicando em Anexo é possível visualizar o item da OS e clicando no anexo do item da OS é possível também iniciar, interromper, terminar os apontamentos e efetuar desconto/despesa para o item da OS.

***Observação***:   
Caso já exista um agendamento de serviço para o técnico na data informada, o sistema irá exibir mensagem ao usuário informando que já existe um agendamento naquela data.  
A data inicial do agendamento deverá ser maior que a data de emissão da OS.  
A data final do agendamento deverá ser maior que a data inicial.  
Ao excluir a alocação de mão de obra o sistema irá verificar se existe agendamento para o técnico e caso exista o mesmo será excluído.  
Ao excluir a OS o sistema irá verificar se existe agendamento para o técnico e caso exista o mesmo será excluído. Não poderão existir registros de agendamento sem que aja uma OS para este agendamento.
