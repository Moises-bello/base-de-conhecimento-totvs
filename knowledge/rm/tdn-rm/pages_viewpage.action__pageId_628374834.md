---
content_hash: b700045299ac4fb50fc1cb059dc6a26b11efb963e61113b843dd25318d1f099d
fetched_at: '2026-06-29T00:11:05.137877+00:00'
page_id: '628374834'
product: rm
source: tdn-rm
title: Cópia de DT_ACOMPANHAMENTO_EXTENSAO_WF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=628374834
version: 46
---

# ACOMPANHAMENTO DE PROJETO DE EXTENSÃO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | **********Inovação,********** Pesquisa e Extensão |
| **Cadastros Iniciais:** | * Tabela dinâmica "Produto final obtido (PESQEXT002)" em "TOTVS Serviços Globais | Administração | Tabela dinâmica | Item da tabela dinâmica"; * Tabela dinâmica "Tipo de arrecadação (PESQEXT011)" em "TOTVS Serviços Globais | Administração | Tabela dinâmica | Item da tabela dinâmica"; * Tabela dinâmica "Tipo de rúbrica (PESQEXT012)" em "TOTVS Serviços Globais | Administração | Tabela dinâmica | Item da tabela dinâmica"; * Tabela dinâmica "Público alvo (PESQEXT013)" em "TOTVS Serviços Globais | Administração | Tabela dinâmica | Item da tabela dinâmica"; * Tabela dinâmica "Linha de extensão (PESQEXT014)" em "TOTVS Serviços Globais | Administração | Tabela dinâmica | Item da tabela dinâmica"; * Tabela dinâmica "Tipo de edital (PESQEXT018)" em "TOTVS Serviços Globais | Administração | Tabela dinâmica | Item da tabela dinâmica"; * Pesquisador/Extensionista em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Edital em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Tipo de bolsa em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Tipo de avaliação em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Tipo de ação em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Função em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Motivo de arquivamento em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Área de conhecimento em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; |
| **Requisito (ISSUE):** | [PCREQ-5448](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-5448 "PCREQ-5448") |
| **Tabelas Utilizadas:** | * SPROJPROJETO - Cadastro da Proposta de Projeto (pesquisa/extensão) * SPROJPARTICIPANTES - Cadastro de equipe do projeto * SPROJPLANOTRABALHO - Plano de trabalho do projeto * SPROJMOTIVOARQUIVO – Cadastro de motivo de arquivamento * SPROJPESQUISADOR – Cadastro de pesquisador/extensionista * SEXTCOMISSAOAVAL – Cadastro de comissão de avaliação * SEXTFUNCAO – Cadastro de função para extensão * SEXTTIPOACAO – Cadastro de tipo de ação * SPROJACOMPANHAMENTO - Acompanhamento de Projeto (pesquisa/extensão) * SPROJACOMPPARTICIPANTES - Participantes do Acompanhamento de Projeto (pesquisa/extensão) * SPROJACOMPARRECADACAO - Arrecadação do Acompanhamento de Projeto (pesquisa/extensão) * SPROJACOMPBOLSATERCEIRO - Bolsa de terceiro do Acompanhamento (pesquisa/extensão) * SPROJACOMPPLANOTRABALHO - Acompanhamento do Plano de trabalho (pesquisa/extensão) * SPROJACOMPDESEMBOLSO - Acompanhamento Desembolso (pesquisa/extensão) * SPROJACOMPDESPESA - Acompanhamento Despesa (pesquisa/extensão) * SPROJACOMPRECEITA - Acompanhamento Receita (pesquisa/extensão) * SPROJACOMPRECURSOBOLSAINST - Acompanhamento recurso bolsa institucional (pesquisa/extensão) * SPROJACOMPPRODUTOOBTIDO - Acompanhamento produto obtido (pesquisa/extensão) * SEXTACOMPPUBLICOALVO - Acompanhamento do publico alvo (extensão) |
| **Versões/Release:** | 12.1.15 |

## Descrição

Foi disponibilizado novo módulo de projetos de “Inovação, Pesquisa e Extensão” no TOTVS Educacional, permitindo ao usuário submeter **acompanhamento de ação de extensão** via solicitação (workflow) no FLUIG.Com essa nova funcionalidade, nossos clientes irão ganhar mais agilidade e facilidade ao realizar a apresentação, análise e avaliação utilizando-se do processo de aprovação através de workflow disponibilizando na plataforma FLUIG.

Pré-requisitos para utilizar a funcionalidade de Acompanhamento de Projeto de Extensão:

* Ter o FLUIG devidamente instalado e configurado conforme documentação:
  + Instalação: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409653>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409655>
