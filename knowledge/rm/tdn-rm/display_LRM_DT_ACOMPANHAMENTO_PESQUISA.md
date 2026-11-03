---
content_hash: ad651376f134b9dffe556a94a0039cbc1af360dfb114c714ae9f997832c2708c
fetched_at: '2026-06-29T00:06:14.625622+00:00'
page_id: '210048117'
product: rm
source: tdn-rm
title: DT_ACOMPANHAMENTO_PESQUISA
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_ACOMPANHAMENTO_PESQUISA
version: 24
---

# Acompanhamento de pesquisa

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Cadastros Iniciais:** | * Tabela dinâmica "Produto final obtido (PESQEXT002)" em "TOTVS Serviços Globais | Administração | Tabela dinâmica | Item da tabela dinâmica"; * Tabela dinâmica "Tipo de arrecadação (PESQEXT011)" em "TOTVS Serviços Globais | Administração | Tabela dinâmica | Item da tabela dinâmica"; * Tabela dinâmica "Tipo de rúbrica (PESQEXT012)" em "TOTVS Serviços Globais | Administração | Tabela dinâmica | Item da tabela dinâmica"; * Pesquisador/Extensionista em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Edital em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Tipo de bolsa em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Tipo de avaliação em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Motivo de arquivamento em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; * Área de conhecimento em "TOTVS Educacional | Atividades acadêmicas | Inovação, pesquisa e extensão"; |
| **Requisito (ISSUE):** | [PCREQ-5448](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-5448 "PCREQ-5448") |
| **Tabelas Utilizadas:** | * SPROJPROJETO - Cadastro da Proposta de Projeto (pesquisa/extensão) * SPROJARRECADACAO - Arrecadação de projeto * SPROJAVALIACAOPROJETO – Avaliadores do projeto de pesquisa/extensão * SPROJITEMAVALIACAO - Itens avaliados no projeto pelos avaliadores * SPROJBOLSATERCEIRO - Cadastro de Recursos de terceiros envolvidos * SPROJDESEMBOLSO - Desembolso do projeto * SPROJDESPESA - Cadastro de Despesas do Projeto * SPROJPARCERIA - Empresas parceiras no projeto * SPROJPARTICIPANTES - Cadastro de equipe do projeto * SPROJPLANOTRABALHO - Plano de trabalho do projeto * SPROJRECEITA - Cadastro de Receitas do Projeto * SPROJRECURSOBOLSAINST - Cadastro de Recursos da instituição * SPROJSOLICITACAOTIPOBOLSA - Cadastro de Solicitação de tipo de bolsas (pagamento) * SPROJEDITAL – Cadastro de edital * SPROJMOTIVOARQUIVO – Cadastro de motivo de arquivamento * SPROJPESQUISADOR – Cadastro de pesquisador/extensionista * SPROJPESQUISADORFILIAL – Cadastro de filial do pesquisador * SPROJTIPOAVALIACAO – Cadastro de tipos de avaliação * SPROJTIPOBOLSA – Cadastro de tipo de bolsa * SPROJTIPOBOLSAEDITAL – Cadastro de tipo de bolsa por edital * SPESALMOXARIFADO - Itens de Almoxarifado * SPESPATRIMONIO - Itens de Patrimônio * SPESGRUPOPESQUISA - Grupo de Pesquisa * SPESITENSPARCERIA - Itens de Parceria * SPESPLANEJAMENTO - Itens de Planejamento * SPESPRODUTOPRETENDIDO - Produtos Pretendidos * SPESRECONSIDERACAO - Reconsideração de Projeto * SPROJACOMPANHAMENTO - Acompanhamento de Projeto (pesquisa/extensão) * SPROJACOMPPARTICIPANTES - Participantes do Acompanhamento de Projeto (pesquisa/extensão) * SPROJACOMPARRECADACAO - Arrecadação do Acompanhamento de Projeto (pesquisa/extensão) * SPROJACOMPBOLSATERCEIRO - Bolsa de terceiro do Acompanhamento (pesquisa/extensão) * SPROJACOMPPLANOTRABALHO - Acompanhamento do Plano de trabalho (pesquisa/extensão) * SPROJACOMPDESEMBOLSO - Acompanhamento Desembolso (pesquisa/extensão) * SPROJACOMPDESPESA - Acompanhamento Despesa (pesquisa/extensão) * SPROJACOMPRECEITA - Acompanhamento Receita (pesquisa/extensão) * SPROJACOMPRECURSOBOLSAINST - Acompanhamento recurso bolsa institucional (pesquisa/extensão) * SPROJACOMPPRODUTOOBTIDO - Acompanhamento produto obtido (pesquisa/extensão) * SPESACOMPALMOXARIFADO - Acompanhamento itens de almoxarifado * SPESACOMPPATRIMONIO - Acompanhamento itens de patrimônio |
| **Versões/Release:** | 12.1.9 |

