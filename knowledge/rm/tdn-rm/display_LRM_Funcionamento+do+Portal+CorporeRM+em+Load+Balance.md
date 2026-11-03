---
content_hash: 073964303849a98090ada2f8de24486cc52d50d63c6a42db71bbf2d4735b6153
fetched_at: '2026-06-29T00:10:57.262981+00:00'
page_id: '59900196'
product: rm
source: tdn-rm
title: Funcionamento do Portal CorporeRM em Load Balance
type: documentation
url: https://tdn.totvs.com/display/LRM/Funcionamento+do+Portal+CorporeRM+em+Load+Balance
version: 1
---

**Introdução**

Em ambientes que utilizam Load Balance, são necessárias algumas configurações para o correto funcionamento do RM Portal.

Essas novas configurações irão permitir o armazenamento dos dados de sessão em banco de dados.

**Desenvolvimento/Procedimento**

**Para cada servidor web:**

- Abra o Prompt de Comando do Windows  (Iniciar -> Programas -> Acessórios -> Prompt de Comando)

 - Pare o serviço de publicação da WWW através do comando *net stop w3svc*

**Para o servidor de banco de dados:**

Caso tenha IIS instalado na máquina:

- Abra o Prompt de Comando do Windows  (Iniciar -> Programas -> Acessórios -> Prompt de Comando)

- Pare o serviço de publicação da WWW através do comando *net stop w3svc*

- Dentro da pasta Windows\Microsoft.NET\Framework\v2.0.50727 execute o programa aspnet\_regsql.exe\*

- O programa criará um banco de dados, portanto é preciso que informe um usuário com privilégios suficientes para executar tal ação

- Por padrão ele criará o banco com o nome ASPState

\*Caso não tenha Framework .NET instalada no servidor de Banco de Dados, o programa pode ser executado em um dos servidores web, porém será informado no programa o nome do servidor de banco de dados.

Caso tenha IIS instalado na máquina:

- Abra o Prompt de Comando do Windows  (Iniciar -> Programas -> Acessórios -> Prompt de Comando)

- **Inicie** o serviço de publicação da WWW através do comando *net start  w3svc*

**Novamente para cada servidor web:**

  - Abra o Prompt de Comando do Windows  (Iniciar -> Programas -> Acessórios -> Prompt de Comando)

- **Inicie** o serviço de publicação da WWW através do comando *net start w3svc*

- Abra o arquivo web.config da aplicação e faça a seguinte configuração para a tag <sessionState>:

<sessionState mode="SQLServer" sqlConnectionString="Data Source=<servidor de banco>;user id=<usuario>;password=<senha>" cookieless="false" timeout="20" />