* Ter o TOTVS Developer Studio (TDS) devidamente instalado e configurado.
  + Instalação: <http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7C+Developer+Studio>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=73078179>
* Criar no FLUIG os papéis necessários para a execução do fluxo de cadastro de proposta de projeto de extensão. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis.
  + Código = **pesquisador**| Descrição = **Pesquisador**
  + Código = **reitoria\_extensao**| Descrição = **Reitoria de Extensão**
  + Código = **secretaria** | Descrição = **Secretaria**
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
* Para que o acesso as informações da linha RM possam ser disponibilizado no FLUIG, deve-se configurar os dados da conta do usuário que será utilizado pelo serviço de WebService. Os dados desse usuário (usuário, senha e e-mail) devem ser alterados no dataset chamado “**rm\_edu\_fontedados\_usuariorm.js**”, conforme o usuário configurado no passo 1 descrito abaixo nos procedimentos de configuração, pois todos os acessos as tabelas do TOTVS Educacional (via WebService) irão utilizar essa conta.
  + Acesse o arquivo em “**TDS | Window | Show View | Package Explorer | \_InovacaoPesquisaExtensaoBase | datasets | rm\_edu\_fontedados\_usuariorm.js***”*e realize as alterações nos dados da conta alterando a linha “**dsRetorno.addRow(['mestre', 'Usuário mestre', 'totvs', 'mestre@[rm.com.br](http://rm.com.br/)'])**”, caso os dados sejam diferentes.
* Exportar para o servidor do FLUIG os Datasets, diagrama, formulário e eventos do cadastro de proposta de projeto de extensão.  
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=189313846>

## **Procedimento para configuração**

**1º Passo)**

Definir um usuário de acesso para comunicação (via WebService*)*para acesso as funcionalidades de extensão na linha RM. Esse usuário deverá ter acesso total nas funcionalidades, pois ele será utilizado para consulta e atualização dos dados nas tabelas no TOTVS Educacional pelo FLUIG (via integração).

Exemplo de usuário do TOTVS Educacional:

**Usuário**: mestre

**Senha**: totvs

**2º Passo)**

Acessar o módulo de Globais e conceder acesso total nas novas funcionalidades para o usuário “definido” no passo 1 em:

“**Módulo Serviços Globais | Segurança | Perfis | Sistema Educacional | Acesso a Menus | Educacional [03] Atividades acadêmicas | [03.01] Acadêmico | [03.01.21] Inovação, Pesquisa e Extensão**”.

****3º Passo)****

Para configurar as notificações referentes ao envio de relatório parcial/final de acompanhamento do projeto de extensão, deve-se realizar a configuração da “Central de Notificações”, que foi uma nova funcionalidade disponibilizada na versão 12.1.8, conforme documentação “<http://tdn.totvs.com/display/LRM/DT_Central_Notificacao>” na parte "Configuração de ambiente (Fluig e Parâmetros Globais e Contas de Comunicação)". Além das configurações realizadas nos passos acima, deve-se realizar o cadastro das mensagens conforme descrito abaixo:

 Acessar o cadastro de mensagens de notificação, disponibilizado em “**TOTVS Educacional | Atividades Acadêmicas | Central de Notificações | Mensagens de notificação**”:

 1)       Mensagem de relatório **parcial** de acompanhamento

 Informar os dados da mensagem para relatório parcial:

* Aba “E-mail”:

                    **-** **Esta mensagem será enviada com o objetivo de**: Enviar notificação ao coordenador do projeto sobre envio de relatório **parcial** de acompanhamento 

**- Tags Disponíveis**: Clicando nessa opção, pode-se inserir algumas tagspré-definidas para serem inseridas no texto da mensagem e que serão substituídas pelos registros correspondentes. 

**- Assunto da mensagem**: Deve-se informar o assunto da mensagem de e-mail; 

**- Ativar envio por e-mail**: Deve-se marcar esse campo, caso deseje enviar e-mail ao coordenador do projeto para envio de relatório parcial; 

**- Texto**: Deve-se criar o texto que será enviado por e-mail para o coordenador do projeto para envio do relatório parcial;  

* Aba “Notificações Fluig”:

**- Ativar notificação via Fluig**: Deve-se marcar esse campo, caso deseje enviar uma notificação ao coordenador do projeto para envio do relatório parcial dentro do fluig; 

**- Texto**: Deve-se criar o texto que será enviado por notificação no fluigpara o coordenador do projeto para envio do relatório parcial; 

 2)       Mensagem de relatório **final** de acompanhamento 

Informar os dados da mensagem para relatório final: 