## Descrição

Possibilita ao usuário gerenciar seus processos referentes ao acompanhamento de pesquisa, permitindo realizar a apresentação, análise e avaliação utilizando-se do processo de aprovação através do FLUIG.

Pré-requisitos para utilizar a funcionalidade de cadastro de Solicitações de Acompanhamento de Propostas de Pesquisa

* Ter o FLUIG devidamente instalado e configurado conforme documentação:
  + Instalação: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409653>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409655>
* Ter o TOTVS Developer Studio (TDS) devidamente instalado e configurado.
  + Instalação: <http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7C+Developer+Studio>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=73078179>
* Criar no FLUIG os papéis necessários para a execução do fluxo de cadastro de Solicitações de Acompanhamento de Propostas de Pesquisa. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis).
  + Código = **pesquisador**| Descrição = **Pesquisador/Coordenador**
  + Código = **reitoria**| Descrição = **Reitoria**
  + Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.
  + Criar no TDS uma conexão com servidor FLUIG chamada "**Desenvolvimento**", pois no fluxo de cadastro de proposta existe uma referência para um servidor com esse nome:  
      
    Opção disponível em “TDS | Window | Show View | Other | Fluig \ Fluig Servers”
    - **Nome Servidor**: Desenvolvimento
    - **Host**: Neste campo deve-se informar o “nome da máquina” ou “IP” onde está instaldo o servidor do FLUIG.
    - **Porta**: Neste campo deve-se informar a porta que foi instaldo o servidor do FLUIG*(*geralmente o valor é 8080).
    - **Usuário**: Neste campo deve-se informar o usuário administrador da empresa no FLUIG.
    - **Senha**: Neste campo deve-se informar a senha do administrador da empresa no FLUIG.
    - **SSL**: Desmarcado
  + Criar um serviço para comunicação com o servidor de aplicação da linha RM (RM.Host), conforme dados abaixo:  
      
    Opção disponível em “TDS | Window | Show View | Other | Fluig | Visualização de Serviços”:  
    - **Servidor**: Desenvolvimento
    - **Código**: WSDATASERVER (Atenção: Para este campo, o valor deverá ser **WSDATASERVER**, visto que todos os datasets criados para o projeto fazem referência a este nome)
    - **Descrição**: Neste campo deve-se informar uma descrição sobre o serviço criado.
    - **URL**: [http://NOME\_DO\_SERVIDOR\_HOST:PPPP/wsDataServer/MEX?wsdl](http://nome_do_servidor_hostpppp/) (Para “NOME\_DO\_SERVIDOR\_HOST” deve-se informar o nome do servidor onde o “RM.Host” está instalado e rodando. Para “PPPP” deve-se informar a porta do WebService que foi configurada no arquivo de configuração do "Host" (tag HTTPPort).
    - **Tipo**: WebService
    - **API**: CXF - Fluig
  + Importar o fluxo de cadastro de proposta de extensão para a ferramenta TOTVS Developer Studio (TDS). Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em: **c:\totvs\CorporeRM\ObjetosGerenciais\Fluig**  
    - Configuração: [http://tdn.totvs.com/download/attachments/172300565/RM\_BT\_Montagem\_Ambiente\_Workflows\_Fluig.pdf](http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf?version=1&modificationDate=1432910252000&api=v2)
  + Para que o acesso as informações da linha RM possam ser disponibilizado no FLUIG, deve-se configurar os dados da conta do usuário que será utilizado pelo serviço de WebService. Os dados desse usuário (usuário, senha e e-mail) devem ser alterados no dataset chamado “**rm\_edu\_fontedados\_usuariorm.js**”, conforme o usuário configurado no passo 1 descrito abaixo nos procedimentos de configuração, pois todos os acessos as tabelas do TOTVS Educacional (via WebService) irão utilizar essa conta.
    - Acesse o arquivo em “**TDS | Window | Show View | Package Explorer | \_InovacaoPesquisaExtensaoBase | datasets | rm\_edu\_fontedados\_usuariorm.js***”*e realize as alterações nos dados da conta alterando a linha “**dsRetorno.addRow(['mestre', 'Usuário mestre', 'totvs', 'mestre@[rm.com.br](http://rm.com.br/)'])**”, caso os dados sejam diferentes.
  + Exportar para o servidor do FLUIG os Datasets, diagrama, formulário e eventos do cadastro de proposta de projeto de extensão.  
    - Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=189313846>

## **Procedimento para configuração**

**1º Passo**

Definir um usuário de acesso para comunicação (via WebService*)*para acesso as funcionalidades de extensão na linha RM. Esse usuário deverá ter acesso total nas funcionalidades, pois ele será utilizado para consulta e atualização dos dados nas tabelas no TOTVS Educacional pelo FLUIG (via integração).

Exemplo de usuário do TOTVS Educacional:

**Usuário**: mestre

**Senha**: totvs

**2º Passo**

Acessar o módulo de Globais e conceder acesso total nas novas funcionalidades para o usuário “definido” no passo 1 em:

“**Módulo Serviços Globais | Segurança | Perfis | Sistema Educacional | Acesso a Menus | Educacional [03] Atividades acadêmicas | [03.01] Acadêmico | [03.01.21] Inovação, Pesquisa e Extensão**”.

**3º Passo**

Para configurar as notificações referentes ao envio de relatório parcial/final de acompanhamento do projeto de extensão, deve-se realizar a configuração da “Central de Notificações”, que foi uma nova funcionalidade disponibilizada na versão 12.1.8, conforme documentação “<http://tdn.totvs.com/display/LRM/DT_Central_Notificacao>” na parte "Configuração de ambiente (Fluig e Parâmetros Globais e Contas de Comunicação)". Além das configurações realizadas nos passos acima, deve-se realizar o cadastro das mensagens conforme descrito abaixo:

 Acessar o cadastro de mensagens de notificação, disponibilizado em “**TOTVS Educacional | Atividades Acadêmicas | Central de Notificações | Mensagens de notificação**”:

 1)       Mensagem de relatório **parcial** de acompanhamento

 Informar os dados da mensagem para relatório parcial:

* + - Aba “E-mail”:

                    **-****Esta mensagem será enviada com o objetivo de**: Enviar notificação ao coordenador do projeto sobre envio de relatório **parcial** de acompanhamento 

**- Tags Disponíveis**: Clicando nessa opção, pode-se inserir algumas tagspré-definidas para serem inseridas no texto da mensagem e que serão substituídas pelos registros correspondentes. 

**- Assunto da mensagem**: Deve-se informar o assunto da mensagem de e-mail; 

**- Ativar envio por e-mail**: Deve-se marcar esse campo, caso deseje enviar e-mail ao coordenador do projeto para envio de relatório parcial; 

**- Texto**: Deve-se criar o texto que será enviado por e-mail para o coordenador do projeto para envio do relatório parcial;  

* + - Aba “Notificações Fluig”:

**- Ativar notificação via Fluig**: Deve-se marcar esse campo, caso deseje enviar uma notificação ao coordenador do projeto para envio do relatório parcial dentro do fluig; 

**- Texto**: Deve-se criar o texto que será enviado por notificação no fluigpara o coordenador do projeto para envio do relatório parcial; 

 2)       Mensagem de relatório **final** de acompanhamento 

