---
content_hash: 6109735f096ea395afaee71db3197c771bc01c949fa0f6d6e33209c9a4448837
fetched_at: '2026-06-29T00:08:45.550946+00:00'
page_id: '311632279'
product: rm
source: tdn-rm
title: Provedor de Dados
type: documentation
url: https://tdn.totvs.com/display/LRM/Provedor+de+Dados
version: 72
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é trazer uma visão de como funciona tela de Provedor de Dados.

# Introdução:

---

       Um determinado "Provedor de Dados" deve ser criado para permitir que o TReports se comunique com uma determinada fonte de dados. Todas as informações a serem mostradas em um determinado relatório serão recuperadas de um determinado provedor de dados. Atualmente a ferramenta disponibiliza as opções: Dados Relacionais e API Padrão TOTVS.

       Em uma empresa, diversos provedores de dados poderão ser cadastrados, buscando dados em locais completamente diferentes.

       Em um único relatório, dados poderão ser recuperados de provedores de dados diferentes.

       Ex: Meu relatório pode ser gerado em minha empresa porém as informações desse relatório podem estar localizadas na nuvem.

# Como criar:

---

       Para criar um novo Provedor de Dados, basta clicar em "+ Novo" e informar os campos abaixo:

***Código do provedor:***Informe o código do Provedor de Dados, deve ser um código único, é por ele que o Provedor de Dados será identificado.

***Descrição:*** Informe uma descrição.

***Tipo do provedor:***  Dados Relacionais.

***Fonte de Dados:*** Selecione se a fonte de dados será um "Provedor banco de dados" ou "Provedor integrado".

**Dados Relacionais:**

Dados Relacionais1Provedor banco de dados

Com essa opção selecionada, o mecanismo de execução do TReports enviará para um determinado provedor uma série de sentenças SQL (de acordo com o relatório criado).

Essas sentenças SQL serão executadas nesses provedores que são responsáveis em chamar uma determinada Fonte de Dados.

Atualmente o TReports tem a capacidade de trabalhar com os seguinte banco de dados relacionais: Oracle, Sql Server, MySql, Postgre, Firebird e DB2.

Apesar de suportar os bancos citados acima, o TReports foi homologado somente em SQL e ORACLE.

Selecione o tipo de banco de dados desejado e note que os parâmetros do banco são buscados automaticamente.

É possível adicionar ou remover um parâmetro, desde que o mesmo não seja do tipo senha.

Para isso, basta clicar nos botões azuis de "Adicionar" ou "Excluir".

Preencha as informações do Banco de Dados clicando em "Editar" e informando o "Valor".

***Exemplo prático abaixo:***

2Provedor integrado

O Provedor Integrado é um provedor remoto. Nesse caso, a extração dos dados nesse provedor passará por todo o mecanismo de segurança do ERP.

Abaixo, será dado o exemplo do ERP RM. Porém, outros provedores de dados específicos de outros ERPS poderão ser criados. Para isso, basta seguir uma especificação de criação de provedores.

Para mais detalhes de como criar um Provedor Integrado, acesse a página [Provedor Integrado](http://tdn.totvs.com/x/gBnAFQ).

É necessário que o Host.exe esteja em execução e o arquivo de configuração do Host tenha os parâmetros HTTPPORT e DEFAULTDB devidamente preenchidos.

Protocolo

Informe se o protocolo é http ou https

Host

Nome da máquina que está rodando o RM.Host.exe

Porta

Informe a porta em que os serviços estão registrados.

Exemplo: 8051

Rota

Exemplo:

Default: api/trep/v1/dbdataproviders   
Protheus: api/protheus/dbdataproviders/v1

Tipo de autenticação

***Basic:*** Neste tipo de autenticação é necessário informar o Usuário e Senha do RM.

***OAuth:*** Neste tipo de autenticação não é necessário informar o Usuário e Senha do RM, ele é buscado automaticamente pelo usuário que está logado no TReports.

***Exemplo prático abaixo:***

Buscar parâmetros

Deve ser utilizado para recuperar as informações de conexão com uma determinada fonte de dados.

Utilize o botão "Testar conexão" para testar sua conexão.

3API Padrão Totvs

       Para criar um novo Provedor de Dados API PAdrão TOTVS, basta clicar em "+ Novo" e informar os campos abaixo:

***Código do provedor:***Informe o código do Provedor de Dados, deve ser um código único, é por ele que o Provedor de Dados será identificado.

***Descrição:*** Informe uma descrição.

***Tipo do provedor:***  Api Padrão TOTVS.

***Fonte de Dados:*** Api Git.

***Complemento da Rota:***Nome do diretório virtual. *Ex.:* Nome do diretório virtual do iis.

***Protocolo:***Selecione se o protocolo é HTTP ou HTTPS.

***Host:***Nome da máquina.

***Porta:***Você informa a porta do seu protocolo. Porém vem marcado por default porta 80 quando selecionado http e porta 443 quando selecionado https.

***Tipo de Autenticação:***Informações de segurança.

***- Basic:***Chamada da API.  
***- OpenID:***Autenticação onde solicita o access token de um service provider.   
*Ex.:* rac google service provider.

***Exemplo prático abaixo:***

false

***Na elaboração de um relatório, etapa de Conexões, quando selecionado o tipo API, não será possível incluir/utilizar outro tipo de conexão.***

4Carol (Tempo real)

       Para criar um novo Provedor de Dados Carol - Tempo Real, basta clicar em "+ Novo" e informar os campos abaixo:

***Código do provedor:***Informe o código do Provedor de Dados, deve ser um código único, é por ele que o Provedor de Dados será identificado.

***Descrição:*** Informe uma descrição.

***Tipo do provedor:***  Carol

***Fonte de Dados:*** Carol  (Tempo Real)

Devem ser preenchidos os seguintes parâmetros:

ApiURL: Rota para alcançar os métodos da Api da Carol.

[ConnectorId](https://docs.carol.ai/docs/1-swagger#generating-connector-token-in-an-environment): Identificador do connector Carol que irá ser utilizado

[A](https://docs.carol.ai/docs/1-swagger#generating-connector-token-in-an-environment)[piKey](https://docs.carol.ai/docs/1-swagger#generating-connector-token-in-an-environment): Chave para acesso ao connector. (deve ser gerada na aplicação Carol)

***Exemplo prático abaixo:***

false

***Neste momento, o data provider do tipo Carol só está disponível para utilização em Dashboards.***

Ao utilizar um Data Provider Carol numa fonte de dados do Dashboard, será necessário configurar a consulta Carol que deseja ser executada.

O TReports trabalha somente com os dados das [agregações e subagregações](https://docs.carol.ai/docs/querying-data#31-aggregation-types) utilizdas na consulta Carol. as inforações de chaves agrupadas (TERM, DATE\_HISTOGRAM) e valores calculado de cada agrupamento (COUNT, MAXIMUM, MINIMUM,...) são disponibilizado para uso no dashboard.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.22 ou Superiores

false

**Processo:** Provedor de Dados

falsefalse

**Status:** Concluído

false

**Data:** 14/05/2019

false

**Autores:**
