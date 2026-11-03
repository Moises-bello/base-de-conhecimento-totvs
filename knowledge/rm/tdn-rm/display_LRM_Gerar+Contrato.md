---
content_hash: b6355470dabd6126d9d1238840f91a3748b7a42f53d66fd2b0afe0c039819e26
fetched_at: '2026-06-29T00:09:16.270000+00:00'
page_id: '421385500'
product: rm
source: tdn-rm
title: Gerar Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerar+Contrato
version: 3
---

Após realizar a equalização e as negociações da concorrência eletrônica, deve-se abrir o projeto vencedor e realizar geração do contrato a partir da licitação vencedora. Ao executar o processo de geração do contrato, a partir do projeto vencedor da licitação, irá criar um novo contrato do tipo Serviço no projeto origem da licitação, com todas as tarefas associadas ao contrato, e os seus receptivos valores.   
    
 O contrato gerado estará vinculado ao projeto pai do projeto vencedor, com o campo código da licitação preenchido com o código do projeto vencedor.  
 O campo Cliente Fornecedor estará desabilitado para edição, quando estiver preenchido com o código CNPJ do fornecedor estiver selecionado. Caso o Fornecedor não esteja cadastrado na base, o campo de Cliente Fornecedor será habilitado dando opção ao usuário de selecionar um outro fornecedor. Caso o CNPJ do Fornecedor selecionado no campo não seja o mesmo do Lookup, será disparado um alerta informado ao usuário a diferença.  
    
 **Observação:**  
 Caso o projeto esteja integrado com ECM e o usuário estiver corretamente configurado com o tipo de atendimento, ao gerar o contrato será exibida uma mensagem informando que o workflow de aprovação do atendimento foi criado para o contrato.  
 Caso o usuário não estiver corretamente configurado com o tipo de atendimento será exibida uma mensagem validando que o usuário ECM não está associado ao usuário do RM.
