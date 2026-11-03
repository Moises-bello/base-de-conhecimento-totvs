---
content_hash: ddf145c8ce89d61f12bc9203987a654c29a66233f8ce28dfcf1705edbbb56777
fetched_at: '2026-06-29T00:11:04.424150+00:00'
page_id: '626919533'
product: rm
source: tdn-rm
title: Rascunho_Documento de Apoio - Cadastro Proposta Pesquisa
type: documentation
url: https://tdn.totvs.com/display/LRM/Rascunho_Documento+de+Apoio+-+Cadastro+Proposta+Pesquisa
version: 1
---

O ***Cadastro de Proposta de Pesquisa***, tem como objetivo possibilitar ao usuário gerenciar seus processos referente ao cadastro de Proposta de Pesquisa, permitindo realizar a apresentação, análise e avaliação, utilizando  do processo de aprovação através do Wokflow FLUIG.  
 Para o Módulo Cadastro proposta Pesquisa, será necessário efetuar alguns cadastros no qual os mesmos são utilizados durante o processo, sendo:

O pesquisador/Extensionista necessita ser um Coordenador para submeter proposta de Pesquisa:   
    
 v  Cadastro: Totvs Gestão Educacional | Atividades Acadêmicas | Pesquisa/Extensão | Pesquisador/Extensionista  
As solicitações de propostas de projeto deverão atender ao edital e poderão ser autônomas ou internas, para a instituição. Essa classificação é determinada pelo Edital publicado.  
 v  Cadastro: Totvs Educacional | Educacional | Atividades Acadêmicas | Pesquisa/Extensão | Edital | Edital Externo  
Configuração do tipo de certificado que será utilizado para certificação dos avaliadores que irão avaliar a proposta de pesquisa:  
 v Cadastro: Totvs Educacional | Educacional | Configurações | Parâmetros - 15.08 - Pesquisa e Extensão | Pesquisa e Extensão 3/4 | Certificados  
Configuração do motivo de arquivamento que será utilizado para as propostas rejeitadas por insuficiência de nota:  
 v  Cadastro: Totvs Educacional | Educacional | Configurações | Parâmetros | Integração | Pesquisa e Extensão | Pesquisa e Extensão 1/4 | Motivo de arquivamento  
Configuração do texto que será exibido, para o coordenador proponente, para informação na confirmação de dados da proposta de pesquisa:  
 v  Cadastro: Totvs Educacional | Educacional | Configurações | Parâmetros | Integração |Pesquisa e Extensão | Pesquisa e Extensão 2/4 | Projeto"  
Informar a Nota Mínima para propostas internas submetidas para Avaliação:  
 v  Cadastro: Totvs Educacional | Educacional | Atividades Acadêmicas | Inovação, Pesquisa e Extensão | Edital | Nota Mínima para Avaliação   
Criar no FLUIG os papéis necessários para a execução do fluxo do projeto de inovação. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis.  
Código = pesquisador | Descrição = Pesquisador / Coordenador  
Código = reitoria\_pesquisa | Descrição = Reitoria  
Código = almoxarifado | Descrição = Resp. pelo Almoxarifado  
Código = centro\_custo| Descrição = Resp. pelo Centro de Custo   
Código = patrimonio | Descrição = Resp. pelo Patrimônio  
    
 Em seguida, associar os usuários aos respectivos papéis cadastrados.  
    
Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.  
    
Importar o fluxo: Cadastro Proposta de Pesquisa  para a ferramenta TOTVS Developer Studio (TDS).   
 Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em c:\totvs\CorporeRM\ObjetosGerenciais\Fluig.  
 **Descrição do Processo:**  
 Logar com o usuário associado ao papel de: "Pesquisador/Coordenador" e iniciar uma nova solicitação no FLUIG, escolhendo a opção:

* "FLUIG | Iniciar Solicitações | Educacional | Inovação, Pesquisa e Extensão | Pesquisa | Cadastro Proposta Pesquisa | Cadastro Proposta Pesquisa"

