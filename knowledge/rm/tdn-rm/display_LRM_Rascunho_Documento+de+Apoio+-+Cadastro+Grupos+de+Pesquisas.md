---
content_hash: 45f8b99f7e140e7afa75de205b8942c431b0622db63201c2375ab180ce1de6be
fetched_at: '2026-06-29T00:11:04.410103+00:00'
page_id: '626919512'
product: rm
source: tdn-rm
title: Rascunho_Documento de Apoio - Cadastro Grupos de Pesquisas
type: documentation
url: https://tdn.totvs.com/display/LRM/Rascunho_Documento+de+Apoio+-+Cadastro+Grupos+de+Pesquisas
version: 1
---

O Cadastro do Grupo de Pesquisa, possibilita ao usuário gerenciar seus processos referentes a um grupo, onde através desde, permitirá cadastrar, submeter à análise e avaliar o Grupo de Pesquisa, utilizando o processo de aprovação através de FLUIG.  
 ð O usuário deve iniciar uma nova solicitação escolhendo a opção "Educacional | Inovação, Pesquisa e Extensão | Grupos de Pesquisa | Grupos de Pesquisa". É necessário estar vinculado ao papel de "Pesquisador" para realizar essa solicitação.  
 ð  Criar no FLUIG os papéis necessários para a execução do fluxo do projeto de inovação. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis.  
 §   Código = pesquisador | Descrição = Pesquisador  
 §   Código = reitoria | Descrição = Reitoria  
 §   Código = pro-reitoria | Descrição = Pró-Reitoria  
 Em seguida, associar os usuários aos respectivos papéis cadastrados.  
 ð Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.  
    
 ð Importar o fluxo: Cadastro Grupos de Pesquisa para a ferramenta TOTVS Developer Studio (TDS).   
 Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em c:\totvs\CorporeRM\ObjetosGerenciais\Fluig.  
 ·       
 **Descrição do Processo:**  
 Logar com o usuário associado ao papel de: "Pesquisador" e iniciar uma nova solicitação no FLUIG, escolhendo a opção:

* "FLUIG | Iniciar Solicitações | Educacional | Inovação, Pesquisa e Extensão | Grupos de Pesquisa | Grupos de Pesquisa"

O formulário de cadastro será aberto com o código do pesquisador vinculado ao usuário do FLUIG, sendo esse o usuário que será cadastrado como solicitante do grupo no TOTVS Educacional.  
 Após preencher as informações do cadastro o usuário enviará a solicitação para "Confirmar Cadastro Grupo", onde um usuário, vinculado ao papel de "Reitoria", vai verificar as informações preenchidas.  
 Nessa etapa, o usuário vinculado ao papel de "Reitoria" terá três opções:  
 §   Avançar etapa para "Cadastro de Grupo Reprovado"  
 O grupo não será cadastrado e uma justificativa deverá ser informada pelo usuário vinculado ao papel de "Reitoria". O fluxo é concluído.  
    
 §   Avançar etapa para "Cadastrar Grupo CNPq"  
 O grupo será cadastrado no TOTVS Educacional e passará para etapa onde o usuário vinculado ao papel de "Reitoria" solicitará o cadastro no CNPq.  
    
 §   Avançar etapa para "Aprovação Cadastro Grupo".  
 Caso seja necessário, o usuário vinculado ao papel de "Reitoria" poderá solicitar uma segunda aprovação do cadastro para a Pró-reitoria. Outro usuário vinculado ao papel de "Pró-reitoria" terá duas opções:  
                 ·  Avançar etapa para "Cadastrar Grupo CNPq"  
 O grupo será cadastrado no TOTVS Educacional e passará para etapa onde o usuário vinculado ao papel de "Reitoria" solicitará o cadastro no CNPq.  
             ·  Avançar etapa para "Cadastro de Grupo Reprovado"  
 O grupo não será cadastrado e uma justificativa deverá ser informada pelo usuário vinculado ao papel de "Reitoria". O fluxo é concluído.  
    
 Ao chegar na etapa de "Certificar Grupo CNPq"o usuário vinculado ao papel de "Reitoria" solicitará a certificação no CNPq (entidade e/ou sistema externo ao fluxo) e enviará o fluxo para a etapa final, onde será concluído.  
    
 Durante toda a execução do fluxo são gerados registros de histórico por etapa. Esse histórico é gravado na tabela SPESCONFIRMAGRUPO e contém informações sobre o usuário que movimentou a etapa, qual etapa foi movimentada, data da movimentação, justificativas, dentre outras.  
    
 Para visualizar o fluxo completo, segue abaixo o diagrama de atividades para ter uma visão mais clara do processo descrito.  
    
    
   
 

Informações Complementares

---

[Documento Técnico - Cadastro de Grupos de Pesquisas](http://tdn.totvs.com/display/LRM/DT_GRUPOS_DE_PESQUISA)
