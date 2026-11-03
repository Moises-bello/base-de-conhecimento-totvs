---
content_hash: f9cb0f4e82b9be0cdf3230373bf763124546d9cb8ea0eb4a1eae232b74dc4988
fetched_at: '2026-06-29T00:06:18.665352+00:00'
page_id: '219684879'
product: rm
source: tdn-rm
title: DT_CADASTRO_PROPOSTA_EXTENSAO
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_CADASTRO_PROPOSTA_EXTENSAO
version: 2
---

# Cadastro de Proposta de Extensão

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Cadastros Iniciais:** | * Tabela dinâmica "Produto final obtido (PESQEXT002)" em "TOTVS Serviços Globais | Administração | Tabela dinâmica | Item da tabela dinâmica"; * Tabela dinâmica "Tipo de arrecadação (PESQEXT011)" em "TOTVS Serviços Globais | Administração | Tabela dinâmica | Item da tabela dinâmica"; * Tabela dinâmica "Tipo de rúbrica (PESQEXT012)" em "TOTVS Serviços Globais | Administração | Tabela dinâmica | Item da tabela dinâmica"; * Tabela dinâmica "Público alvo (PESQEXT013)" em "TOTVS Serviços Globais | Administração | Tabela dinâmica | Item da tabela dinâmica"; * Tabela dinâmica "Linha de extensão (PESQEXT014)" em "TOTVS Serviços Globais | Administração | Tabela dinâmica | Item da tabela dinâmica"; * Tabela dinâmica "Tipo de edital (PESQEXT018)" em "TOTVS Serviços Globais | Administração | Tabela dinâmica | Item da tabela dinâmica"; * Pesquisador/Extensionista em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Edital em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Tipo de bolsa em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Tipo de avaliação em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Tipo de ação em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Função em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Motivo de arquivamento em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Área de conhecimento em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; |
| **Requisito (ISSUE):** | [PCREQ-5448](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-5448 "PCREQ-5448") |
| **Tabelas Utilizadas:** | * SPROJPROJETO - Cadastro da Proposta de Projeto (pesquisa/extensão) * SEXTPUBLICOALVO - Cadastro de Público Alvo * SPROJARRECADACAO - Arrecadação de projeto * SPROJAVALIACAOPROJETO – Avaliadores do projeto de pesquisa/extensão * SPROJITEMAVALIACAO - Itens avaliados no projeto pelos avaliadores * SPROJBOLSATERCEIRO - Cadastro de Recursos de terceiros envolvidos * SPROJDESEMBOLSO - Desembolso do projeto * SPROJDESPESA - Cadastro de Despesas do Projeto * SPROJPARCERIA - Empresas parceiras no projeto * SPROJPARTICIPANTES - Cadastro de equipe do projeto * SPROJPLANOTRABALHO - Plano de trabalho do projeto * SPROJRECEITA - Cadastro de Receitas do Projeto * SPROJRECURSOBOLSAINST - Cadastro de Recursos da instituição * SPROJSOLICITACAOTIPOBOLSA - Cadastro de Solicitação de tipo de bolsas (pagamento) * SPROJEDITAL – Cadastro de edital * SPROJMOTIVOARQUIVO – Cadastro de motivo de arquivamento * SPROJPESQUISADOR – Cadastro de pesquisador/extensionista * SPROJPESQUISADORFILIAL – Cadastro de filial do pesquisador * SPROJTIPOAVALIACAO – Cadastro de tipos de avaliação * SPROJTIPOBOLSA – Cadastro de tipo de bolsa * SPROJTIPOBOLSAEDITAL – Cadastro de tipo de bolsa por edital * SEXTCOMISSAOAVAL – Cadastro de comissão de avaliação * SEXTFUNCAO – Cadastro de função para extensão * SEXTTIPOACAO – Cadastro de tipo de ação * SEXTSUBTIPOACAO – Cadastro de subtipo de ação |
| **Versões/Release:** | 12.1.9 |

## Descrição

Foi disponibilizado novo módulo de projetos de “Inovação, Pesquisa e Extensão” no TOTVS Educacional, permitindo ao usuário submeter **projetos de extensão** via solicitação (workflow) no FLUIG.Com essa nova funcionalidade, nossos clientes irão ganhar mais agilidade e facilidade ao realizar a apresentação, análise e avaliação utilizando-se do processo de aprovação através de workflow disponibilizando na plataforma FLUIG.

