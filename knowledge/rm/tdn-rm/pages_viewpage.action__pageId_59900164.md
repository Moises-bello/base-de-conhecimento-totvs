---
content_hash: 89948b864d857cb342ea2da29bce2614ef2c3cf6d139bda335cf697cc07547ea
fetched_at: '2026-06-29T00:10:57.260485+00:00'
page_id: '59900164'
product: rm
source: tdn-rm
title: Instalação do Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=59900164
version: 8
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.50 |
| **Processo** | **:** | Gestão de conteúdos |
| **Subprocesso** | **:** | Instalação do Portal WEB |
| **Data da publicação** | **:** | 18/07/2013 |

### 1. Requisitos Necessários para instalação e utilização do Portal RM

- Framework 4.0

- IIS (Internet Information Services)

### 2. Instalar a Framework 4.0

#### 2.1. O que é .NET Framework ou simplesmente .NET?

.NET é uma "plataforma de software". É um ambiente independente de linguagem para criação de programas que possam inter-operar facilmente e de forma segura com diversos sistemas operacionais. Em vez de serem desenvolvidos para uma combinação hardware/software particular, os programas serão desenvolvidos para o ".NET", e funcionarão em qualquer lugar onde a .NET Framework estiver implementada.

A principal idéia da .NET Framework é usar uma forma única das aplicações conversarem com o sistema operacional. Este é o modelo mais flexível e produtivo entre todos os disponíveis..

Do ponto de vista dos “programadores”, a .NET Framework é evolução do sistema operacional Windows. É através dela que são invocadas todas as funções necessárias ao funcionamento dos programas que rodam em ambiente Windows.

#### 2.2. Por que devemos instalar o .NET Framework?

A .NET Framework é uma biblioteca de classes que reúne todas as funções normalmente associadas ao sistema operacional. O .NET Framework permite a criação de código gerenciado que não pode danificar o sistema de execução.

A TOTVS, alinhada com as tendências do mercado e visando promover a conectividade e conseqüentemente o aumento de produtividade de nossos clientes, escolheu como plataforma de desenvolvimento para o CORPORE RM a .NET Framework. A partir deste novo conceito, a RM estará evoluindo gradualmente suas soluções, e substituindo as suas aplicações cliente/servidor por aplicações multi-camadas nesta nova plataforma.

Sendo assim, a partir da versão 11.20.1 do CORPORE RM será requisito mínimo de software ter a versão 4.0 da .NET Framework instalada em todas as máquinas que irão utilizar as soluções RM. Veja a conclusão da instalação.

### 3. Instalação do IIS (Internet Information Services)

Para instalação do Portal, a máquina já deve estar com o IIS instalado.

Recomenda-se a instalação completa do IIS para que seja possível a instalação do Portal.

Erros na instalação do portal estão diretamente relacionados a má instalação do IIS.

### 4. Instalação da Biblioteca

Para utilização do Portal RM, na arquitetura cliente-servidor, é necessário estar instalado a Biblioteca RM na própria máquina onde o portal será instalado.

### 5. Instalação do Portal RM (Gestão de Conteúdos / .exe)

Utilize o instalador do Portal mais atual compatível com a Biblioteca RM.

Basicamente a instalação do Portal Web é o mesmo processo do Gestão de Conteúdos, avançar cada etapa até chegar à opção de “Instalar”.

Neste momento o instalador irá configurar a Framework instalada anteriormente e a página no Servidor Web IIS que já deverá estar instalada no servidor.

Obs: O servidor Web IIS é um produto da Microsoft

Preste atenção na janela abaixo, pois esta é fundamental para o correto funcionamento do portal.

Essa tela irá aparecer somente se na pasta RM.NET não houver o arquivo Alias.dat.

Após instalação do Portal será criado uma nova sub-pasta em CorporeRM chamada Corpore.Net. Esta pasta contém as DLL’s para o funcionamento do Portal.

#### 5.1. Configuração do Alias.dat

...\CorporeRM\RM.Net\RM.AliasManager.exe

Alias: Apelido do seu alias.

Tipo de banco: Verificar qual banco de dados utilizando em sua empresa

Servidor de banco: Nome do servidor de banco de dados

Base de Dados: Nome do seu banco de dados.

Observação: Para Oracle, será necessário informar apenas a instancia.

Veja a estrutura do arquivo Alias.dat

Exemplo para Banco de dados SQL:

<?xml version="1.0" standalone="yes"?>

<RMSAliasData xmlns="http://tempuri.org/RMSAliasData.xsd">

<DbConfig>

<Alias>CorporeRM</Alias>

<DbType>SqlServer</DbType>

<DbProvider>SqlClient</DbProvider>

<DbServer>rm0004066</DbServer>

