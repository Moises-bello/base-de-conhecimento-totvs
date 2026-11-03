---
content_hash: 7be5f74af0f01808d113e9156f5f497906e1e28e67a5a482b859dc9414222b42
fetched_at: '2026-06-29T00:11:04.344703+00:00'
page_id: '626919370'
product: rm
source: tdn-rm
title: Rascunho_Acompanhamento do Projeto de Extensão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=626919370
version: 1
---

O ***Acompanhamento do Projeto de Extensão***, possibilita o Pesquisador do projeto enviar a proposta de Extensão para que a mesma seja avaliada.   
 Caso o projeto seja uma solicitação 'extraordinária' (Solicitação mudança no projeto original para dados da "equipe" e/ou "plano de trabalho") onde o projeto será encaminhado para o usuário que tenha o papel de *reitoria* que irá definir se a mudança será aprovada ou reprovada.  
 Caso o projeto seja uma solicitação de 'acompanhamento' (Relatório parcial/final), onde o projeto será encaminhando para o usuário que tenha o papel de *presidente da comissão* que irá avaliar o projeto de extensão.  
 Antes de iniciar o processo, o usuário terá que:   
 ð Criar no FLUIG os papéis necessários para a execução do fluxo do projeto de inovação. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis.  
    
 §   Código = pesquisador | Descrição = Pesquisador  
 §   Código = reitoria | Descrição = Reitoria   
 §   Código = secretaria| Descrição = Secretaria  
    
 Em seguida, associar os usuários aos respectivos papéis cadastrados.  
    
 ð Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.  
    
 ð Importar o fluxo: Cadastro projeto de Pesquisa Extensão para a ferramenta TOTVS Developer Studio (TDS).   
 Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em c:\totvs\CorporeRM\ObjetosGerenciais\Fluig.  
    
    
 **Descrição do Processo:**  
 Logar com o usuário associado ao papel de:"Pesquisador" e iniciar uma nova solicitação no FLU IG, escolhendo a opção:

* "FLUIG | Iniciar Solicitações | Educacional | Inovação, Pesquisa e Extensão | Extensão | Acompanhamento Projeto de Extensão"

Assim que o usuário pesquisador (coordenador do projeto) estiver algum projeto de extensão com situação "Em execução" (submeteu o projeto de extensão e foi aprovado), ele poderá acessar o fluige cadastrar seu acompanhamento do projeto de extensão informando os dados do formulário. Quando o usuário informar todos campos obrigatórios do formulário e aceitar os termos para submissão de acompanhamento da proposta de extensão, o fluxo poderá seguir dois caminhos a saber:  
 ð Caso seja uma "solicitação extraordinária" (solicitação de mudança no projeto original para dados da "equipe" e/ou "plano de trabalho"), a solicitação será encaminhada para a atividade "**Avaliar solicitação extraordinária**", pois todas solicitações de mudança no projeto original serão avaliadas pelo papel de "Reitoria", que irá definir se a mudança será aprovada ou reprovada, mas caso seja aprovado, os dados (equipe e/ou plano de trabalho) serão alterados no projeto original.  
 ð Caso seja um "acompanhamento" (relatório parcial/final), a solicitação será encaminhada para a atividade "**Avaliar acompanhamento**", que será de responsabilidade do presidente de comissão do edital informado na proposta do projeto. Ou seja, quando o usuário da secretaria do TOTVS Educacional realizar o cadastro do edital de projetos de extensão (TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão | Edital), ele deverá definir quem será o presidente de comissão de avaliação do edital (TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão | Edital | Anexo Comissão de avaliação). Assim, todos acompanhamentos de projetos para um edital não externo, serão encaminhados diretamente para o pesquisador/extensionista cadastrado na comissão do edital como "presidente". Este usuário deverá realizar a avaliação do acompanhamento (tanto para relatório parcial quanto para final), e poderá solicitar uma retificação das informações, encaminhando a atividade "**Retificar**", onde o coordenador do projeto deverá realizar as alterações e encaminhar novamente para o presidente da comissão, que poderá reprovar ou aprovar a solicitação encaminhando a solicitação para a atividade "**Aprovado**". Caso seja um relatório **parcial**, a solicitação será finalizada e o coordenador do projeto poderá enviar novo acompanhamento de projeto de extensão. Em contrapartida, caso seja um relatório **final**, a solicitação será encaminhada para a atividade "**Aprovação final**", que será de responsabilidade do papel de "Reitoria", que poderá definir quatro saídas para o andamento da solicitação, são elas:  
    ·  **Retificar**: Caso o usuário com papel de reitoria encaminhe para essa atividade, o fluxo será encaminhado para o solicitante (usuário que solicitou o acompanhamento do projeto) para que ele possa realizar as devidas alterações no acompanhamento, e posteriormente retornar para o usuário que solicitou a retificação do acompanhamento.   
    ·  **Reprovado**: Caso o usuário com papel de reitoria encaminhe para essa atividade, o fluxo será encerrado e o acompanhamento receberá a situação de reprovado, tendo o coordenador do projeto solicitar um novo acompanhamento de relatório final para seu projeto de extensão.   
    · **Emitir certificado**: Caso o usuário com papel de reitoria encaminhe para essa atividade, o usuário com papel de "Secretaria" deverá assumir a tarefa e acessar o TOTVS Educacional para a geração dos certificados inseridos no sistema em "TOTVS Educacional | Atividades acadêmicas | Certificados". Depois que todos certificados forem emitidos, ele deverá encaminhar o fluxo para a atividade "**Validar certificados**", que será executado pelo usuário que executou a atividade de "Aprovação final" anteriormente. Com os certificados validados, o responsável pela atividade deverá encaminha o fluxo para a atividade "Projeto encerrado", conforme descrito abaixo.   
    · **Projeto encerrado**: Caso o usuário encaminhe para essa atividade, o acompanhamento do projeto será "aprovado" e o projeto de extensão terá sua a situação alterada para "Encerrado", finalizando o fluxo e o projeto de extensão.  
    
    
 Para visualizar o fluxo completo, segue abaixo o diagrama de atividades para ter uma visão mais clara do processo descrito.  
    
    
                                 
  

 Informações Complementares

---

[Acompanhamento de Projeto de Extensão](http://tdn.totvs.com/display/LRM/DT_ACOMPANHAMENTO_EXTENSAO)
