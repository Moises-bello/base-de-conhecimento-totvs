---
content_hash: b8a66e40d02119526a18468fdc9fa92c4b1451388d228b0ad0e1850d46983c14
fetched_at: '2026-06-29T00:11:51.527513+00:00'
page_id: '848818879'
product: rm
source: tdn-rm
title: Implantação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=848818879
version: 159
---

Este documento visa fornecer um guia passo a passo para o processo de implantação do TOTVS Automação de Testes. 

# Atualização

Caso haja interesse em atualizar o instalador para a versão mais recente do **TOTVS Automação de Testes**, recomenda-se consultar a **documentação de Atualização**, onde estão descritos os procedimentos e orientações necessários para realizar o processo corretamente. Para acessar, **[clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=880071945)**.

solid#21cafc1dashedComponentes do TOTVS Automação de testes

A solução é composta por três elementos essenciais:

#### 1. Host (Website)

O Website é a

interface principal da ferramenta, permitindo que os usuários realizem diversas ações, tais como:

* Criação e gerenciamento de testes;
* Solicitação de execução de atividades e testes;
* Exportação de relatórios;
* Criação de agendamentos de testes;
* Visualização de dashboards com informações sobre execuções realizadas.

#### 2. Agent

O Agent é responsável pela execução dos testes solicitados pelo Website. Suas principais funções incluem:

* Execução de testes no servidor;
* Realização de testes de requisições;
* Comunicação com o RM para a gravação dos passos de aplicações WinForms;
* Envio de informações sobre os testes executados de volta ao Website.

#### 3. Servidor de Banco de Dados (SQL)

O Servidor de Banco de Dados armazena todas as informações essenciais para o funcionamento da ferramenta e do CorporeRM. Ele é responsável por:

* Hospedar o banco de dados da ferramenta e do CorporeRM;
* Armazenar informações sobre testes, execuções e agendamentos;
* Permitir a restauração das bases do CorporeRM quando necessário.

## Fluxo de Interação

1. O Website solicita a execução de testes ao Agent.
2. O Agent processa os testes e executa as requisições necessárias.
3. O Agent envia os resultados das execuções ao Website.
4. O Banco de Dados armazena as informações e permite a restauração das bases do CorporeRM caso necessário.

Esse fluxo garante a automação e o gerenciamento eficiente dos testes dentro da ferramenta.

solid#21cafc1dashedCriação do ambiente

## Ambiente recomendado

Para uso, segue especificações recomendadas das máquinas para hospedar o Host e o Agent da ferramenta.

* **VM Host:** Neste ambiente será hospedado o host (website) do TOTVS Automação de Testes.
  + SO: Windows Server 2016+
  + 2VCPU
  + 4GB RAM
  + 60GB Disco.
* **VM Banco de Dados:** Base de dados do TOTVS Automação de Testes e as bases de testes do cliente
  + SQL Server 2019+
  + 2VCPU
  + 4GB RAM
  + 60GB de disco (Windows + Base TOTVS Automação de Testes) + disco suficiente para 2x tamanho da base de testes do cliente.
* **VM de Agent**: Nesse ambiente será hospedado o Agent do TOTVS Automação de Testes e o ambiente do RM.
  + 2VCPU
  + 4GB de ram
  + 60GB de disco.
  + Ambiente do RM

É obrigatório que o RM esteja instalado na mesma máquina do Agent. Isso é necessário para a execução de atividades que interagem com a interface (WinForms) e para a execução de comandos como "Inicia Host" e "Inicia RM". Recomenda-se que esta máquina seja dedicada e possua um ambiente limpo e controlado para evitar interferências visuais ou de sistema durante os testes de tela.

## Ambientes alternativos

É possível também criar topologias alternativas considerando a capacidade de criação de VMs do cliente.

Um exemplo seria utilizar apenas uma VM, conforme exemplo a seguir:

* **VM com ambiente completo:** Neste ambiente será hospedado todos os componentes referentes ao TOTVS Automação de Testes.
  + SO: Windows Server 2016+
  + SQL Server 2019+
  + Ambiente do RM
  + 4VCPU
  + 12GB RAM
  + 120GB disco (Windows + Base TOTVS Automação de Testes) + disco suficiente para 2x tamanho da base de testes do cliente
