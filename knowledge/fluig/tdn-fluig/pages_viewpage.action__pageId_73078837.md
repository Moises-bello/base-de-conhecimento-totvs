---
content_hash: 21413ffff9dabee2c0e3090864e4eb4a3dbaf0bbdaa9899ab09c22fd318bea65
fetched_at: '2026-06-28T21:35:28.989442+00:00'
page_id: '73078837'
product: fluig
source: tdn-fluig
title: ARQ - Como configurar o banco de dados SQL Server na release 1.5.13 ou anterior?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=73078837
version: 55
---

Atenção

Esta página foi revisada para considerar as configurações da atualização 1.5.13 ou anteriores.

Acesse a página original a partir da atualização 1.6: .

# Índice

4true.\*ndicenone

# Versões homologadas do SQL Server

Para verificar as versões homologadas do Microsoft SQL Server acesse a [Matriz de Portabilidade](http://tdn.totvs.com/display/fluig/Matriz+de+Portabilidade)

# Criação do banco de dados

O TOTVS Fluig Plataforma necessita de uma base de dados com codificação **Latin1\_General\_CI\_AS***,* para criar o banco com esta característica, autentique-se no SQL Server com o usuário que será utilizado pela plataforma e execute o seguinte comando SQL:

sql

Onde **nome\_do\_banco** é o nome do banco a ser criado.

Outra alternativa para a criação do banco de dados é utilizar o **Microsoft SQL Server Management Studio,**seguindo o seguintes passos:

0.5falsecreate-db-studiofadetrue11º Passo

Conecte na instância do SQL Server através **Microsoft SQL Server Management Studio,** e então clique com o botão direito no mouse na pasta Bancos de Dados e selecione a opção **Novo Banco de Dados...**

22º Passo

Ao abrir a tela do assistente, selecione a opção **Geral** em **Selecionar uma página.** Em seguida, informe o nome desejado para o banco de dados no campo **Nome do banco de dados** e selecione o usuário que será utilizado pela plataforma no campo **Proprietário.**

33º Passo

Seguindo, selecione a opção **Opções** em **Selecionar uma página.** Em seguida, selecione o valor **Latin1\_General\_CI\_AS** no campo **Agrupamento**.

44º Passo

Para finalizar, encontra o opção **O Instantâneo de Leitura Confirmada Está Ativo (Is Read Committed Snapsho On** em inglês**)** e altere seu valor para **True.** Clique no botão **OK** para finalizar e criar o banco de dados.

# Configuração do banco

Após a criação do banco de dados é necessário realizar as seguintes verificações:

### Proprietário do Banco

O usuário utilizado pela plataforma para conexão com o banco de dados deve ser **proprietário (db\_owner)** do banco utilizado. Para verificar qual usuário é o proprietário do banco execute o seguinte comando SQL:

sql

Onde **nome\_do\_banco** é o nome do banco para consulta do proprietário.

Caso o proprietário do banco não seja o usuário utilizado pela plataforma Fluig para conexão com o banco de dados execute o seguinte comando T-SQL para definir este usuário como **proprietário (db\_owner):**

sql

Onde **nome\_do\_banco** é o nome do banco e **nome\_usuario**o usuário que se tornará proprietário do banco de dados.

### Alteração do nível de Isolamento

Para verificar se a opção de isolamento READ\_COMMITTED\_SNAPSHOT está habilitado para o banco de dados execute o seguinte comando SQL:

sql

Onde **nome\_do\_banco** é o nome do banco para consulta do proprietário.

Caso o retorno da consulta anterior seja o valor **0** é necessário executar o seguinte comando SQL:

sql

Onde **nome\_do\_banco** é o nome do banco de dados a ser utilizado para a plataforma.

Esta operação de alteração do nível de isolamento padrão do SQL Server é realizada automaticamente pela plataforma. Porém é importante atentar para o seguinte fator:

Na criação do banco de dados, é executada uma ação de alteração na base. É normal visualizar no log algumas mensagens de erro, tratando-se de um processo padrão para atualização. A situação será normalizada após o término da operação.

Assim que o servidor estiver no ar recomendamos a reinicialização do mesmo.

### SQL Server 2014

Como você pode verificar na , a plataforma está homologada para o SQL Server 2014 a partir da **atualização 1.6.5 - Liquid**.

Para as  atualizações 1.5.13 ou inferiores, caso seja utilizada a versão 2014 ou superior do SQL Server, é necessário alterar o arquivo **[Instalação fluig]\jboss\bin\standalone.conf.bat**(standalone.conf em ambientes Linux) e incluir a seguinte linha:

0.5falseLinhafadetrue1WindowspowershellEclipsestandalone.conf.bat2LinuxpowershellEclipsestandalone.conf

Além disso, é importante setar o nível de compatibilidade do banco de dados para SQL Server 2012 executando o comando abaixo:

sql

Este procedimento pode ser realizado através do **Microsoft SQL Server Management Studio.**