Informar os dados da mensagem para relatório final: 

* + - Aba “E-mail”:

**-****Esta mensagem será enviada com o objetivo de**: Enviar notificação ao coordenador do projeto sobre envio de relatório **final** de acompanhamento 

**- Tags Disponíveis**: Clicando nessa opção, pode-se inserir algumas tagspré-definidas para serem inseridas no texto da mensagem e que serão substituídas pelos registros correspondentes. 

**- Assunto da mensagem**: Deve-se informar o assunto da mensagem de e-mail; 

**- Ativar envio por e-mail**: Deve-se marcar esse campo, caso deseje enviar e-mail ao coordenador do projeto para envio de relatório final; 

**- Texto**: Deve-se criar o texto que será enviado por e-mail para o coordenador do projeto para envio do relatório final; 

* + - Aba “Notificações Fluig”:

**- Ativar notificação via Fluig**: Deve-se marcar esse campo, caso deseje enviar uma notificação ao coordenador do projeto para envio do relatório final dentro do fluig; 

**- Texto**: Deve-se criar o texto que será enviado por notificação no fluigpara o coordenador do projeto para envio do relatório final;

 

**4º Passo**

Acessar os parâmetros do sistema para configurar a central de notificações para relatórios (parcial/final) do projeto, disponibilizado no menu “**Módulo Educacional | Configurações | Parâmetros | 15 – Educacional |****15.05 – Integração | 15.05.10 - Fluig**”.

