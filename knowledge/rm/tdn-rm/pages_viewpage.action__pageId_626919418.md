---
content_hash: 77f3983fca8c85706df6135ffabeb7c53a9a0bb7f33e70680e96c7c4036bac7c
fetched_at: '2026-06-29T00:11:04.359609+00:00'
page_id: '626919418'
product: rm
source: tdn-rm
title: Rascunho_Cadastro Proposta de Extensão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=626919418
version: 1
---

O workflow ***Cadastro de Proposta de Extensão***permite ao usuário, a partir de um edital pré-definido, submeter propostas de pesquisa vinculando um planejamento de gasto e itens necessários para a realização da nova pesquisa. Essa proposta passa por uma avaliação que define sua viabilidade técnica, podendo ser aprovada ou reprovada para execução.  
    
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

* "FLUIG | Iniciar Solicitações | Educacional | Inovação, Pesquisa e Extensão | Extensão | Proposta de projeto de extensão"

Assim que o usuário com papel de "Pesquisador" (que esteja cadastrado no TOTVS Educacional como pesquisador/extensionista ativo e coordenador) acessar o processo "Proposta de projeto de extensão", ele poderá cadastrar sua proposta de projeto de extensão informando os dados do formulário. Quando o usuário informar todos campos obrigatórios do formulário e aceitar os termos para submissão de proposta de extensão, o fluxo poderá seguir dois caminhos a saber:  
 Caso seja uma proposta de edital externo (sem avaliação, ou seja, proposta de projeto autônomo), a solicitação será encaminhado para a atividade "**Avaliar projeto autônomo**", pois projetos autônomos são avaliados por usuários que possuem o papel de "Reitoria", que irá definir se será aprovado ou arquivado, mas em ambos os casos será cadastrado na base de dados da linha RM.  
 Caso seja uma proposta de edital de avaliação (edital não externo), a solicitação será encaminhada para a atividade "**Distribuir avaliação**" de responsabilidade do presidente de comissão do edital informado na proposta do projeto. Ou seja, quando o usuário da secretaria do TOTVS Educacional realizar o cadastro do edital de projetos de extensão (TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão | Edital), ele deverá definir quem será o presidente de comissão de avaliação do edital (TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão | Edital | Anexo Comissão de avaliação). Assim, todos projetos submetidos para um edital não externo, serão encaminhados diretamente para o pesquisador/extensionista cadastrado na comissão do edital como "presidente".  
 Assim que a solicitação estiver com o presidente de comissão do edital, ele poderá convidar novos pesquisadores a fazerem parte da equipe de avaliação do edital, bastando selecionar um pesquisador como possível avaliador e encaminhando a solicitação para a atividade "**Convite de comissão**". Esse convite será direcionado para o avaliador, que deverá acessar sua central de tarefas no FLUIG*,*para aceitar ou não sua participação na comissão de avaliação do edital. Depois que o possível "convidado" responder, a solicitação será direcionada novamente para o presidente de comissão do edital, permitindo que o presidente possa realizar vários convites até selecionar os avaliadores da proposta.  
 De posse da solicitação novamente, o presidente de comissão deverá selecionar os avaliadores da proposta de extensão. Ele deverá selecionar um e no máximo três avaliadores, informando a data limite e hora para realizar a avaliação da proposta e enviar a solicitação para a atividade "**Avaliar**". Caso o avaliador selecionado perca o prazo estipulado, a solicitação será redirecionada para a atividade "**Replanejamento X**", onde "**X**" será o número do avaliador selecionado, e que o presidente de comissão deverá definir um novo prazo para avaliação e/ou informar um outro avaliador na lista de avaliadores do edital. Assim que todos avaliadores realizarem a avaliação da proposta, a atividade será encaminhada para a atividade "**Avaliar proponente**". Essa atividade será direcionada para o presidente de comissão, que deverá conceder uma nota para o coordenador do projeto (o pesquisador que submeteu a proposta de projeto de extensão). Depois que o presidente de comissão enviar a solicitação para a atividade "**Processar notas**", o sistema irá calcular a nota do projeto (obtida pela média de notas dos avaliadores e multiplicada pelo peso definido no edital) e verificar se está abaixo do mínimo exigido no edital para aprovação. Caso a nota seja abaixo do mínimo exigido no edital, o projeto será arquivado automaticamente e o fluxo será encerrado com o projeto arquivado por insuficiência de nota.  
 Caso o projeto obtenha uma nota superior ao mínimo exigido no edital, a solicitação será encaminhada para a atividade "**Avaliação Final**", que será de responsabilidade do papel de "Reitoria", que deverá realizar a aprovação/reprovação final do projeto. Ou seja, mesmo que o projeto obtenha nota superior ao exigido no edital, o usuário que possuir papel de "Reitoria" poderá reprovar estes projetos. Caso o projeto seja aprovado pelo pela reitoria, ele será classificado com a situação "Em Execução", permitindo ao coordenador do projeto solicitar outras atividades, tais como: "Cadastrar bolsistas" e "[Acompanhar projeto de extensão](http://tdn.totvs.com/display/LRM/DT_ACOMPANHAMENTO_EXTENSAO)".  
    
 Para visualizar o fluxo completo, segue abaixo o diagrama de atividades para ter uma visão mais clara do processo descrito.  
    
  

 Informações Complementares

---

[Documento Técnico - Cadastro Projeto Pesquisa e Extensão](http://tdn.totvs.com/display/LRM/DT_CADASTRO_PROPOSTA_EXTENSAO)