* Aba “E-mail”:

**-** **Esta mensagem será enviada com o objetivo de**: Enviar notificação ao coordenador do projeto sobre envio de relatório **final** de acompanhamento 

**- Tags Disponíveis**: Clicando nessa opção, pode-se inserir algumas tagspré-definidas para serem inseridas no texto da mensagem e que serão substituídas pelos registros correspondentes. 

**- Assunto da mensagem**: Deve-se informar o assunto da mensagem de e-mail; 

**- Ativar envio por e-mail**: Deve-se marcar esse campo, caso deseje enviar e-mail ao coordenador do projeto para envio de relatório final; 

**- Texto**: Deve-se criar o texto que será enviado por e-mail para o coordenador do projeto para envio do relatório final; 

* Aba “Notificações Fluig”:

**- Ativar notificação via Fluig**: Deve-se marcar esse campo, caso deseje enviar uma notificação ao coordenador do projeto para envio do relatório final dentro do fluig; 

**- Texto**: Deve-se criar o texto que será enviado por notificação no fluigpara o coordenador do projeto para envio do relatório final;

 

**4º Passo)**

Acessar os parâmetros do sistema para configurar a central de notificações para relatórios (parcial/final) do projeto, disponibilizado no menu “**Módulo Educacional | Configurações | Parâmetros | 15 – Educacional |** **15.05 – Integração | 15.05.10 - Fluig**”.

* Acad. Social – Geral

* + **Código da conta de comunicação**: Informe a conta de comunicação utilizada para integração com o fluig. Para mais informações de cadastro dessa conta, acesse a documentação disponível em <http://tdn.totvs.com/display/public/LRM/DT_Academia_Social> na seção “Configuração de ambiente”;

 

* Notificações

* + **Gerar estrutura de notificação do Educacional no Fluig?** Verifique se os eventos de notificação foram gerados no fluig, ou seja, se a coluna “Gerado?” está com o valor “sim” não será necessário essa configuração, pois já foi realizada. Caso esteja com o valor “não”, deve-se marcar o parâmetro “Gerar estrutura de notificação do Educacional no Fluig” e avançar o parametrizador para que o sistema configure o fluig com os novos eventos de notificação.

Acessar os parâmetros do sistema para configurar o módulo de extensão, disponibilizado no menu “**Módulo Educacional | Configurações | Parâmetros | 15 – Educacional | 15.08 – Pesquisa e Extensão**”.

* Pesquisa e Extensão 2 / 5  
    
  + **Aviso de envio de relatório PARCIAL do projeto - Dias para aviso (Exemplo: 10, 15, 20, 25)**: Informe os dias que deseja avisar (por e-mail ou notificação do fluig) aos coordenadores dos projetos de extensão para enviar o **relatório parcial** de acompanhamento dos projetos.
  + **Aviso de envio de relatório PARCIAL do projeto - Mês para aviso (Exemplo: 1, 2)**: Informe os meses que deseja avisar (por e-mail ou notificação do fluig) aos coordenadores dos projetos de extensão para enviar o **relatório parcial** de acompanhamento dos projetos.
  + **Aviso de envio de relatório FINAL do projeto - Dias para aviso (Exemplo: 10, 15, 20, 25)**: Informe os dias que deseja avisar (por e-mail ou notificação do fluig) aos coordenadores dos projetos de extensão para enviar o **relatório final** de acompanhamento dos projetos.
  + **Aviso de envio de relatório FINAL do projeto - Mês para aviso (Exemplo: 1, 2)**: Informe os meses que deseja avisar (por e-mail ou notificação do fluig) aos coordenadores dos projetos de extensão para enviar o **relatório final** de acompanhamento dos projetos.

**5º Passo)**

Acessar o arquivo de configuração do “RM.Host” (RM.Host.exe.config ou RM.Host.Service.exe.config) e incluir as tags conforme imagem abaixo, caso não existam no arquivo.

* **JobServer3Camadas**: O valor dessa tag deverá ser “true” para possibilitar o agendamento de Jobs pela funcionalidade do módulo de Globais.
* **DefaultDB**: O valor dessa tag deverá ter o valor do alias utilizado na linha RM para conexão (no exemplo acima, o alias se chama “CorporeRM”), assim será possível acessar o banco de dados RM pelo acesso via WebServices.
* **HTTPPort**: O valor dessa tag deverá ter o valor da porta utilizada para acesso ao WebService dos serviços da linha RM. Por padrão, utilizamos a porta 8051, conforme mostra a imagem acima.

 Outra configuração necessária para agendamento de Jobs, será no “**Gerenciamento de Alias**” (no momento do login no RM) para habilitar o processamento de Jobs. Neste cadastro, acessar a aba “**Serviços**” e marcar o parâmetro “**Habilitar Processamento de Job**”.