* + - Acad. Social – Geral

* + - * **Código da conta de comunicação**: Informe a conta de comunicação utilizada para integração com o fluig. Para mais informações de cadastro dessa conta, acesse a documentação disponível em <http://tdn.totvs.com/display/public/LRM/DT_Academia_Social> na seção “Configuração de ambiente”;

 

* + - Notificações

* + - * **Gerar estrutura de notificação do Educacional no Fluig?** Verifique se os eventos de notificação foram gerados no fluig, ou seja, se a coluna “Gerado?” está com o valor “sim” não será necessário essa configuração, pois já foi realizada. Caso esteja com o valor “não”, deve-se marcar o parâmetro “Gerar estrutura de notificação do Educacional no Fluig” e avançar o parametrizador para que o sistema configure o fluig com os novos eventos de notificação.

Acessar os parâmetros do sistema para configurar o módulo de extensão, disponibilizado no menu “**Módulo Educacional | Configurações | Parâmetros | 15 – Educacional | 15.08 – Pesquisa e Extensão**”.

* + - Pesquisa e Extensão 2 / 4  
        
      * **Dias para aviso de envio de relatório parcial/final do projeto**: Informe os dias que deseja avisar (e-mail ou notificação do fluig) aos coordenadores dos projetos de extensão para enviar os relatórios (parcial e final) de acompanhamento dos projetos. Exemplo: 10,15,20,25

**5º Passo**

Acessar o arquivo de configuração do “RM.Host” (RM.Host.exe.config ou RM.Host.Service.exe.config) e incluir as tags conforme imagem abaixo, caso não existam no arquivo.

* + **JobServer3Camadas**: O valor dessa tag deverá ser “true” para possibilitar o agendamento de Jobs pela funcionalidade do módulo de Globais.
  + **DefaultDB**: O valor dessa tag deverá ter o valor do alias utilizado na linha RM para conexão (no exemplo acima, o alias se chama “CorporeRM”), assim será possível acessar o banco de dados RM pelo acesso via WebServices.
  + **HTTPPort**: O valor dessa tag deverá ter o valor da porta utilizada para acesso ao WebService dos serviços da linha RM. Por padrão, utilizamos a porta 8051, conforme mostra a imagem acima.
  + Outra configuração necessária para agendamento de Jobs, será no “**Gerenciamento de Alias**” (no momento do login no RM) para habilitar o processamento de Jobs. Neste cadastro, acessar a aba “**Serviços**” e marcar o parâmetro “**Habilitar Processamento de Job**”.

Caso tenha alterado as configurações do arquivo, deve-se parar o serviço e iniciar novamente para que as alterações possam estar disponíveis. Essas configurações serão necessárias para enviar “notificação” aos coordenadores do projeto sobre o envio de relatórios (parcial/final) no acompanhamento do projeto de extensão e pesquisa.

## Procedimento para Utilização

Depois que todos os passos acima forem configurados, o workflowde acompanhamento do projeto de extensão estará disponível no fluig, conforme descrito abaixo:

Acompanhamento de projeto de extensão disponível em: “**Fluig | Processos | Iniciar Solicitações | Processos disponíveis | Educacional | Inovação, Pesquisa e Extensão | Pesquisa | Acompanhamento de pesquisa | Acompanhamento de projeto de Pesquisa**”



