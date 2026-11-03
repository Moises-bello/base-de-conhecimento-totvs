---
content_hash: 98ffacd0b02b48ba76f4e1ad340f93a1f3a136c309b93b24f1a330b022682ac6
fetched_at: '2026-06-29T00:11:05.252589+00:00'
page_id: '628377704'
product: rm
source: tdn-rm
title: Cópia de DT_CADASTRO_PROPOSTA_PESQUISA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=628377704
version: 1
---

# Cadastro de Proposta de Pesquisa

## Características do Requisito

|  |  |
| --- | --- |
| **inha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Cadastros Iniciais:** | * Tabela dinâmica "Produto final obtido (PESQEXT002)" em "TOTVS Serviços Globais | Administração | Tabela dinâmica | Item da tabela dinâmica"; * Tabela dinâmica "Tipo de arrecadação (PESQEXT011)" em "TOTVS Serviços Globais | Administração | Tabela dinâmica | Item da tabela dinâmica"; * Tabela dinâmica "Tipo de rúbrica (PESQEXT012)" em "TOTVS Serviços Globais | Administração | Tabela dinâmica | Item da tabela dinâmica"; * Pesquisador/Extensionista em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Edital em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Tipo de bolsa em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Tipo de avaliação em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Motivo de arquivamento em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Área de conhecimento em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; |
| **Requisito (ISSUE):** | [PCREQ-5453](http://jira.totvs.com.br/browse/PCREQ-5453) |
| **Tabelas Utilizadas:** | * SPROJPROJETO - Cadastro da Proposta de Projeto (pesquisa/extensão) * SPROJARRECADACAO - Arrecadação de projeto * SPROJAVALIACAOPROJETO – Avaliadores do projeto de pesquisa/extensão * SPROJITEMAVALIACAO - Itens avaliados no projeto pelos avaliadores * SPROJBOLSATERCEIRO - Cadastro de Recursos de terceiros envolvidos * SPROJDESEMBOLSO - Desembolso do projeto * SPROJDESPESA - Cadastro de Despesas do Projeto * SPROJPARCERIA - Empresas parceiras no projeto * SPROJPARTICIPANTES - Cadastro de equipe do projeto * SPROJPLANOTRABALHO - Plano de trabalho do projeto * SPROJRECEITA - Cadastro de Receitas do Projeto * SPROJRECURSOBOLSAINST - Cadastro de Recursos da instituição * SPROJSOLICITACAOTIPOBOLSA - Cadastro de Solicitação de tipo de bolsas (pagamento) * SPROJEDITAL – Cadastro de edital * SPROJMOTIVOARQUIVO – Cadastro de motivo de arquivamento * SPROJPESQUISADOR – Cadastro de pesquisador/extensionista * SPROJPESQUISADORFILIAL – Cadastro de filial do pesquisador * SPROJTIPOAVALIACAO – Cadastro de tipos de avaliação * SPROJTIPOBOLSA – Cadastro de tipo de bolsa * SPROJTIPOBOLSAEDITAL – Cadastro de tipo de bolsa por edital * SPESALMOXARIFADO - Itens de Almoxarifado * SPESPATRIMONIO - Itens de Patrimônio * SPESGRUPOPESQUISA - Grupo de Pesquisa * SPESITENSPARCERIA - Itens de Parceria * SPESPLANEJAMENTO - Itens de Planejamento * SPESPRODUTOPRETENDIDO - Produtos Pretendidos * SPESRECONSIDERACAO - Reconsideração de Projeto |
| **Versões/Release:** | 12.1.9 |

## Descrição

Possibilita ao usuário gerenciar seus processos referentes a cadastro de proposta, permitindo realizar a apresentação, análise e avaliação utilizando-se do processo de aprovação através do FLUIG.

Pré-requisitos para utilizar a funcionalidade de cadastro de Proposta de Projeto de Pesquisa:

* Ter o FLUIG devidamente instalado e configurado conforme documentação:
  + Instalação: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409653>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409655>
* Ter o TOTVS Developer Studio (TDS) devidamente instalado e configurado.
  + Instalação: <http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7C+Developer+Studio>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=73078179>
* Criar no FLUIG os papéis necessários para a execução do fluxo de cadastro de proposta de projeto de pesquisa. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis.
  + Código = **pesquisador**| Descrição = **Pesquisador/Coordenador**
  + Código = **reitoria\_pesquisa**| Descrição = **Reitoria**
  + Código = **almoxarifado**| Descrição = **Resp. pelo Almoxarifado**
  + Código =**c**entro\_custo**|**Descrição =**Resp. pelo **Centro de custo****
  + Código =****p**atrimonio**|****Descrição =****Resp. pelo **Patrimônio******
* Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.
* Criar no TDS uma conexão com servidor FLUIG chamada "**Desenvolvimento**", pois no fluxo de cadastro de proposta existe uma referência para um servidor com esse nome:  
    
  Opção disponível em “TDS | Window | Show View | Other | Fluig \ Fluig Servers” 
  + **Nome Servidor**: Desenvolvimento
  + **Host**: Neste campo deve-se informar o “nome da máquina” ou “IP” onde está instaldo o servidor do FLUIG.
  + **Porta**: Neste campo deve-se informar a porta que foi instaldo o servidor do FLUIG*(*geralmente o valor é 8080).
  + **Usuário**: Neste campo deve-se informar o usuário administrador da empresa no FLUIG.
  + **Senha**: Neste campo deve-se informar a senha do administrador da empresa no FLUIG.
  + **SSL**: Desmarcado
* Criar um serviço para comunicação com o servidor de aplicação da linha RM (RM.Host), conforme dados abaixo:  
    
  Opção disponível em “TDS | Window | Show View | Other | Fluig | Visualização de Serviços”:  
  + **Servidor**: Desenvolvimento
  + **Código**: WSDATASERVER (Atenção: Para este campo, o valor deverá ser **WSDATASERVER**, visto que todos os datasets criados para o projeto fazem referência a este nome)
  + **Descrição**: Neste campo deve-se informar uma descrição sobre o serviço criado.
  + **URL**: [http://NOME\_DO\_SERVIDOR\_HOST:PPPP/wsDataServer/MEX?wsdl](http://nome_do_servidor_hostpppp/) (Para “NOME\_DO\_SERVIDOR\_HOST” deve-se informar o nome do servidor onde o “RM.Host” está instalado e rodando. Para “PPPP” deve-se informar a porta do WebService que foi configurada no arquivo de configuração do "Host" (tag HTTPPort).
  + **Tipo**: WebService
  + **API**: CXF - Fluig
* Importar o fluxo de cadastro de proposta de extensão para a ferramenta TOTVS Developer Studio (TDS). Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em: **c:\totvs\CorporeRM\ObjetosGerenciais\Fluig**  
  + Configuração: [http://tdn.totvs.com/download/attachments/172300565/RM\_BT\_Montagem\_Ambiente\_Workflows\_Fluig.pdf](http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf?version=1&modificationDate=1432910252000&api=v2)
* Para que o acesso as informações da linha RM possam ser disponibilizado no FLUIG, deve-se configurar os dados da conta do usuário que será utilizado pelo serviço de WebService. Os dados desse usuário (usuário, senha e e-mail) devem ser alterados no dataset chamado “**rm\_edu\_fontedados\_usuariorm.js**”, pois todos os acessos as tabelas do TOTVS Educacional (via WebService) irão utilizar essa conta.

  false

  Acesse o arquivo em “**TDS | Window | Show View | Package Explorer | \_InovacaoPesquisaExtensaoBase | datasets | rm\_edu\_fontedados\_usuariorm.js***”*e realize as alterações nos dados da conta alterando a linha “**dsRetorno.addRow(['mestre', 'Usuário mestre', 'totvs', 'mestre@[rm.com.br](http://rm.com.br/)'])**”, caso os dados sejam diferentes.
* Exportar para o servidor do FLUIG os Datasets, diagrama, formulário e eventos do cadastro de proposta de projeto de extensão.  
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=189313846>

## **Procedimento para configuração**

**1º Passo**

Definir um usuário de acesso para comunicação (via WebService*)*para acesso as funcionalidades de extensão na linha RM. Esse usuário deverá ter acesso total nas funcionalidades, pois ele será utilizado para consulta e atualização dos dados nas tabelas no TOTVS Educacional pelo FLUIG (via integração).

Exemplo de usuário do TOTVS Educacional:

**Usuário**: mestre

**Senha**: totvs

**2º Passo**

Acessar o módulo de Globais e conceder acesso total nas novas funcionalidades para o usuário “definido” no passo 1 em:

**Estrutura curricular**: “**Módulo Serviços Globais | Segurança | Perfis | Sistema Educacional | Acesso a Menus | Educacional [03] Atividades acadêmicas | [03.01] Acadêmico | [03.01.21] Inovação, Pesquisa e Extensão**”.

 

**3º Passo**

 Acessar os parâmetros do sistema para configurar o módulo de extensão, disponibilizado no menu “**Módulo Educacional | Configurações | Parâmetros | 15 – Educacional | 15.08 – Pesquisa e Extensão**”.

* + - Pesquisa e Extensão 1 / 4 
      * **Motivo de arquivamento de projeto por insuficiência de nota**: Informe um motivo para que os projetos que não obtiverem uma nota suficiente para aprovação sejam arquivados automaticamente pelo sistema*.*
    - Pesquisa e Extensão 2 / 4
      * **Texto para confirmação de envio de proposta de projeto**: Informe o texto que deseja ser exibido aos coordenadores de projetos de extensão, para que eles possam ler e concordar com a veracidade dos dados fornecidos na proposta de projeto.

 

**4º Passo**

Acessar o arquivo de configuração do “RM.Host” (RM.Host.exe.config ou RM.Host.Service.exe.config) e incluir as tagsconforme imagem abaixo, caso não existam no arquivo.

* + - **DefaultDB**: O valor dessa tag deverá ter o valor do alias utilizado na linha RM para conexão (no exemplo acima, o alias se chama “CorporeRM”), assim será possível acessar o banco de dados RM pelo acesso via WebServices.
    - **HTTPPort**: O valor dessa tag deverá ter o valor da porta utilizada para acesso ao WebService dos serviços da linha RM. Por padrão, utilizamos a porta 8051, conforme mostra a imagem acima.

Caso tenha alterado as configurações do arquivo, deve-se parar o serviço e iniciar novamente para que as alterações possam estar disponíveis.

 

**5º Passo**

Acessar o fluig (pelo browser de sua escolha), com o usuário administrador da empresa para configurar um agendador de avanço automático de tarefas. Este cadastro está disponibilizado na opção “**Fluig | Painel de Controle | Aba Gerais | Agendador de Tarefas**”, conforme descrito abaixo:

Adicionar uma “nova” configuração de agendamento, caso não exista conforme o tipo “Fluxo automático” descrito abaixo:

**- Descrição**:  Neste campo deve-se informar uma descrição para o agendamento automático. Exemplo: Avanço automático de tarefas;

**- Tipo**: Fluxo Automático;

**- Executar somente após as**: 00:00

**- Frequência**: A cada 1 minuto

 Com esse agendamento criado no servidor fluig*,*todas atividades que estiverem atrasadas serão processadas e encaminhadas para a próxima atividade. Essa configuração será necessária, pois no workflow de projeto de extensão, o presidente de comissão do edital irá definir um prazo para que os avaliadores possam realizar a tarefa, e caso este prazo não seja comprido, a tarefa será retornada para o presidente de comissão definir um novo prazo de avaliação.

## Procedimento para Utilização

Depois que todos os passos acima forem configurados, o workflow do projeto de extensão deverá estar disponível no FLUIG, conforme descrição abaixo:

**Proposta de projeto de extensão** disponível em: “**Fluig | Processos | Iniciar Solicitações | Processos disponíveis | Educacional | Inovação, Pesquisa e Extensão | Extensão | Proposta de projeto de extensão**”

Para facilitar o entendimento do workflow*,*descrevemos os passos de acordo com o desenho do fluxo:

**Fluxo do WorkFlow**

O usuário deve iniciar uma nova solicitação escolhendo a opção "Educacional | Inovação, Pesquisa e Extensão | Cadastro de Proposta de Pesquisa".

false

Para a realização dessa solicitação, é necessário que:

                - O usuário esteja vinculado ao papel de **“Pesquisador/Coordenador”**, no Fluig;

                - O Pesquisador/Extensionista, no TOTVS Educacional, precisa ser um **coordenador** para submeter propostas de pesquisa;

                               Caminho: "**Educacional | Educacional | Atividades Acadêmicas | Pesquisa/Extensão | Pesquisador/Extensionista**"

As solicitações de propostas de projeto deverão atender ao edital e poderão ser autônomas ou internas, para a instituição. Essa classificação é determinada pelo Edital publicado.

Caminho: "**Educacional | Educacional | Atividades Acadêmicas | Pesquisa/Extensão | Edital | Edital Externo**"

A propostas de projetos autônomos possuem informações reduzidas e além informações básicas do projeto, deverão ser inclusas as seguintes informações:

* + Produtos pretendidos pelo projeto;

Se a proposta de projeto for autônoma, o fluxo será redirecionado para uma única análise pela **Reitoria** para uma posição final de aprovação ou reprovação do projeto, finalizando o fluxo. 

Caso não seja uma proposta de projeto autônoma, além das informações básicas do cadastro, o usuário terá as seguintes opções de cadastros extras:

* + Parcerias: Caso o campo "Parceria com instituições externas?" esteja com valor "sim", será possível cadastrar as Parcerias da proposta.
  + Cronograma de desembolso previsto: 
    - Caso o tipo de reembolso seja da instituição, será carregada a filial do edital selecionado;
    - Caso seja uma entidade parceira, deverá ser informada uma empresa parceira;
  + Detalhamento de estrutura financeira - Arrecadação (Receitas)
  + Recursos da instituição (Receitas)
  + Rubricas da instituição (Receitas)
  + Recurso de bolsa de terceiros envolvidos (Receitas)
  + Rubricas de terceiros envolvidos (Receitas)
  + Despesas: Classificadas por tipo de rubrica.
  + Participantes: Referente a equipe de execução do projeto. Nessa atividade, o responsável irá informar os pesquisadores que farão parte do projeto.
  + Plano de trabalho: Cronograma de atividades da equipe.
  + Recursos: Definição de recursos que serão utilizados na proposta do projeto.
  + Itens de planejamento: Definição de recursos de capital, custeio, bolsas e taxas.
  + Itens de almoxarifado: Definição de recursos de almoxarifado que serão utilizado pelo projeto.
  + Itens de patrimônio: Definição de recursos de patrimônio necessários para execução do projeto.
  + Itens de parcerias: Itens de parcerias com empresas externas
  + Bolsas: Os limites de bolsas serão disponibilizados para análise pelos avaliadores conforme definido no edital.
  + Produtos pretendidos: Produtos pretendidos pelo projeto.

 

 

Importante

As informações abaixo são premissas para cadastro de propostas de pesquisa:

* Configuração do tipo de certificado que será utilizado para certificação do avaliadores que irão avaliar a proposta de pesquisa:

Caminho: "**Educacional | Educacional | Configurações | Parâmetros**"

"**15.08 - Pesquisa e Extensão | Pesquisa e Extensão 3/4 | Certificados**"

* Configuração do motivo de arquivamento que será utilizado para as propostas rejeitadas por insuficiência de nota:

Caminho: "**Educacional | Educacional | Configurações | Parâmetros**"

"**15.08 - Pesquisa e Extensão | Pesquisa e Extensão 1/4 | Motivo de arquivamento**"

* Configuração do texto que será exibido, para o coordenador proponente, para informação na confirmação de dados da proposta de pesquisa:

Caminho: "**Educacional | Educacional | Configurações | Parâmetros**"

"**15.08 - Pesquisa e Extensão | Pesquisa e Extensão 2/4 | Projeto**"

* Configuração do texto que será exibido, para o coordenador proponente, para informação na confirmação de dados da proposta de pesquisa:

Caminho: "**Educacional | Educacional | Atividades acadêmicas | Inovação, Pesquisa e Extensão**"

"**Identificação | Nota mínima para aprovação**"

A nota mínima será utilizada somente para proposta internas, submetidas para a instituição.

Caso essas informações não sejam carregas ao selecionar o edital, será exibida uma mensagem, definida na tag de resource "***j****s\_msg\_zoom\_EditalInformadoNaoPossuiInformacoesParaAvaliacaoProposta***", para o usuário.

 

 

Após inclusão da informações do projeto, a proposta poderá ser submetida para avaliação desde que o vigente no edital, ainda, esteja válido:

* + - Submeter propostas: A submissão de um projeto deve atender as seguintes condições:
      1. Somente é submetido o projeto que tiver confirmação de veracidade de informação pelo usuário.
      2. Somente é submetido o projeto com data de término de submissão vigente.Após submetido, o projeto passa para o status (Em avaliação).

Após submissão da proposta para análise, seguirão as etapas:       

1. 1. Viabilidade técnico-econômica:  
      1. Validar disponibilidade:  
         Projeto NÃO viável, situação alterada para "Arquivado":  
         1. Inclusão de itens de almoxarifado que não possuíam disponibilidade.
         2. O responsável pelo centro de custo não autorizou sua utilização.
         3. Inclusão de itens de patrimônio e que não possuíam disponibilidade.Para todos os casos, antes do arquivamento, poderá ser solicitada a reconsideração das informações do projeto. Todas as considerações e reconsiderações poderão ter o campo observação preenchido.  
           
         Projeto viável: Caso o projeto seja viável (não se enquadre como projeto não viável), o fluxo é encaminhado para a atividade de avaliação da proposta e distribuição.  
           
         Validações que poderão ser realizadas:

* + - * Itens em estoque: Se houverem itens de almoxarifado na proposta de projeto seguirá o seguinte fluxo:

1. 1. 1. 1. 1. Validar disponibilidade do almoxarifado: Assim que o "Resp. pelo almoxarifado" receber essa tarefa, deverá acessar o sistema (ERP) e verificar a disponibilidade dos itens. Se algum item não estiver disponível, deverá ser informada uma observação sobre a análise realizada e dar seguimento no fluxo para reconsideração pelo Coordenador ou arquivamento do projeto. Caso contrário, a tarefa deverá seguir o fluxo de liberação pelo responsável do Centro de Custo (item c).
            2. Verificar liberação de centro de custo: Assim que o "Resp. pelo centro de custo" receber essa tarefa, ele deverá acessar o sistema (ERP) e verificar a disponibilidade do centro de custo para os itens. Se algum item não estiver disponível, deverá ser informada uma observação sobre a análise realizada e dar seguimento no fluxo para reconsideração pelo Coordenador ou arquivamento do projeto. Caso contrário, a tarefa deve seguir o fluxo para realização da reserva de estoque (item d).  
               Se o fluxo for enviado para reconsideração do Coordenador, após sua reposta, ele retornará para validação novamente pelo responsável do almoxarifado.
            3. Realizar reserva no estoque: Essa atividade retomará para o usuário que realizou a aprovação do almoxarifado, para efetuar reserva de estoque no sistema.

* + - * Equipamentos e instalações (Patrimônios): Se houverem itens de patrimônio na proposta de projeto seguirá o seguinte fluxo:

1. 1. 1. 1. 1. Aprovação de patrimônio: Assim que o "Resp. pelo patrimônio" receber essa tarefa, deverá verificar a disponibilidade do equipamento/instalação. Se algum item não estiver disponível, deverá ser informada uma observação sobre a análise realizada e dar seguimento no fluxo para reconsideração pelo Coordenador ou arquivamento do projeto. Caso contrário, a tarefa deverá seguir o fluxo para análise e avaliação do responsável pela área de conhecimento.

1. 1. Avaliar currículo de coordenadores:   
      A atividade é enviada para o responsável pela área de conhecimento definida na proposta para avaliação inicial da Proposta de Projeto solicitada.   
      A avaliação do coordenador irá gerar um histórico e que poderá ser visualizado sempre nas etapas de avaliações de projeto.   
      Será possível anexar na atividade arquivos como, por exemplo, o "Berema" (Documento interno da instituição para avaliação de coordenadores).
   2. Distribuir propostas para responsável CNPq:   
      Deverão ser selecionados os avaliadores para a realização da avaliação da proposta.   
      Devem ser selecionados de 2 a 3 avaliadores.  
      Deverá ser definido um prazo para avaliação. Caso o prazo exceda, não haja avaliação, a atividade retornará para o responsável pela área de conhecimento para alteração do prazo ou mudança de avaliador.

      false

      Para que o Fluig retorne a tarefa após o vencimento de um prazo definido, é necessário realizar o passo para o cadastro de um **Agendador de Tarefas,**encontrado no menu de Painel de Controle, do Fluig. O agendador deve ser do tipo "Expiração de tarefas".
   3. Avaliar propostas: Nessa atividade, os responsáveis realizam a avaliação do projeto e darão notas entre 0 e 10.   
      O avaliador terá até a data limite, definido pelo responsável pela área de conhecimento, para a realização da avaliação. Caso a data limite para avaliação do projeto seja expirada, a tarefa é retornada para o responsável pela distribuição da tarefa.  
      Além da avaliação do projeto, o avaliador deverá informar se recomenda o projeto ou não o projeto. Caso não recomende, deverá informar uma justificativa para a decisão.  
        
      Nota 1: Mesmo que o avaliador não recomende o projeto, as suas notas serão consideradas para cálculo de média da avaliação do projeto.  
      Nota 2: É exibido para o avaliador algumas informações relacionadas aos limites de bolsas do edital com o total dos projetos, para que o mesmo possa avaliar e decidir a aprovação , tais como:
      1. Tipo de bolsa pagamento (Pesquisa):
         1. Exibe a quantidade disponibilizada para o edital e a soma das bolsas de todos projetos para o edital em questão que já foram aprovados.
         2. Exibe o total de recurso (valores de bolsa R$) no edital para o projeto e o total de recuso de de bolsas solicitado no projeto corrente.
         3. Exibe o total de recurso (valores de bolsa R$) para o edital e a soma de recursos de bolsas de todos projetos para o edital em questão, que já foram aprovados.Com esses valores, o avaliador poderá verificar/decidir a aprovação do projeto, caso os valores estejam abaixo ou acima do valor estipulado no edital.
   4. Aprovar avaliações: Nessa atividade o responsável pela área CNPq irá verificar todas as avaliações para aprová-las ou reprová-las.   
      Caso defina como reprovado deverá ser incluída uma justificativa para a ação.  
        
      Nota: A nota será considerada para cálculo da média de avaliação do projeto somente se for aprovada.
   5. Gerar certificados: Nessa atividade será incluído um certificado para todos os avaliadores que realizaram a avaliação.
   6. Realizar cálculos e classificação: Nessa etapa o sistema calcula as médias da proposta de projeto a atualiza os campos:
      1. Média dos avaliadores: Campo calculado pela média obtida pelas notas aprovadas dos avaliadores.
      2. Nota do proponente (currículo do coordenador): Nota recebida pelo responsável pela área de conhecimento.
      3. Nota final do projeto: Soma das médias das notas dos avaliadores com a nota do responsável pela área de conhecimento, divida pelo número de avaliadores com a nota aprovada mais o coordenador.

         false

         **Média do avaliador** = Total das notas dos itens avaliados (Por nota) / Quantidade de itens avaliados (Por nota)  
           
         **Nota Final** =  ( Total das médias dos avaliadores com nota aprovada pelo coordenador da área + Nota do coordenador da área ) / Número de avaliadores com nota aprovada + Coordenador da área  
           
         Exemplo, considerando 3 avaliadores com suas devidas notas aprovadas pelo coordenador da área: ***( Média Avaliador 1 + Média Avaliador 2 + Média Avaliador 3 + Nota Coordenador ) / 4 Pessoas***

         **Importante**: As notas são lançadas, no Fluig, com limitação de valores de 0 a 10.
   7. A proposta de projeto é considerada "Aprovada", se a nota final for maior ou igual a nota mínima exigida pelo edital da proposta. Caso contrário o projeto é arquivado e a proposta que considerada como reprovada.

O motivo utilizado para o arquivamento do projeto é o mesmo parametrizado no TOTVS Educacional, como premissa de parâmetros para cadastro de uma proposta de pesquisa.

Cancelamento do processo no Fluig

Caso o processo no Fluig seja cancelado, a proposta receberá o status de "**Cancelada**", mas não será excluída da base de dados do TOTVS Educacional.