Caso tenha alterado as configurações do arquivo, deve-se parar o serviço e iniciar novamente para que as alterações possam estar disponíveis. Essas configurações serão necessárias para enviar “notificação” aos coordenadores do projeto sobre o envio de relatórios (parcial/final) no acompanhamento do projeto de extensão e pesquisa.

## Procedimento para Utilização

Depois que todos os passos acima forem configurados, o workflowde acompanhamento do projeto de extensão estará disponível no fluig, conforme descrito abaixo:

Acompanhamento de projeto de extensão disponível em: “**Fluig | Processos | Iniciar Solicitações | Processos disponíveis | Educacional | Inovação, Pesquisa e Extensão | Extensão | Acompanhamento do projeto de extensão**”

Assim que o usuário pesquisador (coordenador do projeto) estiver algum projeto de extensão com situação “Em execução” (submeteu o projeto de extensão e foi aprovado), ele poderá acessar o fluige cadastrar seu acompanhamento do projeto de extensão informando os dados do formulário. Quando o usuário informar todos campos obrigatórios do formulário e aceitar os termos para submissão de acompanhamento da proposta de extensão, o fluxo poderá seguir dois caminhos a saber:

Caso seja uma “solicitação extraordinária” (solicitação de mudança no projeto original para dados de "bolsa",  “equipe” e/ou “plano de trabalho”), a solicitação será encaminhada para a atividade “**Avaliar solicitação extraordinária**”, pois todas solicitações de mudança no projeto original serão avaliadas pelo papel de “Reitoria de Extensão”, que irá definir se a mudança será aprovada ou reprovada, mas caso seja aprovado, os dados (bolsa, equipe e/ou plano de trabalho) serão alterados no projeto original.

Caso seja um “acompanhamento” (relatório parcial/final), a solicitação será encaminhada para a atividade “**Avaliar acompanhamento**”, que será de responsabilidade do presidente de comissão do edital informado na proposta do projeto. Ou seja, quando o usuário da secretaria do TOTVS Educacional realizar o cadastro do edital de projetos de extensão (TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão | Edital), ele deverá definir quem será o presidente de comissão de avaliação do edital (TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão | Edital | Anexo Comissão de avaliação). Assim, todos acompanhamentos de projetos para um edital não externo, serão encaminhados diretamente para o pesquisador/extensionista cadastrado na comissão do edital como “presidente”. Este usuário deverá realizar a avaliação do acompanhamento (tanto para relatório parcial quanto para final), e poderá solicitar uma retificação das informações, encaminhando a atividade “**Retificar**”, onde o coordenador do projeto deverá realizar as alterações e encaminhar novamente para o presidente da comissão, que poderá aprovar a solicitação encaminhando a solicitação para a atividade “**Aprovado**”. Caso seja um relatório **parcial**, a solicitação será finalizada e o coordenador do projeto poderá enviar novo acompanhamento de projeto de extensão. Em contrapartida, caso seja um relatório **final**, a solicitação será encaminhada para a atividade “**Aprovação final**”, que será de responsabilidade do papel de “Reitoria de Extensão”, que poderá definir três saídas para o andamento da solicitação, são elas:

* **Retificar**: Caso o usuário com papel de reitoria de extensão encaminhe para essa atividade, o fluxo será encaminhado para o solicitante (usuário que solicitou o acompanhamento do projeto) para que ele possa realizar as devidas alterações no acompanhamento, e posteriormente retornar para o usuário que solicitou a retificação do acompanhamento.

* **Emitir certificado**: Caso o usuário com papel de reitoria de extensão encaminhe para essa atividade, o usuário com papel de “Secretaria” deverá assumir a tarefa e acessar o TOTVS Educacional para a geração dos certificados inseridos no sistema em “TOTVS Educacional | Atividades acadêmicas | Certificados”. Depois que todos certificados forem emitidos, ele deverá encaminhar o fluxo para a atividade “**Validar certificados**”, que será executado pelo usuário que executou a atividade de “Aprovação final” anteriormente. Com os certificados validados, o responsável pela atividade deverá encaminhar o fluxo para a atividade “Projeto encerrado”, conforme descrito abaixo.
* **Projeto encerrado**: Caso o usuário encaminhe para essa atividade, o acompanhamento do projeto será “aprovado” e o projeto de extensão terá sua a situação alterada para “Encerrado”, finalizando o fluxo e o projeto de extensão.

divs