O usuário deve iniciar uma nova solicitação escolhendo a opção "**Educacional | Inovação, Pesquisa e Extensão | Acompanhamento de Pesquisa**". É necessário estar vinculado ao papel de "***Pesquisador***" para realizar essa solicitação.

Nesse fluxo o responsável poderá realizar uma solicitação extraordinária, que diz repeito a qualquer alteração alteração voltada a utilização de recurso. Além de submeter o acompanhamento para avaliação parcial/final.

### Avaliação parcial/final:

Plano de trabalho: Os dados do plano de trabalho são uma cópia de uma estrutura já existente, e permite ao usuário alterar a situação da atividade (0 - Em execução | 1 - Encerrada). 

* + - Relatório Parcial: O coordenador deverá atualiza a situação do plano de trabalho conforme evolução do projeto.
    - Relatório Final: O coordenador deverá atualiza a situação do plano de trabalho conforme evolução do projeto.

Item de almoxarifado: Os dados do almoxarifado são uma cópia de uma estrutura já existente, e permite ao usuário alterar a situação do item para "Não atendido", "Parcialmente atendido" e "Totalmente atendido". 

* + - Relatório Parcial: O coordenador deverá atualiza a situação do item conforme atendimento de sua necessidade.
    - Relatório Final: O coordenador deverá atualiza a situação do item conforme atendimento de sua necessidade.

Item de patrimônio: Os dados do patrimônio são uma cópia de uma estrutura já existente, e permite ao usuário alterar a situação do item para "Não atendido", "Parcialmente atendido" e "Totalmente atendido".

* + - Relatório Parcial: O coordenador deverá atualiza a situação do item conforme atendimento de sua necessidade.
    - Relatório Final: O coordenador deverá atualiza a situação do item conforme atendimento de sua necessidade.

Cronograma de desembolso: 

* + - Relatório Parcial: Na 1ª vez que o coordenador for enviar o relatório parcial, o sistema faz uma cópia dos dados do cronograma de desembolso que foi aprovado no projeto para a estrutura de acompanhamento. Essas informações poderão ser alteradas conforme a situação do projeto. As informações originais do projeto não serão alteradas.
    - Relatório Final: Serão carregas as últimas informações aprovadas por solicitações parciais para envio da solicitação final.

### Avaliação final:

O sistema realiza a cópia dos dados aprovados no projeto, dos seguintes itens, abaixo, e, também, de todas as informações citadas para um relatório parcial:

Informações financeiras do projeto:

* + - Receitas:

* 1. 1. 1. Arrecadação
        2. Recursos da Instituição
        3. Rubricas
        4. Recursos de terceiros
        5. Rubricas de terceiros
* + - Despesas

Será disponibilizado um novo sub-formulário para preenchimentos dos produto obtidos pelo projeto:

* + - Produtos obtidos

### Solicitações Extraordinárias:

### 

Os dados do projeto serão exibidos para que o coordenador possa realizar adequações nas informações da equipe, dos recursos solicitados e nos planos de trabalho, conforme descrito abaixo:

Equipe de execução do projeto: Serão exibidos os dados da equipe do projeto para que o coordenador possa realizar qualquer alterar necessária, tais como, excluir um membro da equipe ou até mesmo cadastrar um novo membro.

Plano de trabalho do projeto: Serão exibidos os dados do plano de trabalho do projeto para que o coordenador possa realizar as devidas alterações ou inclusão de novas atividades.

Item de almoxarifado: Serão exibidos os dados dos itens de almoxarifado do projeto para que o coordenador possa realizar as devidas alterações, ou inclusão de novos itens.

Item de patrimônio: Serão exibidos os dados de itens de patrimônio do projeto para que o coordenador possa realizar as devidas alterações, ou inclusão de novos patrimônios a serem utilizados.

### Avaliar solicitação extraordinária:

### 

Nessa etapa as solicitações são avaliadas e poderão ser aprovadas ou reprovadas. Caso sejam aprovadas, elas serão alteradas nas informações do projeto, caso não sejam aprovados elas serão registradas como histórico, mas não serão alteradas no projeto.

### Certificados:

### 

São gerados os certificados para o coordenador do projeto e todos os envolvidos. Os certificados, criados, podem ser visualizados e emitidos em TOTVS Educacional (**Atividades acadêmicas | Certificados/Diplomas**).
