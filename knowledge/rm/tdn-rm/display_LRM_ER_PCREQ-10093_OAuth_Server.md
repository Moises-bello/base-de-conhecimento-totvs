---
content_hash: b32c98e1372864763c6ef64f8fbb6f2295b6ec2898d71a74bcc85ba6c42fc9cf
fetched_at: '2026-06-29T00:06:28.933018+00:00'
page_id: '233765123'
product: rm
source: tdn-rm
title: ER_PCREQ-10093_OAuth_Server
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-10093_OAuth_Server
version: 141
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | FRAMEWORK | **Módulo** | SERVIÇOS GLOBAIS |
| **Segmento Executor** |  | | |
| **Projeto1** | * [R\_FRW\_FRW002](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_FRW_FRW002 "R_FRW_FRW002") | **IRM1** | * [PCREQ-10036](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-10036 "PCREQ-10036") |
| **Requisito1** | PCREQ-10093 | **Subtarefa1** | 1. [PDR\_FRW\_FRW002-272](http://jira.totvs.com.br/browse/PDR_FRW_FRW002-272) |
| **Chamado2** |  | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Definir um mecanismo para gerenciamento de autorização via OAuth 2.0 para os serviços HTTP da Linha RM. Este mecanismo deve ser reutilizado nos WebServices da WebAPI e nos demais WebServices expostos pelo RM.Host.

*<Nesta etapa informar o objetivo da especificação do requisito, ou seja, o que a funcionalidade deve fazer. Exemplo: Permitir que o usuário defina o percentual mínimo em espécie (dinheiro), a referência mínima para calculo dos débitos do aluno e o período de validade do parâmetro de negociação>.*

## Definição da Regra de Negócio

OAuth 2.0 é um protocolo aberto para permitir a autorização segura de forma simples e padronizada para aplicações Web, Mobile e Desktop. 

A segurança baseada em tokens consiste em enviar um token de acesso em cada requisição para acesso à recursos restritos. Um token típico, além de outras informações, contém o que chamamos de escopos (scopes), que representam a intenção do usuário ao acessar determinado recurso, por exemplo: acesso de leitura, escrita, gerenciamento de recursos, etc.

Esta implementação deve ser dividida em três partes:

1. Criar uma forma de obter *tokens* de autorização;
2. Criar uma forma de validar estes *tokens* no acesso à recursos;
3. Garantir que os recursos não estejam acessíveis caso este *token* não exista;

Importante:

* Esta especificação não trata sobre a forma de envio desses tokens dos clientes para o servidor de recursos. Consumo da API é responsabilidade do OAuth Client.
* OAuth 2.0 é usado para autorizar o acesso. [OAuth 2 não é sobre autenticação](http://oauth.net/articles/authentication/), o padrão não diz nada sobre o usuário. É sobre o que um aplicativo cliente pode ou não fazer. O aplicativo cliente não conhece nada sobre quem concedeu esta autorização. Para isto existe outro padrão, chamado [OpenId Connect](http://openid.net/connect/), não abordado neste requisito.

## Fluxos OAuth 2.0

Há uma distinção importante a ser feita com relação aos aplicativos clientes. Dependendo do tipo de cliente é preciso utilizar uma maneira diferente de obter o *token* para se manter seguro. Não existe uma única maneira segura para todos os tipos de clientes. Estas maneiras são chamadas de Fluxos.

Uma das restrições podem ser entendidas da seguinte forma: quando uma aplicação solicita um token de autorização em nome de um usuário, onde este token pode ser entregue? 

#### Authorization Code

Normalmente utilizado por aplicações que são processadas em um servidor, por exemplo uma aplicação web ASP.NET MVC. Necessita de um interação com o usuário para conceder a autorização.

<Colar o diagrama de fluxo>

#### Implicit

Normalmente utilizado aplicações nativas, baseadas em um navegador, por exemplo, uma aplicação Angular JS ou um aplicativo móvel. Necessita de um interação com o usuário para conceder a autorização.

#### Resource Owner Password Credential

Normalmente utilizado em aplicações confiáveis, pois ela deve coletar as credenciais do usuário e obter a autorização munido dessas credenciais. Não necessita de uma interação com o usuário para conceder a autorização, pois já foram utilizadas as suas credenciais.

#### Cliente Credentials

Este fluxo é utilizado para interação direto do aplicativo cliente com o servidor de recursos. Não existe um usuário envolvido neste fluxo. São utilizadas credenciais do próprio cliente.

## Papeis principais

O OAuth2 possuiu quatro papéis principais:

**User (Resource Owner):** Entidade capaz de possibilitar acesso a um recurso protegido. Quando ele é uma pessoa, nos referimos ao usuário final.

**Resource Server:**  É o servidor que hospeda os recursos protegidos capaz de aceitar e responder as solicitações usando tokens de acesso. 

**Authorization Server:** É o servidor capaz de fornecer *tokens* de acesso a um cliente depois de uma autenticação com sucesso do resource owner e obtendo autorização. Chamado de STS (Security Token Service)

**Client:** É a aplicação que acessa um recurso protegido em nome do resource owner e com sua autorização. 

## Tipos de Clientes

**Confidential Client:** É o cliente capaz de manter confidencialidade das suas credenciais. Estamos falando de credenciais de clientes e não de usuários. Tipicamente temos um *ClienteId* e um *ClientSecrect*. Ex.: MVC App (Server to Server)

**Public Client:** São incapazes de manter a confidencialidade de suas credenciais. Aplicativos Mobile, ou baseados no browser. Ex.: Mobile App, JS App.

## Endpoints

Authorization Endpoint:  utilizado pelo cliente para obter autorização do resource owner através de redirecionamento. OAuth 2.0 não especifica a forma como o resource owner deve se autenticar, isso significa que normalmente o redirecionamento se dará para uma página de login.

Token Endpoint: utilizado pelo cliente para trocar um código de autorização por um *token* de acesso (*client authentication*).

Redirection Endpoint: ponto do cliente onde será recebido o *token*. Os fluxos apresentados são baseados em redirecionamento. Utilizado pelo servidor de autorização para retornar respostas contendo as credenciais de autorização para o *client*.

## Identity Server 3

A implementação de um servidor de autorização ou STS - *Security Token Service*, não é trivial. Precisaríamos desenvolver diferentes fluxos, pontos de extremidade, ter um meio de gerar *tokens* e mais. Por isto, vamos utilizar um framework chamado [Identity Server 3](https://identityserver.github.io/Documentation/).

É uma implementação open source, aberta, extensível, faz parte do .NET Foundation, mantida pela comunidade .NET apoiada pela Microsoft.

Vamos utilizar esse mecanismo e adaptá-lo à arquitetura da Linha RM.

Passos para essa adaptação:

1. Implementar ponto de extensão do STS para utilizar a base do RM como fonte de dados de usuários:

   1
   complete
   Criar serviço REST no Host para expor os Alias

   2
   complete
   Criar serviço REST no Host para expor a validação de usuário da Linha RM para o STS. O STS não terá referência direta para a Lib.
2. Implementar serviço customizado de telas para o STS:

   3
   complete
   Criar ViewService  
   Vide: <https://identityserver.github.io/Documentation/docsv2/advanced/customizingViews.html>

   4
   complete
   Ajustar tela de Login do STS para incluir seletor de Alias;

   5
   complete
   Enviar valor do Alias para o Serviço de Validação de Usuários;
3. Implementar ponto de extensão do STS para utilizar a base do RM como fonte de dados de clientes:

   11
   incomplete
   Criar tabelas necessárias para armazenamento de informações de clientes como esperado pelo IdentityServer3 na base do RM;

   12
   incomplete
   Criar serviço REST para expor os dados de clientes do RM para o STS;

   6
   incomplete
   Criar serviço para leitura de dados de clientes pelo STS;  
   Vide:  <https://identityserver.github.io/Documentation/docsv2/ef/clients_scopes.html>

   7
   incomplete
   Criar cadastro de aplicativos clientes no RM;
4. Implementar ponto de extensão do STS para utilizar a base do RM como fonte de dados de escopos. (Pode ser opcional na 1ª fase, caso seja dividido em entregas.):

   13
   incomplete
   Criar tabelas necessárias para armazenamento de informações de escopos como esperado pelo IdentityServer3 na base do RM;

   14
   incomplete
   Criar serviço REST para expor os dados de escopos do RM para o STS;  

   8
   incomplete
   Criar serviço para leitura de dados de escopos pelo STS  
   Vide:  <https://identityserver.github.io/Documentation/docsv2/ef/clients_scopes.html>  

   9
   incomplete
   Criar cadastro de escopos no RM;
5. Implementar ponto de extensão do STS para utilizar a base do RM como fonte de dados operacionais do STS:  

   10
   incomplete
   Serviços obrigatórios para produção: AuthorizationCodeStore, TokenHandleStore, RefreshTokenStore, ConsentStore  
   Vide: <https://identityserver.github.io/Documentation/docsv2/ef/operational.html>  
   Vide: <https://identityserver.github.io/Documentation/docsv2/configuration/serviceFactory.html>
6. Blindar serviços do RM para não aceitar requisições sem que contenham o Token de Autorização:
7. Validar Token de Autorização no STS nos serviços do RM:

*<Regra de negócio é o que define a forma de fazer o negócio, o processo definido e/ou as regras que devem ser contempladas. Devem ser descritas restrições, validações, condições e exceções do processo. Caso necessário, incluir neste capítulo também regras de integridade que devem ser observadas no momento do desenvolvimento>.*

*<Na tabela abaixo informe quais são as rotinas envolvidas, o tipo de operação, a opção de menu e se necessário uma breve descrição das regras de negócio relacionadas a rotina>.*

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [ACAA040 – Parâmetros] | [Alteração] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA050 – Negociação Financeira] | [Envolvida] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA060 – Cadastro de Pedidos] | [Criação] | [Atualizações -> Acadêmico-> Cadastros] | - |

***Exemplo de Aplicação:***

* *Criar o campo “% Mínimo Espécie” (AAA\_PERESP) onde o usuário informará o % que o aluno pagará em dinheiro. Esse % poderá ser alterado durante a negociação.*
* *Criar o campo “Referência Mínima para Cálculo” (AAA\_REFCAL) onde o usuário informará um dos 4 valores disponíveis para pagamento das mensalidades  como a referência mínima para calcular o débito total do aluno.*
* *Criar o parâmetro MV\_ACPARNE que definirá se as informações de “% Mínimo Espécie” e “Referência Mínima para Cálculo” serão obrigatórias.*
* *O parâmetro MV\_ACPARNE deve ter as seguintes opções: 1=Obrigatório e 2=Opcional. Deve ser inicializado como opcional>.*

***Tabelas Utilizadas***

* *SE2 – Cadastro de Contas a Pagar*
* *FI9 – Controle de Emissão de DARF>.*

### Opcional

## Protótipo de Tela

*<Caso necessário inclua protótipos de telas com o objetivo de facilitar o entendimento do requisito, apresentar conceitos e funcionalidades do software>.*

**Protótipo 01**

### Opcional

## Fluxo do Processo

*<Nesta etapa incluir representações gráficas que descrevam o problema a ser resolvido e o sistema a ser desenvolvido. Exemplo: Diagrama - Caso de Uso, Diagrama de Atividades, Diagrama de Classes, Diagrama de Entidade e Relacionamento e Diagrama de Sequência>.*

### Opcional

## Dicionário de Dados

**Arquivo ou Código do Script:** AAA – Negociação Financeira / \*Versao=CP.2014.12\_03\*/

 

|  |  |
| --- | --- |
| **Índice** | **Chave** |
| **01** | <FI9\_FILIAL+FI9\_IDDARF+FI9\_STATUS> |
| **02** | <FI9\_FILIAL+FI9\_FORNEC+ FI9\_LOJA+FI9\_EMISS+FI9\_IDDARF> |
| **03** | <FI9\_FILIAL+FI9\_FORNEC+ FI9\_LOJA+FI9\_PREFIX+FI9\_NUM+FI9\_PARCEL+FI9\_TIPO> |

|  |  |
| --- | --- |
| **Campo** | <AAA\_PERESP> |
| **Tipo** | <N> |
| **Tamanho** | <6> |
| **Valor Inicial** | <Varia de acordo com o tipo informado. Por exemplo, quando o campo “tipo” for date, neste campo pode ser informado uma data>. |
| **Mandatório** | Sim (  ) Não (  ) |
| **Descrição** | <Referência Mínima para Cálculo> |
| **Título** | <Ref.Calc.> |
| **Picture** | <@E999.99> |
| **Help de Campo** | <Informar o % que o aluno pagará em dinheiro. Esse % poderá ser alterado durante a negociação> |

### (Opcional)

## Grupo de Perguntas

 

*<Informações utilizadas na linha Protheus>.*

 

**Nome: FINSRF2**

|  |  |
| --- | --- |
| **X1\_ORDEM** | 01 |
| **X1\_PERGUNT** | Emissão De |
| **X1\_TIPO** | D |
| **X1\_TAMANHO** | 8 |
| **X1\_GSC** | G |
| **X1\_VAR01** | MV\_PAR01 |
| **X1\_DEF01** | Comum |
| **X1\_CNT01** | '01/01/08' |
| **X1\_HELP** | Data inicial do intervalo de emissões das guias de DARF a serem consideradas na seleção dos dados para o relatório |

### (Opcional)

## Consulta Padrão

*<Informações utilizadas na linha Protheus>*

**Consulta: AMB**

|  |  |
| --- | --- |
| **Descrição** | Configurações de Planejamento |
| **Tipo** | Consulta Padrão |
| **Tabela** | “AMB” |
| **Índice** | “Código” |
| **Campo** | “Código”; ”Descrição” |
| **Retorno** | AMB->AMB\_CODIGO |

### (Opcional)

## Estrutura de Menu

*<Informações utilizadas na linha Datasul>.*

**Procedimentos**

|  |  |  |  |
| --- | --- | --- | --- |
| **Procedimento** |  |  |  |
| **Descrição** | (Max 40 posições) | (Max 40 posições) | (Max 40 posições) |
| **Módulo** |  |  |  |
| **Programa base** |  |  |  |
| **Nome Menu** | (Max 32 posições) | (Max 32 posições) | (Max 32 posições) |
| **Interface** | GUI/WEB/ChUI/Flex | GUI/WEB/ChUI/Flex | GUI/WEB/ChUI/Flex |
| **Registro padrão** | Sim | Sim | Sim |
| **Visualiza Menu** | Sim/Não | Sim/Não | Sim/Não |
| **Release de Liberação** |  |  |  |

**Programas**

|  |  |  |  |
| --- | --- | --- | --- |
| **Programa** |  |  |  |
| **Descrição** | (Max 40 posições) | (Max 40 posições) | (Max 40 posições) |
| **Nome Externo** |  |  |  |
| **Nome Menu/Programa** | (Max 32 posições) | (Max 32 posições) | (Max 32 posições) |
| **Nome Verbalizado**[1]**** | (Max 254 posições) | (Max 254 posições) | (Max 254 posições) |
| **Procedimento** |  |  |  |
| **Template** | (Verificar lista de opções no man01211) | (Verificar lista de opções no man01211) | (Verificar lista de opções no man01211) |
| **Tipo**[2]**** | Consulta/Manutenção/ Relatório/Tarefas | Consulta/Manutenção/ Relatório/Tarefas | Consulta/Manutenção/ Relatório/Tarefas |
| **Interface** | GUI/WEB/ChUI/Flex | GUI/WEB/ChUI/Flex | GUI/WEB/ChUI/Flex |
| **Categoria**[3]**** |  |  |  |
| **Executa via RPC** | Sim/Não | Sim/Não | Sim/Não |
| **Registro padrão** | Sim | Sim | Sim |
| **Outro Produto** | Não | Não | Não |
| **Visualiza Menu** | Sim/Não | Sim/Não | Sim/Não |
| **Query on-line** | Sim/Não | Sim/Não | Sim/Não |
| **Log Exec.** | Sim/Não | Sim/Não | Sim/Não |
| **Rotina (EMS)** |  |  |  |
| **Sub-Rotina (EMS)** |  |  |  |
| **Localização dentro da Sub Rotina (EMS)** |  |  |  |
| **Compact**[4]**** | Sim/Não | Sim/Não | Sim/Não |
| **Home**[5]**** | Sim/Não | Sim/Não | Sim/Não |
| **Posição do Portlet**[6]**** | 0 – Top Left  1 – Top Right  2 – Bottom Left  3 – Bottom Right | 0 – Top Left  1 – Top Right  2 – Bottom Left  3 – Bottom Right | 0 – Top Left  1 – Top Right  2 – Bottom Left  3 – Bottom Right |
| **Informar os papeis com os quais o programa deve ser vinculado** |  |  |  |

**Cadastro de Papéis**

*<O cadastro de papéis é obrigatório para os projetos de desenvolvimento FLEX a partir do Datasul 10>.*

*<Lembrete: o nome dos papeis em inglês descrito neste ponto do documento, devem ser homologados pela equipe de tradução>.*

|  |  |
| --- | --- |
| **Código Papel** | **(máx 3 posições)** |
| **Descrição em Português\*** |  |
| **Descrição em Inglês\*** |  |

---

[1] Nome Verbalizado é obrigatório para desenvolvimentos no Datasul 10 em diante.

[2] Tipo é obrigatório para desenvolvimento no Datasul 10 em diante

[3] Categorias são obrigatórias para os programas FLEX.

[4] Obrigatório quando o projeto for FLEX

[5] Obrigatório quando o projeto for FLEX

[6] Obrigatório quando o projeto for FLEX

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