Após inclusão das informações do projeto, a proposta poderá ser submetida para avaliação desde que o vigente no edital, ainda, esteja válido:  
Submeter propostas: A submissão de um projeto deve atender as seguintes condições;  
Somente é submetido o projeto que tiver confirmação de veracidade de informação pelo usuário;  
 Somente é submetido o projeto com data de término de submissão vigente.   
 Após submetido, o projeto passa para o status (Em avaliação).  
 Após submissão da proposta para análise, seguirão as etapas:         
 \*\*\* Propostas de projetos para editais externos (projetos autônomos) não sofrerão as validações dos itens abaixo, pois não possuem vínculos com bolsas e não utilizarão recursos da instituição.  
    
 A)   Viabilidade técnico-econômica:  
    
 - Validar disponibilidade:  
 Projeto NÃO viável, situação alterada para "Arquivado":  
 Inclusão de itens de almoxarifado que não possuíam disponibilidade.  
 O responsável pelo centro de custo não autorizou sua utilização.  
 Inclusão de itens de patrimônio e que não possuíam disponibilidade.  
  
 Para todos os casos, antes do arquivamento, poderá ser solicitada a reconsideração das informações do projeto. Todas as considerações e reconsiderações poderão ter o campo observação preenchido.  
Projeto viável: Caso o projeto seja viável (não se enquadre como projeto não viável), o fluxo é encaminhado para a atividade de avaliação da proposta e distribuição.  
 Validações que poderão ser realizadas:  
 a)    Itens em estoque: Se houverem itens de almoxarifado na proposta de projeto seguirá o seguinte fluxo:  
 1)    Validar disponibilidade do almoxarifado: Assim que o "Resp. pelo almoxarifado" receber essa tarefa, deverá acessar o sistema (ERP) e verificar a disponibilidade dos itens. Se algum item não estiver disponível, deverá ser informada uma observação sobre a análise realizada e dar seguimento no fluxo para reconsideração pelo Coordenador ou arquivamento do projeto. Caso contrário, a tarefa deverá seguir o fluxo de liberação pelo responsável do Centro de Custo (item c).  
 2)    Verificar liberação de centro de custo: Assim que o "Resp. pelo centro de custo" receber essa tarefa, ele deverá acessar o sistema (ERP) e verificar a disponibilidade do centro de custo para os itens. Se algum item não estiver disponível, deverá ser informada uma observação sobre a análise realizada e dar seguimento no fluxo para reconsideração pelo Coordenador ou arquivamento do projeto. Caso contrário, a tarefa deve seguir o fluxo para realização da reserva de estoque (item d). Se o fluxo for enviado para reconsideração do Coordenador, após sua reposta, ele retornará para validação novamente pelo responsável do almoxarifado.  
 3)     Realizar reserva no estoque: Essa atividade retomará para o usuário que realizou a aprovação do almoxarifado, para efetuar reserva de estoque no sistema.  
 b)    Equipamentos e instalações (Patrimônios): Se houverem itens de patrimônio na proposta de projeto seguirá o seguinte fluxo:  
 1)    Aprovação de patrimônio: Assim que o "Resp. pelo patrimônio" receber essa tarefa, deverá verificar a disponibilidade do equipamento/instalação.   
 - Se algum item não estiver disponível, deverá ser informada uma observação sobre a análise realizada e dar seguimento no fluxo para reconsideração pelo Coordenador ou arquivamento do projeto. Caso contrário, a tarefa deverá seguir o fluxo para análise e avaliação do responsável pela área de conhecimento.  
    
 B) Avaliar currículo de coordenadores:   
 - A atividade é enviada para o responsável pela área de conhecimento definida na proposta para avaliação inicial da Proposta de Projeto solicitada.   
 - A avaliação do coordenador irá gerar um histórico e que poderá ser visualizado sempre nas etapas de avaliações de projeto.   
 - Será possível anexar na atividade arquivos como, por exemplo, o "Berema" (Documento interno da instituição para avaliação de coordenadores).  
 C) Distribuir propostas para responsável CNPq:   
 - Deverão ser selecionados os avaliadores para a realização da avaliação da proposta.   
 - Devem ser selecionados de 2 a 3 avaliadores.  
 - Deverá ser definido um prazo para avaliação. Caso o prazo exceda, não haja avaliação, a atividade retornará para o responsável pela área de conhecimento para alteração do prazo ou mudança de avaliador.  
    
 D) Avaliar propostas: Nessa atividade, os responsáveis realizam a avaliação do projeto e darão notas entre 0 e 10.   
 - O avaliador terá até a data limite, definido pelo responsável pela área de conhecimento, para a realização da avaliação. Caso a data limite para avaliação do projeto seja expirada, a tarefa é retornada para o responsável pela distribuição da tarefa.  
 - Além da avaliação do projeto, o avaliador deverá informar se recomenda o projeto ou não o projeto. Caso não recomende, deverá informar uma justificativa para a decisão.  
    
 Nota 1: Mesmo que o avaliador não recomende o projeto, as suas notas serão consideradas para cálculo de média da avaliação do projeto.  
 Nota 2: É exibido para o avaliador algumas informações relacionadas aos limites de bolsas do edital com o total dos projetos, para que o mesmo possa avaliar e decidir a aprovação, como:  
 ·     Tipo de bolsa pagamento (Pesquisa):  
 o    Exibe a quantidade disponibilizada para o edital e a soma das bolsas de todos projetos para o edital em questão que já foram aprovados.  
 o    Exibe o total de recurso (valores de bolsa R$) no edital para o projeto e o total de recuso de de bolsas solicitado no projeto corrente.  
 o    Exibe o total de recurso (valores de bolsa R$) para o edital e a soma de recursos de bolsas de todos projetos para o edital em questão, que já foram aprovados.  
 Com esses valores, o avaliador poderá verificar/decidir a aprovação do projeto, caso os valores estejam abaixo ou acima do valor estipulado no edital.  
 E)    Aprovar avaliações: Nessa atividade o responsável pela área CNPq irá verificar todas as avaliações para aprová-las ou reprová-las.  Caso defina como reprovado deverá ser incluída uma justificativa para a ação.  
 Nota: A nota será considerada para cálculo da média de avaliação do projeto somente se for aprovada.  
 F)  Gerar certificados: Nessa atividade será incluído um certificado para todos os avaliadores que realizaram a avaliação.  
 G) Realizar cálculos e classificação: Nessa etapa o sistema calcula as médias da proposta de projeto a atualiza os campos:  
                               i.        Média dos avaliadores: Campo calculado pela média obtida pelas notas aprovadas dos avaliadores.  
                              ii.        Nota do proponente (currículo do coordenador): Nota recebida pelo responsável pela área de conhecimento.  
                             iii.        Nota final do projeto: Soma das médias das notas dos avaliadores com a nota do responsável pela área de conhecimento, dividida pelo número de avaliadores com a nota aprovada mais o coordenador.  
 *Cálculo para realizar a Média:*  
  *\** *Média do avaliador* = Total das notas dos itens avaliados (Por nota) / Quantidade de itens avaliados (Por nota)  
 Exemplo: O Coordenador, cadastrou 3 itens a serem avaliados.  
 ·          O 1º Avaliador , concedeu as seguintes notas:  
 Item 1 = 9  
 Item 2 = 7  
 Item 3 = 5  
 Total: 21 / 3 = 7  
 Nota do 1º Avaliador = 7  
 ·          O 2º Avaliador, concedeu as seguintes notas:  
 Item 1 = 5  
 Item 2 = 4  
 Item 3 = 9  
 Total: 18 / 3 = 6  
 Nota do 2º Avaliador = 6  
 ·          Nota do responsável pela Área: 8  
 *\** *Nota Final* =  ( Total das médias dos avaliadores com nota aprovada pelo coordenador da área + Nota do coordenador da área ) / Número de avaliadores com nota aprovada   
 Exemplificando:  
 Considerando 3 avaliadores com suas devidas notas aprovadas pelo coordenador da área:   
           (Méd. 1º Avaliador  + Méd. 2º Avaliador + Nota Coordenador) / 3 Pessoas  
                     7                             6                       8                 /  3     =   7  
 Neste exemplo, a nota final do projeto foi: 7  
 **Importante**: As notas são lançadas no Fluig, com limitação de valores de 0 a 10. Devido a isso, a Nota máxima cadastrada no Edital tem que seguir a mesma estrutura.  
 H)  A proposta de projeto é considerada "Aprovada", se a nota final for maior ou igual a nota mínima exigida pelo edital da proposta. Caso contrário o projeto é arquivado e a proposta que considerada como reprovada.  
 O motivo utilizado para o arquivamento do projeto é o mesmo parametrizado no TOTVS Educacional, como premissa de parâmetros para cadastro de uma proposta de pesquisa.  
 O Cancelamento do processo no Fluig: Caso o processo no Fluig seja cancelado, a proposta receberá o status de "Cancelada", mas não será excluída da base de dados do TOTVS Educacional.  
    
 Para visualizar o fluxo completo, segue abaixo o diagrama de atividades para ter uma visão mais clara do processo descrito.  
     

Informações Complementares

---

[Documento Técnico - Cadastro Proposta Pesquisa](http://tdn.totvs.com/display/LRM/DT_CADASTRO_PROPOSTA_PESQUISA)
