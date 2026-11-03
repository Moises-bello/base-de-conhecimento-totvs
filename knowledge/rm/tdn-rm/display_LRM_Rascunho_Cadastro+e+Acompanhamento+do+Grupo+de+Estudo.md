---
content_hash: 17c8986612bf749a37fe1705be919d845e42c4a51f659e4d82c04c4664fd45db
fetched_at: '2026-06-29T00:11:04.352436+00:00'
page_id: '626919394'
product: rm
source: tdn-rm
title: Rascunho_Cadastro e Acompanhamento do Grupo de Estudo
type: documentation
url: https://tdn.totvs.com/display/LRM/Rascunho_Cadastro+e+Acompanhamento+do+Grupo+de+Estudo
version: 1
---

O Workflow ***Cadastro e Acompanhamento do Grupo de Estudo***, tem como objetivo possibilitar o usuário gerenciar seus processos referentes a criação/acompanhamento de grupos de estudo, permitindo realizar o cadastro, submeter a análise e avaliação utilizando-se do processo de aprovação através de FLUIG.  
    
 Antes de iniciar o processo, o usuário terá que:   
    
 Criar no FLUIG os papéis necessários para a execução do fluxo do projeto de inovação. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis.  
     Código = pesquisador | Descrição = Pesquisador

   Código = reitoria | Descrição = Reitoria  
    
 Em seguida, associar os usuários aos respectivos papéis cadastrados.  
    
 Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.  
    
 Importar o fluxo: Cadastro de Proposta de Extensão para a ferramenta TOTVS Developer Studio (TDS).   
 Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em c:\totvs\CorporeRM\ObjetosGerenciais\Fluig.  
 ·       
 **Descrição do Processo:**  
 Logar com o usuário associado ao papel de: "Pesquisador" e iniciar uma nova solicitação no FLUIG, escolhendo a opção:

* "FLUIG | Iniciar Solicitações | Educacional | Inovação, Pesquisa e Extensão | Grupos de Estudo"

O formulário de cadastro será aberto com o código do pesquisador vinculado ao usuário do FLUIG, sendo esse o usuário que será cadastrado como solicitante do grupo no TOTVS Educacional.  
 Após preencher as informações do cadastro o usuário enviará a solicitação para "Solicitar Aprovação", onde um usuário, vinculado ao papel de "Reitoria", vai verificar as informações preenchidas.  
 Nessa etapa, o usuário vinculado ao papel de "Reitoria" terá duas opções:  
    ·  Avançar etapa para "Solicitação Reprovada" O grupo de estudo será cadastrado mas não será aprovado e um parecer deverá ser informado pelo usuário vinculado ao papel de "Reitoria". O fluxo é concluído.  
    ·  Avançar etapa para "Solicitação Aprovada" O grupo de estudo será cadastrado como aprovado no TOTVS Educacional. O fluxo é concluído.  
    
   
           
 Após a conclusão do fluxo acima, logar com o usuário associado ao papel de: "Pesquisador" e iniciar uma nova solicitação no FLUIG, escolhendo a opção:

* "FLUIG | Iniciar Solicitações | Educacional | Inovação, Pesquisa e Extensão | Acompanhamento Grupos Estudo | Acompanhamento Grupos Estudo"

Para o correto funcionamento desse fluxo, o grupo de estudo já deve estar cadastrado e aprovado, conforme descrito no primeiro fluxo acima.  
 O formulário de acompanhamento será aberto e mostrará apenas os grupos de estudo que estiverem relacionados ao usuário logado no FLUIG.  
 Após preencher as informações do acompanhamento o usuário enviará a solicitação para "Atividade Cadastrada", onde as informações serão atualizadas no TOTVS Educacional e o fluxo será concluído.  
    
   
    
  

 Informações Complementares

---

[Documento Técnico - Cadastro e Acompanhamento de Grupos de Estudo](http://tdn.totvs.com/display/LRM/DT_GRUPOS_DE_ESTUDO)