<DbName>exemplo1120</DbName>

<UserName>SYSDBA</UserName>

<Password>masterkey</Password>

<RunCustom>false</RunCustom>

<RunService>false</RunService>

</DbConfig>

</RMSAliasData>

Exemplo para Banco de dados Oracle:

<DbConfig>

<Alias>Corporerm\_Oracle</Alias>

<DbType>Oracle</DbType>

<DbProvider>OracleClient</DbProvider>

<DbServer>baseoracle</DbServer>

<DbName />

<UserName>SYSDBA</UserName>

<Password>masterkey</Password>

<RunService>false</RunService>

<JobServerEnabled>false</JobServerEnabled>

<JobServerMaxThreads>3</JobServerMaxThreads>

<JobServerLocalOnly>true</JobServerLocalOnly>

<JobServerPollingInterval>10</JobServerPollingInterval>

<ChartAlertEnabled>false</ChartAlertEnabled>

<ChartAlertPollingInterval>20</ChartAlertPollingInterval>

<ChartHistoryEnabled>false</ChartHistoryEnabled>

<ChartHistoryPollingInterval>20</ChartHistoryPollingInterval>

<RSSReaderMailEnabled>false</RSSReaderMailEnabled>

<RSSReaderMailPollingInterval>10</RSSReaderMailPollingInterval>

</DbConfig>

</RMSAliasData>

### 6. Configuração do Portal RM no IIS

#### 6.1. Windows 2003

Para configuração do Portal no IIS, acesse o caminho Painel de Controle – Ferramentas Administrativas - o IIS (Internet Information Services)

Em uma instalação bem sucedida do Portal, o diretório virtual “Corpore.net” já terá sido criado dentro do menu *Sites da Web Padrão*.

Clique com o botão direito em cima do Diretório virtual e abra a “Propriedade”.

A tela de configuração do Portal será aberta na aba Diretório Virtual, com algumas opções já definidas.

As opções que devem ser marcadas são:

- Acesso ao código fonte do script

- Ler

- Pesquisa no diretório

- Criar log de visitantes

- Indexar este recurso

Observe se o campo *Nome do aplicativo* está preenchido, caso contrário, clique em “Remover” e logo em seguida “Criar”.

Na aba Documentos, deverá ser ativado o documento padrão “Login.aspx” para que o IIS busque esse arquivo como default.

Na aba ASP.NET, selecione a versão 4.0 do framework para utilização do o Portal.

OBS: Possíveis problemas podem ocorrer se alguma versão inferiores a 4.0 esteja instalado. Nesse caso será necessário ajustar a versão nesta janela.

Caso o cliente deseje usar o RSS, para recebimento dos feed, a opção de autenticação deverá ser desmarcada para não usar a “Autenticação do Windows Integrada”

Após essas configurações, o portal deverá estar pronto para utilização.

Acesse o navegador, e digite o caminho [HTTP://localhost/Corpore.net](http://localhost/Corpore.net) ou clique com o botão direito do mouse no diretório virtual Corpore.net e selecione a opção “Procurar”.

Com isso a página inicial do portal deverá ser aberta.

Nas configurações do Windows 2003, é necessário conceder permissão para os objetos mostrados abaixo:

**OBSERVAÇÕES:**

Para que a instalação funcionem corretamente, como pré-requisito do instalador do Portal, além do IIS instalado, é necessário que a compatibilidade com IIS 6 esteja instalada. E o IIS 5 não contempla essas alterações, logo, sistemas operacionais anteriores ao Windows XP, não funcionarão, no mínimo Windows 2003 Server e Windows Vista.

Essa opção de compatibilidade, só aparece em Windows com IIS 7 (Windows 2008 Server e Windows Vista em diante).

Esse recurso é instalado juntamente do IIS, mas se o mesmo já estiver instalado, é possível adicionar apenas esse recurso.

Tirei alguns prints das opções nos 3 windows disponíveis.

Todos ambientes instalam da mesma forma, através do Painel de controle à “Adicionar ou remover programas“ / “Programas e Recursos” à “Ativar ou desativar recursos do Windows”

Windows Vista:

Windows 2008 Server:

Windows 7:

#### 6.2. Windows Vista

As configurações para o Windows Vista será diferente na opção de criação do diretório virtual.

No Windows Vista o portal deverá ser criado um Aplicativo.

As configurações para utilização do RSS – feed devem ser conforme tela abaixo.

**ATENÇÃO:**

**Analisar o arquivo de portabilidade, para verificar as recomendações de servidores para o portal Web.**

**O documento de portabilidade é disponibilizado com a instalação do conversor (...\CorporeRM\Scripts\Documentos\** **Portabilidade e Arquitetura RM)**

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