Pré-requisitos para utilizar a funcionalidade de cadastro de Proposta de Projeto de Extensão:

* Ter o FLUIG devidamente instalado e configurado conforme documentação:
  + Instalação: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409653>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409655>
* Ter o TOTVS Developer Studio (TDS) devidamente instalado e configurado.
  + Instalação: <http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7C+Developer+Studio>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=73078179>
* Criar no FLUIG os papéis necessários para a execução do fluxo de cadastro de proposta de projeto de extensão. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis.
  + Código = **pesquisador**| Descrição = **Pesquisador**
  + Código = **reitoria**| Descrição = **Reitoria**
* Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.
* Criar no TDS uma conexão com servidor FLUIG chamada "**Desenvolvimento**", pois no fluxo de cadastro de proposta existe uma referência para um servidor com esse nome:  
    
  Opção disponível em “TDS | Window | Show View | Other | Fluig \ Fluig Servers” 
  + **Nome Servidor**: Desenvolvimento
  + **Host**: Neste campo deve-se informar o “nome da máquina” ou “IP” onde está instaldo o servidor do FLUIG.
  + **Porta**: Neste campo deve-se informar a porta que foi instaldo o servidor do FLUIG*(*geralmente o valor é 8080).
  + **Usuário**: Neste campo deve-se informar o usuário administrador da empresa no FLUIG.
  + **Senha**: Neste campo deve-se informar a senha do administrador da empresa no FLUIG.
  + **SSL**: Desmarcado
* Criar um serviço para comunicação com o servidor de aplicação da linha RM (RM.Host), conforme dados abaixo:  
    
  Opção disponível em “TDS | Window | Show View | Other | Fluig | Visualização de Serviços”:  
  + **Servidor**: Desenvolvimento
  + **Código**: WSDATASERVER (Atenção: Para este campo, o valor deverá ser **WSDATASERVER**, visto que todos os datasets criados para o projeto fazem referência a este nome)
  + **Descrição**: Neste campo deve-se informar uma descrição sobre o serviço criado.
  + **URL**: [http://NOME\_DO\_SERVIDOR\_HOST:PPPP/wsDataServer/MEX?wsdl](http://nome_do_servidor_hostPPPP) (Para “NOME\_DO\_SERVIDOR\_HOST” deve-se informar o nome do servidor onde o “RM.Host” está instalado e rodando. Para “PPPP” deve-se informar a porta do WebService que foi configurada no arquivo de configuração do "Host" (tag HTTPPort).
  + **Tipo**: WebService
  + **API**: CXF - Fluig
* Importar o fluxo de cadastro de proposta de extensão para a ferramenta TOTVS Developer Studio (TDS). Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em: **c:\totvs\CorporeRM\ObjetosGerenciais\Fluig**  
  + Configuração: [http://tdn.totvs.com/download/attachments/172300565/RM\_BT\_Montagem\_Ambiente\_Workflows\_Fluig.pdf](http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf?version=1&modificationDate=1432910252000&api=v2)
* Para que o acesso as informações da linha RM possam ser disponibilizado no FLUIG, deve-se configurar os dados da conta do usuário que será utilizado pelo serviço de WebService. Os dados desse usuário (usuário, senha e e-mail) devem ser alterados no dataset chamado “**rm\_edu\_fontedados\_usuariorm.js**”, conforme o usuário configurado no passo 1 descrito abaixo nos procedimentos de configuração, pois todos os acessos as tabelas do TOTVS Educacional (via WebService) irão utilizar essa conta.
  + Acesse o arquivo em “**TDS | Window | Show View | Package Explorer | \_InovacaoPesquisaExtensaoBase | datasets | rm\_edu\_fontedados\_usuariorm.js***”* e realize as alterações nos dados da conta alterando a linha “**dsRetorno.addRow(['mestre', 'Usuário mestre', 'totvs', 'mestre@[rm.com.br](http://rm.com.br)'])**”, caso os dados sejam diferentes.
* Exportar para o servidor do FLUIG os Datasets, diagrama, formulário e eventos do cadastro de proposta de projeto de extensão.  
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=189313846>

## **Procedimento para configuração**

**1º Passo)**

Definir um usuário de acesso para comunicação (via WebService*)* para acesso as funcionalidades de extensão na linha RM. Esse usuário deverá ter acesso total nas funcionalidades, pois ele será utilizado para consulta e atualização dos dados nas tabelas no TOTVS Educacional pelo FLUIG (via integração).

Exemplo de usuário do TOTVS Educacional:

**Usuário**: mestre

**Senha**: totvs

**2º Passo)**