solid#21cafc1dashedLiberações de rede

Para a utilização do TOTVS Automação de Testes é necessário fazer algumas liberações de rede entre os ambientes e localmente no firewall dos servidores.

## Entre os ambientes

* Verificar a conectividade entre as redes da máquina Host e da máquina Agent
  + Descubra qual o IPV4 dos servidores

    - Abra o prompt de comando (cmd) em ambas as máquinas.
    - Digite o comando **'ipconfig'** e pressione Enter.
    - Verifique no seu adaptador de internet o seu endereço de IPV4

Para determinar se dois endereços IP estão na mesma rede, utiliza-se a máscara de sub-rede. Esta máscara é utilizada para distinguir a parte de rede da parte de host em um endereço IP.

Em resumo, se todos os números antes do último ponto resultantes do comando 'ipconfig' forem idênticos, isso indica que as máquinas estão conectadas na mesma rede. Por exemplo:

**10.171.32**.200 e **10.171.32**.201

**10.31.7.**13 e **10.31.7.**14

**192.168.0.**1 e **192.168.0.**2

Caso não estejam na mesma rede ou ainda não seja possível fazer a conexão, é necessário garantir as seguintes liberações de rede:

| Origem | Destino | Protocolo | Porta | Motivo |
| --- | --- | --- | --- | --- |
| Host | Agent | TCP | 5010, 5011, 5012, 445 | Compartilhamento de arquivo e Conexão do Host com Agent. |
| Agent | Host | TCP | 6060, 445 | Compartilhamento de arquivo e Conexão do Agent com Host. |
| Agent | Servidor de Banco SQL | TCP | 1433 | Conexão do Agent com o Banco. |
| Agent | Servidor de Banco SQL | UDP | 1434 | Conexão do Agent com o Banco. |
| Máquina local do usuário (Opcional caso tenha) | Host | TCP | 6060 | Conexão do computador local com o Host do TOTVS Automação de Testes. |
| Máquina local do usuário (Opcional caso tenha) | Host, Agent | TCP | 3389 | Conexão remota com a VM do Host e do Agent. |

Para testar a conexão entre duas máquinas (por exemplo, entre a máquina do **Agent** e o servidor de banco de dados), abra o **PowerShell** como Administrador e execute o seguinte comando:

 -Port ]]>

## Firewall

Localmente nos servidores do Agent e do Host é necessário fazer as mesmas liberações de rede para a utilização do TOTVS Automação de Testes. Para isso, dê acesso ao firewall às portas listadas na tabela acima, tanto para entrada, quanto para a saída das portas.

## Liberações de rede em topologias alternativas

Caso utilize ambientes alternativos, é necessário adaptar as liberações de rede conforme a topologia configurada. 

solid#21cafc1dashedConfigurações de usuários

Para a utilização do TOTVS Automação de Testes é necessário configurar ou utilizar usuários que tenham permissões específicas conforme descrição a seguir.

SMTP

O TOTVS Automação de Testes necessita de um usuário com permissões para envio de email.

Ele será utilizado para envio de e-mails de agendamentos e geração de relatórios.

Para isso, é necessário preparar algumas configurações de SMTP para a implantação, são elas:

* Endereço de email do remetente;
* Porta do servidor;
* Host do servidor;
* Nome de usuário;
* Senha do usuário;
* Domínio;
* Se deve habilitar o SSL;

A sugestão é criar um usuário específico apenas com as permissões necessárias

Banco de dados

O TOTVS Automação de Testes necessita de um usuário com permissões para criar, remover e acessar as bases de dados da ferramenta e CorporeRM.

Ele será utilizado durante as restaurações de base da automação e também para gravação de dados internos do serviço.

A sugestão é criar um usuário específico apenas com as permissões necessárias

solid#21cafc1dashedPré-condições para implantação

**A partir desse passo, é necessário que esses itens estejam configurados e disponíveis.**

* Servidores do Agent, Host e banco disponíveis para a implantação;
* Liberações de rede entre os servidores do Agent, Host e banco já consolidadas;
* Dados SMTP para envio de e-mails;
* Dados de um usuário de banco com permissão de criar, remover e acessar as bases de dados da ferramenta e CorporeRM
* Ambiente RM instalado na VM onde será instalado o Agent
* Base CorporeRM que será utilizada na automação já restaurada no ambiente
solid#21cafc1dashedCadastro no Fluig Identity

