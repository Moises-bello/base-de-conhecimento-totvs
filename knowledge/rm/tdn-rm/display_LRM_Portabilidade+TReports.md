---
content_hash: 1056db59c8cd5c5bef52a45e469e23f6ee8c2b7e8e66f20f3291bead7217e8f3
fetched_at: '2026-06-29T00:09:13.577758+00:00'
page_id: '421371925'
product: rm
source: tdn-rm
title: Portabilidade TReports
type: documentation
url: https://tdn.totvs.com/display/LRM/Portabilidade+TReports
version: 90
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O documento de Portabilidade TReports possui orientações de configurações do ambiente que devem ser utilizadas em sua empresa, buscando o melhor desempenho e usabilidade do sistema.

       As informações contidas neste documento têm como objetivo apresentar, principalmente, quais os sistemas operacionais, banco de dados e navegadores de internet que devem ser utilizados para correto funcionamento do TReports.

       O dimensionamento de hardware descrito neste documento é apenas um informativo para uma empresa de médio porte. Maiores informações sobre qual configuração de hardware é mais adequada à sua empresa devem ser verificadas junto ao Executivo da Conta.

# Requisitos de hardware para instalação do TReports

---

       Tendo em vista que o TReports é uma solução Cross e que trabalha com extração de dados em fontes de dados externa, não temos como medir um sizing.

       A ferramenta permite a criação de relatórios pelo próprio usuário final, sendo assim não temos como saber:  
       - A quantidade de relatórios criados;  
       - O volume de dados gerados por estes relatórios;  
       - As querys escritas em cada relatório;  
       - Os componentes em que o relatório foi criado (pode ser feito o uso de gráficos, imagens, textos rico, pivot tables e etc);  
  
       Desta forma, informamos os requisitos mínimos necessários, para que a solução possa ser utilizada:

* Memória: 4 GB
* Processador: 2 vcpus
* Disco: 40 GB

# Banco de Dados:

---

       Banco de Dados para hospedar o TReports:

false

SQL Server 2014 ou Oracle 11g.

false1SQL Server

Nas versões 12.1.23, 24 e 25 temos somente o collation **Latin1\_General\_CP1\_CI\_AI** homologado. Em versões superiores, temos os collations **Latin1\_General\_CP1\_CI\_AI** e **Latin1\_General\_BIN**.

Caso opte por criar um usuário específico para uso do TReports, segue exemplo de script utilizado para criação do usuário e concessão de privilégios:

-- Criaçao do usuário  
CREATE LOGIN [user] WITH PASSWORD=N'password'  
GO  
  
-- Nível de Privilégio Mínimo  
ALTER SERVER ROLE [user] ADD MEMBER [user]  
GO

* ***user:***nome do usuário que será criado
* ***password:***senha do usuário que será criado

É recomendado que seja criada uma base separada para o uso do TReports.

2Oracle

Conjunto de Caracteres (Character Set) homologado: **WE8ISO8859P1**

O agendamento de relatórios nativo do TReports não está disponível quando este banco de dados for utilizado.

É recomendado que seja criada uma nova instância Oracle para o uso do TReports.

Para a criação de tablespace para o TReports, é recomendado seguir o exemplo abaixo:

CREATE TABLESPACE tablespace DATAFILE 'diretorio\_da\_instancia\_oracle\tablespace\_01.dbf' SIZE 100M AUTOEXTEND ON NEXT 10M;

* ***tablespace:***nome da tablespace a ser criada
* ***datafile:***arquivo físico que será criado para a tablespace. Informe o diretório e o nome do arquivo, exemplo: 'C:\APP\ADMINISTRATOR\ORADATA\TREPORTS\treports\_01.dbf'.
* ***size:*** espaço destinado para a tablespace

Para a criação de um novo usuário, a seguinte instrução é usada:

CREATE USER userid IDENTIFIED BY password  
DEFAULT TABLESPACE tablespace  
TEMPORARY TABLESPACE temp  
QUOTA UNLIMITED ON treports;

* ***userid:*** nome do usuário que será criado
* ***password:*** senha do usuário que será criado
* ***tablespace:*** tablespace padrão onde os objetos do banco de dados serão armazenados, no caso, a tablespace criada no script anterior.
* ***temporary tablespace:*** Tablespace padrão onde são armazenados os objetos temporários, como tabelas temporárias por exemplo.
* ***quota unlimited:*** é a quantidade de espaço alocado para um usuário em uma tablespace, nesse caso, é ilimitada.

Com o usuário criado, a concessão de privilégios é realizada da seguinte forma:

GRANT CREATE SESSION TO userid;

GRANT CREATE TABLE TO userid;  
GRANT CREATE VIEW TO userid;