Acessar o módulo de Globais e conceder acesso total nas novas funcionalidades para o usuário “definido” no passo 1 em:

**Estrutura curricular**: “**Módulo Serviços Globais | Segurança | Perfis | Sistema Educacional | Acesso a Menus | Educacional [03] Atividades acadêmicas | [03.01] Acadêmico | [03.01.21] Inovação, Pesquisa e Extensão**”.

 

**3º Passo)**

 Acessar os parâmetros do sistema para configurar o módulo de extensão, disponibilizado no menu “**Módulo Educacional | Configurações | Parâmetros | 15 – Educacional | 15.08 – Pesquisa e Extensão**”.

* Pesquisa e Extensão 1 / 4 
  + **Motivo de arquivamento de projeto por insuficiência de nota**: Informe um motivo para que os projetos que não obtiverem uma nota suficiente para aprovação sejam arquivados automaticamente pelo sistema*.*
* Pesquisa e Extensão 2 / 4
  + **Texto para confirmação de envio de proposta de projeto**: Informe o texto que deseja ser exibido aos coordenadores de projetos de extensão, para que eles possam ler e concordar com a veracidade dos dados fornecidos na proposta de projeto.

 

**4º Passo)**

Acessar o arquivo de configuração do “RM.Host” (RM.Host.exe.config ou RM.Host.Service.exe.config) e incluir as tagsconforme imagem abaixo, caso não existam no arquivo.

* **DefaultDB**: O valor dessa tag deverá ter o valor do alias utilizado na linha RM para conexão (no exemplo acima, o alias se chama “CorporeRM”), assim será possível acessar o banco de dados RM pelo acesso via WebServices.
* **HTTPPort**: O valor dessa tag deverá ter o valor da porta utilizada para acesso ao WebService dos serviços da linha RM. Por padrão, utilizamos a porta 8051, conforme mostra a imagem acima.

Caso tenha alterado as configurações do arquivo, deve-se parar o serviço e iniciar novamente para que as alterações possam estar disponíveis.

 

**5º Passo)**

Acessar o fluig (pelo browser de sua escolha), com o usuário administrador da empresa para configurar um agendador de avanço automático de tarefas. Este cadastro está disponibilizado na opção “**Fluig | Painel de Controle | Aba Gerais | Agendador de Tarefas**”, conforme descrito abaixo:

Adicionar uma “nova” configuração de agendamento, caso não exista conforme o tipo “Fluxo automático” descrito abaixo:

**- Descrição**:  Neste campo deve-se informar uma descrição para o agendamento automático. Exemplo: Avanço automático de tarefas;

**- Tipo**: Fluxo Automático;

**- Executar somente após as**: 00:00

**- Frequência**: A cada 1 minuto

 Com esse agendamento criado no servidor fluig*,* todas atividades que estiverem atrasadas serão processadas e encaminhadas para a próxima atividade. Essa configuração será necessária, pois no workflow de projeto de extensão, o presidente de comissão do edital irá definir um prazo para que os avaliadores possam realizar a tarefa, e caso este prazo não seja comprido, a tarefa será retornada para o presidente de comissão definir um novo prazo de avaliação.

## Procedimento para Utilização

Depois que todos os passos acima forem configurados, o workflow do projeto de extensão deverá estar disponível no FLUIG, conforme descrição abaixo:

**Proposta de projeto de extensão** disponível em: “Fluig | Processos | Iniciar Solicitações | Processos disponíveis | Educacional | Inovação, Pesquisa e Extensão | Extensão | Proposta de projeto de extensão”

Para facilitar o entendimento do workflow*,* descrevemos os passos de acordo com o desenho do fluxo:

Assim que o usuário com papel de “Pesquisador” (que esteja cadastrado no TOTVS Educacional como pesquisador/extensionista ativo e coordenador) acessar o processo “Proposta de projeto de extensão”, ele poderá cadastrar sua proposta de projeto de extensão informando os dados do formulário. Quando o usuário informar todos campos obrigatórios do formulário e aceitar os termos para submissão de proposta de extensão, o fluxo poderá seguir dois caminhos a saber:

Caso seja uma proposta de edital externo (sem avaliação, ou seja, proposta de projeto autônomo), a solicitação será encaminhado para a atividade “**Avaliar projeto autônomo**”, pois projetos autônomos são avaliados por usuários que possuem o papel de “Reitoria”, que irá definir se será aprovado ou arquivado, mas em ambos os casos será cadastrado na base de dados da linha RM.

Caso seja uma proposta de edital de avaliação (edital não externo), a solicitação será encaminhada para a atividade “**Distribuir avaliação**” de responsabilidade do presidente de comissão do edital informado na proposta do projeto. Ou seja, quando o usuário da secretaria do TOTVS Educacional realizar o cadastro do edital de projetos de extensão (TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão | Edital), ele deverá definir quem será o presidente de comissão de avaliação do edital (TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão | Edital | Anexo Comissão de avaliação). Assim, todos projetos submetidos para um edital não externo, serão encaminhados diretamente para o pesquisador/extensionista cadastrado na comissão do edital como “presidente”.

Assim que a solicitação estiver com o presidente de comissão do edital, ele poderá convidar novos pesquisadores a fazerem parte da equipe de avaliação do edital, bastando selecionar um pesquisador como possível avaliador e encaminhando a solicitação para a atividade “**Convite de comissão**”. Esse convite será direcionado para o avaliador, que deverá acessar sua central de tarefas no FLUIG*,* para aceitar ou não sua participação na comissão de avaliação do edital. Depois que o possível “convidado” responder, a solicitação será direcionada novamente para o presidente de comissão do edital, permitindo que o presidente possa realizar vários convites até selecionar os avaliadores da proposta.

De posse da solicitação novamente, o presidente de comissão deverá selecionar os avaliadores da proposta de extensão. Ele deverá selecionar um e no máximo três avaliadores, informando a data limite e hora para realizar a avaliação da proposta e enviar a solicitação para a atividade “**Avaliar**”. Caso o avaliador selecionado perca o prazo estipulado, a solicitação será redirecionada para a atividade “**Replanejamento X**”, onde “**X**” será o número do avaliador selecionado, e que o presidente de comissão deverá definir um novo prazo para avaliação e/ou informar um outro avaliador na lista de avaliadores do edital. Assim que todos avaliadores realizarem a avaliação da proposta, a atividade será encaminhada para a atividade “**Avaliar proponente**”. Essa atividade será direcionada para o presidente de comissão, que deverá conceder uma nota para o coordenador do projeto (o pesquisador que submeteu a proposta de projeto de extensão). Depois que o presidente de comissão enviar a solicitação para a atividade “**Processar notas**”, o sistema irá calcular a nota do projeto (obtida pela média de notas dos avaliadores e multiplicada pelo peso definido no edital) e verificar se está abaixo do mínimo exigido no edital para aprovação. Caso a nota seja abaixo do mínimo exigido no edital, o projeto será arquivoado automaticamente e o fluxo será encerrado com o projeto arquivado por insuficiência de nota.

Caso o projeto obtenha uma nota superior ao mínimo exigido no edital, a solicitação será encaminhada para a atividade “**Avaliação Final**”, que será de responsabilidade do papel de “Reitoria”, que deverá realizar a aprovação/reprovação final do projeto. Ou seja, mesmo que o projeto obtenha nota superior ao exigido no edital, o usuário que possuir papel de “Reitoria” poderá reprovar estes projetos. Caso o projeto seja aprovado pelo pela reitoria, ele será classificado com a situação “Em Execução”, permitindo ao coordenador do projeto solicitar outras atividades, tais como: “Cadastrar bolsistas” e “[Acompanhar projeto de extensão](http://tdn.totvs.com/display/LRM/DT_ACOMPANHAMENTO_EXTENSAO)”.

divs