É necessário após a criação do ambiente de automação a solicitação para a TOTVS para que o cadastro do Fluig Identity seja realizado.

Deve ser enviado as seguintes informações:

* Nome completo do Host do TOTVS Automação de Testes acessível pela máquina no Agent, exemplo: meu-servidor.br01.local;
* Email e nome dos usuários que irão utilizar a ferramenta;

Após o cadastro será enviado a Url de redirecionamento do Fluig Identity e o Secret JWT que serão utilizados posteriormente para a implantação.

solid#21cafc1dashedInstalaçõesInstalaçõesConfigurações antes da instalaçãoInstalação do IIS

## Instalando o IIS

1) Abra o Dashboard do Server Manager e clique em **“Add roles and features”**

2) Next -> Next -> Next.

3) Em server Roles selecione a **“Web Server (IIS)” → Add Features → Next  
Obs:** Caso o Web Server ISS já vier previamente marcado, pule para o passo 5 e depois retorne para a 4.

4) Em Features, selecione a opção **"IIS Hostable Web Core" → Next → Next.**

**Obs:** Caso tenha vindo do passo 5, pule para o passo 6.

5) Em Role Services, selecione a opção **“Web Server (IIS) → Common HTTP Features → HTTP Redirection”, "Security → Basic Authentication e Windows Authentication"** e "**Managment Tools** → **IIS 6 Management Compatibility (Marcar todos os itens)**"**.**

6) Next -> Install.

Instalação do URL Rewrite

## Instalando o URL Rewrite

1) Acesse o link <https://www.iis.net/downloads/microsoft/url-rewrite> e selecione a opção ***English: x64 installer***

2) Após o download execute o instalador como administrador e clique na opção ***Next***

3) Selecione a opção ***Install***

*4)* Aguarde e selecione a opção ***Finish*** para finalizar a instalação

Instalação manual dos Frameworks .NET

## Componentes .NET necessários

Para o correto funcionamento da ferramenta, é necessário que os seguintes componentes do **Microsoft .NET** estejam instalados no servidor:

* **.NET Core 2.2 – Hosting Bundle**  
  Necessário para execução de aplicações web hospedadas no servidor (inclui suporte ao IIS e runtime do .NET).   
  Download:  
  [Baixar .NET Core 2.2 Hosting Bundle](https://builds.dotnet.microsoft.com/dotnet/aspnetcore/Runtime/2.2.8/dotnet-hosting-2.2.8-win.exe)
* **.NET 8 – Runtime**  
  Necessário para execução das aplicações que utilizam essa versão da plataforma .NET.   
  Download:  
  [Baixar .NET 8 Runtime](https://builds.dotnet.microsoft.com/dotnet/aspnetcore/Runtime/8.0.27/aspnetcore-runtime-8.0.27-win-x64.exe)
Instalador

Para instalação, deverá ser executado o instalador específico TOTVSAutomacao.exe, que fará algumas validações e automações, simplificando o processo de implantação.

O instalador está disponível no link <https://testflowstorage.blob.core.windows.net/latest/TOTVSAutomacao.exe>.

Ao iniciar, será validada a existência do IIS e seus componentes, bem como a do URLRewrite na máquina.

Caso passe pela validação, irá realizar a instalação de:

* Arquivos do TOTVSAutomação
* Base de dados inicial
* Criação do Site no IIS

## Base de dados

Após o download, é necessário restaurar no servidor de banco de dados o arquivo **.bak** disponibilizado após a instalação do **TOTVS Automação**, pois a ferramenta utiliza essa base para armazenar suas próprias informações.

O arquivo **.bak** da base pode ser localizado no seguinte caminho: **C:\TOTVS\TOTVSAutomacao\Base**.

Deve existir no ambiente a liberação de rede para a comunicação do Host com o servidor de banco.

O primeiro usuário a realizar login no **TOTVS Automação de Testes** em uma base será automaticamente cadastrado como 'Administrador' no grupo geral 'Todos'. Esse usuário poderá cadastrar, gerenciar e conceder permissões aos próximos usuários do sistema.

## Passo a passo de instalação - Instalador TOTVS Automação de Testes

Com os pré-requisitos técnicos finalizados (IIS, URL Rewrite e Frameworks .NET), você pode prosseguir com a instalação do sistema. O instalador oferece dois métodos de execução: via **Interface Gráfica** ou **Modo Silencioso**.

#### Instalação via Interface Gráfica

Ao executar o `TOTVSAutomacao.exe`, você encontrará a tela de seleção de componentes. Esta etapa define quais partes da solução serão implantadas no servidor.

* **Instalação Completa (Padrão):** Realiza a implantação de todos os arquivos do Host (Website) e prepara a base de dados inicial. É a opção indicada para novas instalações.
* **Instalação Personalizada / Customizada:** Oferece controle total sobre o que será instalado. Você pode optar por instalar apenas os arquivos da aplicação (TOTVS Automação) ou apenas os componentes de banco de dados.
* **Instalação Compacta:** Versão simplificada contendo apenas os binários essenciais para execução rápida do Host.

#### Instalação via Linha de Comando (Modo Silencioso)

Para implantações automatizadas ou em larga escala, o instalador suporta a execução silenciosa. Esse método ignora as telas de interface e aplica as configurações padrão de forma automática.

* Para executar, abra o Prompt de Comando (CMD) como Administrador e utilize:

  > `TOTVSAutomacao.exe /s`

**Aplicação Principal:**  
Refere-se aos arquivos binários, front-end e serviços do Website (Host). Esta opção deve estar sempre marcada para novas instalações ou atualizações de versão.

**Base Vazia**

**Quando DESMARCAR (Recomendado):**  
Se você já restaurou manualmente o arquivo **.bak** no SQL Server conforme orientado no passo anterior, mantenha esta opção desmarcada. Dessa forma, o instalador não realizará nenhuma ação relacionada ao banco de dados.

**Quando MARCAR:**  
Utilize esta opção apenas quando desejar que o instalador **disponibilize/crie o arquivo de backup (.bak)** para que a base de dados possa ser restaurada posteriormente no SQL Server.

Host

Após utilizar o instalador é necessário criar e configurar o arquivo **appsettings.json** do Host.

Criação do arquivo appsettings.json

O Arquivo de configuração deve ser criado e preenchido conforme as informações do ambiente e enviadas durante a implantação.

O formato JSON deve respeitar algumas formatações, restrições e caracteres de escape, para a configuração no formato correto, é importante consultar a documentação oficial através do link <https://www.json.org/json-en.html>.

1) Entre no diretório *C:\inetpub\wwwroot\TotvsAutomacao*e crie um arquivo **appsettings.json** com o conteúdo a seguir:

js

Exemplo do arquivo criado:

Valide se o arquivo criado está com a extensão **.json** e é reconhecido pelo Sistema Operacional como **Arquivo JSON**, como na imagem acima.   
Exemplo de arquivo certo e errado:

**Obs:**Essa validação é necessária pois dependendo da forma que criamos o arquivo, o arquivo pode parecer ser um JSON, mas possui duas extensões que geralmente não é visível facilmente.

2) Preencha cada campo conforme as orientações a seguir:

| Campo | Tipo do campo | O que deve ser informado | Template | Exemplo |
| --- | --- | --- | --- | --- |
| Jwt.Secret | Texto | Segredo informado durante a implantação |  | 83f7df92-9c05-4f17-a848-c12e9c6cfb92 |
| Jwt.RedirectUrl | Texto | Url de retorno do Fluig informada durante a implantação |  | [https://testflow.fluigidentity.com/cloudpass/launchpad/launchApp/2575eb568asudhaushdue/080aadasdfuhfaab6](https://testflow.fluigidentity.com/cloudpass/launchpad/launchApp/2575eb50628a446db83dd1bec4e7ceee/08059b592ab0489c9f4d6f2c29208eb6) |
| ConnectionStrings.default | Texto | A connection string do banco de dados da ferramenta | Data Source={seu-servidor-de-banco};User Id={usuário};Password={senha};Initial Catalog=TotvsAutomacao; | Data Source=TotvsAutomacaoServer;User Id=sa;Password=123456789;Initial Catalog=TotvsAutomacao; |
| smtp.From.Address | Texto | Email do usuário SMTP |  | [totvsautomacao@minhaempresa.com](mailto:totvsautomacao@minhaempresa.com) |
| smtp.Port | Numérico | Porta do servidor SMTP |  | 587 |
| smtp.Host | Texto | Endereço do servidor SMTP |  | [smtp.gmail.com](http://smtp.gmail.com) |
| smtp.Username | Texto | Nome do usuário SMTP |  | totvsautomacao |
| smtp.Password | Texto | Senha do usuário SMTP |  | 123456789 |
| smtp.Domain | Texto | Domínio do servidor SMTP |  | br01 |
| smtp.EnableSsl | Booleano | Habilitar Ssl |  | true |
| Endpoint | Texto | Url do host | [http://{host}:6060](http://localhost:3000/callback-auth) | [http://servidor-totvs-automacao:6060](http://localhost:3000/callback-auth) |

3) Exemplo de um arquivo criado

##### Validação

Após esse passo, reinicie o computador e na sequência, dê um start no IIS. Com isso, já será possível acessar o TOTVS Automação de Testes pela URL configurada.

AgentInstalação do Agent

Proceda da seguinte forma:

* Acesse a URL correspondente ao host do TOTVS Automação de Testes configurado anteriormente em um navegador da web.
* Em seguida, proceda com o download do Agent.

Isso fará com que seja baixado um arquivo .exe. Esse é o instalador do Agent que deverá ser executado.

Prosseguindo com a instalação do TotvsAutomacaoAgent

Após baixar o arquivo .exe, basta executá-lo e seguir o guia a seguir.

Caso apareça esse alerta do windows, clique em **"Mais informações"**:

E depois em **"Executar assim mesmo"**:

Uma vez que esse arquivo foi executado, uma janela com o instalador irá aparecer:

Na próxima etapa, será necessário selecionar um caminho preferido para os arquivos. É recomendável utilizar a configuração padrão "c:\TOTVS\Agent".

É necessário possuir ao menos 189,9MB disponíveis no disco.

Ao prosseguir, deverá inserir a URL do servidor onde está o TOTVS Automação:

Essa configuração foi feita nos passos anteriores da instalação do TOTVS Automação, o Agent deverá apenas apontar para aquela mesma URL.

**Exemplo: "[http://NomedoHost.local:6060](http://NomedoHost.local:6060/)"**

Com tudo isso feito, agora basta confirmar as informações, clicar no botão **"Instalar"**e aguardar até a instalação ser finalizada.

Ao fim da instalação, basta clicar em **"Concluir"**e o Agent do TOTVS Automação de Testes será executado.

Para garantir que tudo funcionou com sucesso, acesse o cadastro de servidores, cadastre o HostName da máquina onde o Agent do TOTVS Automação está sendo executado e valide se está online.

## Utilização de um usuário de serviço

A recomendação é que seja utilizado um usuário de serviço para iniciar o Agent. Assim, é possível garantir que ele nunca estará offline, mesmo quando um usuário seja desconectado do servidor.

Validações

## Validações após instalações

Após a instalação e configuração dos ambientes é interessante validar se os cadastros e execuções estão funcionando conforme esperado.

Autenticação com o Fluig IdentityConexão com o Agent

Vá no cadastro de Servidores e clique no botão da coluna "Online" do seu servidor.

Cadastro de gruposExecução de projetosExecução de agendamentosValidação de erros

Caso ocorra o **Erro 500 (Internal Server Error)**, significa que o servidor encontrou um problema inesperado ao processar a requisição.

Para investigar a causa do problema, execute o comando abaixo no **Prompt de Comando (CMD)**, utilizando o caminho **`C:\inetpub\wwwroot\TotvsAutomacao`**  
Esse comando exibirá informações que podem ajudar a identificar os possíveis caminhos para a resolução do erro.

## Uso do sistema somente após a vínculo do usuário em um grupo

Após o usuário ser adicionado em um grupo, será possível para o mesmo criar, editar, visualizar e executar atividades no TOTVS Automação de Testes.