GRANT CREATE PROCEDURE, CREATE SEQUENCE TO userid;

Para retornar informações para geração de relatórios o TReports tem a capacidade de trabalhar com os seguintes banco de dados relacionais: Oracle, Sql Server, MySql, Postgre, Firebird e DB2.

Apesar de relacionar com os bancos citados acima, o TReports foi homologado somente em SQL e Oracle.

# Navegadores:

---

       Atualmente, os navegadores que suportam o TReports são o Google Chrome, Firefox, Opera e Edge.

Apesar de suportar os navegadores citados acima, o TReports foi homologado somente no Google Chrome.

# Acesso à aplicação:

---

       O servidor em que o TReports e o RAC forem instalados deve estar disponível na rede através do "HostName" ou "DNS".

       A aplicação necessita de um Tenant para seu funcionamento. O Tenant padrão criado pelo instalador é "TReports", caso necessário, se pode alterá-lo no momento da instalação.

       Ao acessar a aplicação via browser, a primeira palavra antes do primeiro ponto encontrado no DNS é interpretada como o Tenant, por exemplo:

       - Supondo que o endereço da aplicação seja <http://treports.MeuDominio.com>,

       O Tenant considerado será: ***TReports***.

       - Supondo que o endereço da aplicação seja <http://MinhaEmpresa.EnderecoPublico.com>,

       O Tenant considerado será: ***MinhaEmpresa***.

    Portanto, o DNS público disponibilizado para os usuários deve contemplar o Tenant antes do endereço do domínio.

O Acesso à ferramenta não deve ser realizado utilizando o IP do servidor.

# Requisitos de software para instalação do TReports

---

Os passos seguintes devem ser executados exatamente na mesma ordem em que se encontram.

falseRequisitosVersõesRequisitosVersõesTReports 12.1.23TReports 12.1.23

1) Sistema Operacional:

false

Windows 7, 10 ou Server 2012 (ou superior)

2) Ativação do IIS na máquina

false11IIS 7.0 e 7.5

Nas versões 7.0 e 7.5 do IIS, além das opções marcadas por default, maque também as opções abaixo quando feita sua ativação.

Obs: Marque as opções .NET Extensibility e ASP.NET mesmo não apresentando o código da versão.

2IIS 8.0

Na versão 8.0 do IIS acesse o *Gerenciador do Servidor | Adicionar Funções e Recursos* e ative as seguintes configurações.

Passo a passo11° Passo22° Passo33° Passofalse

*Deve ser ativado a “Compatibilidade com Gerenciamento do IIS 6” conforme exemplo acima.*

44° Passo

Depois de feita as configurações iniciais, reinicie a máquina e acesse novamente o *Gerenciador do Servidor | Adicionar Funções e Recursos*, para configurarmos as opções .Net adicionais.

3) Instale a última versão do DotNetCore Windows Hosting (2.1.5)

false

Disponível em: [Download Windows Hosting (2.1.5)](https://www.microsoft.com/net/download/thank-you/dotnet-runtime-2.1.5-windows-hosting-bundle-installer)

4) Instale a versão do .Net Framework 4.7.1 ou superior

false

Disponível em: [Download .Net Framework 4.7.1](https://www.microsoft.com/pt-br/download/details.aspx?id=56116)

RequisitosVersõesTReports 12.1.24 ou SuperiorTReports 12.1.24 ou Superior

1) Sistema Operacional:

false

Windows 7, 10 ou Server 2012 (ou superior)

2) Ativação do IIS na máquina

false11IIS 7.0 e 7.5

Nas versões 7.0 e 7.5 do IIS, além das opções marcadas por default, maque também as opções abaixo quando feita sua ativação.

Obs: Marque as opções .NET Extensibility e ASP.NET mesmo não apresentando o código da versão.

2IIS 8.0

Na versão 8.0 do IIS acesse o *Gerenciador do Servidor | Adicionar Funções e Recursos* e ative as seguintes configurações.

Passo a passo11° Passo22° Passo33° Passofalse

*Deve ser ativado a “Compatibilidade com Gerenciamento do IIS 6” conforme exemplo acima.*

44° Passo

Depois de feita as configurações iniciais, reinicie a máquina e acesse novamente o *Gerenciador do Servidor | Adicionar Funções e Recursos*, para configurarmos as opções .Net adicionais.

3) Instale a última versão do DotNetCore Windows Hosting (2.1.5)

false

Disponível em: [Download Windows Hosting (2.1.5)](https://www.microsoft.com/net/download/thank-you/dotnet-runtime-2.1.5-windows-hosting-bundle-installer)

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.23 ou Superiores

false

**Processo:** Portabilidade TReports

falsefalse

**Status:** Finalizado

false

**Data:** 10/10/2018

false

**Autores:**
