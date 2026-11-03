---
content_hash: afc554d528e328e35bcafbcce3db97f8428c620f8994df9143adbeddcc6c2eab
fetched_at: '2026-06-28T21:35:23.675734+00:00'
page_id: '257623499'
product: fluig
source: tdn-fluig
title: Configuração do banco de dados SQL Server
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=257623499
version: 46
---

Fique atento!

Esta página é válida para atualizações **1.6** e **superiores** do TOTVS Fluig.

Caso possua uma atualização anterior acesse:

2.\*ndice

# Versões homologadas do SQL Server

---

Para verificar as versões homologadas do Microsoft SQL Server, acesse a [Matriz de Portabilidade](http://tdn.totvs.com/display/fluig/Matriz+de+Portabilidade).

# Criação do banco de dados com codificação Latin1\_General\_CI\_AS

---

Importante!

Por questões de segurança, é altamente recomendável efetuar a encriptação da senha conforme o procedimento descrito em [encriptação de senha do banco de dados](http://tdn.totvs.com/x/Oh4WGw).

A plataforma necessita de uma base de dados com *charset* **Latin1\_General\_CI\_AS**. Só serão aceitos caracteres com codificação Latin1\_General\_CI\_AS, pois caracteres não pertencentes a esta codificação não são homologados para a plataforma, estando sujeito a inconsistências de banco de dados. Na versão 2012 e inferiores do SQL server, a codificação é regionalizada, podendo causar inconsistências quando utilizado, por exemplo, a UTF8.

Para criar o banco com esta característica, autentique-se no SQL Server com o usuário que será utilizado pela plataforma e execute o seguinte comando SQL, onde "nome\_do\_banco" é o nome do banco a ser criado.

sql

Outra alternativa para a criação do banco de dados é utilizar o **Microsoft SQL Server Management Studio,**seguindo o seguintes passos:

0.5falsecreate-db-studiofadetrue1Passo 1

* Conecte na instância do SQL Server por meio do **Microsoft SQL Server Management Studio.**
* Clique com o botão direito do *mouse* na pasta **Bancos de Dados** e selecione a opção **Novo Banco de Dados...**

2Passo 2

* Ao abrir a tela do assistente, selecione a opção **Geral** em **Selecionar uma página.** Em seguida, informe o nome desejado para o banco de dados no campo **Nome do banco de dados** e selecione o usuário que será utilizado pela plataforma no campo **Proprietário.**

3Passo 3

* Seguindo, selecione a opção **Opções** em **Selecionar uma página.** Em seguida, selecione o valor **Latin1\_General\_CI\_AS** no campo **Agrupamento**.

4Passo 4

* Para finalizar, encontre a opção **O Instantâneo de Leitura Confirmada Está Ativo** (*Is Read Committed Snapshot On* em inglês) e altere seu valor para ***True*.** Clique no botão **OK** para finalizar a criação do banco de dados.

# Configuração do banco

---

Após a criação do banco de dados é necessário realizar as verificações a seguir.

## Proprietário do banco

---

O usuário utilizado pela plataforma para conexão com o banco de dados deve ser **proprietário (db\_owner)** do banco utilizado pela plataforma. Para verificar qual usuário é o proprietário do banco, execute o seguinte comando SQL:

sql

Onde **nome\_do\_banco** é o nome do banco para consulta do proprietário.

Caso o proprietário do banco não seja o usuário utilizado pela plataforma para conexão com o banco de dados, execute o seguinte comando T-SQL para definir este usuário como **proprietário (db\_owner):**

sql

Onde **nome\_do\_banco** é o nome do banco e **nome\_usuario**o usuário que se tornará proprietário do banco de dados.

## Parâmetros de conexão

---

Veja a seguir alguns parâmetros que podem ser utilizados na URL de conexão.

### Parâmetro para evitar lentidão

---

Para evitar lentidão em algumas consultas da plataforma, é necessário adicionar um parâmetro de conexão no arquivo de configurações.

Para isso:

**01.** Acesse o arquivo de configurações da plataforma de acordo com a atualização utilizada no seu ambiente:

* **a partir da atualização 2.0:** acesse o arquivo **standalone.xml** ([diretório\_instalação]/appserver/standalone/configuration/standalone.xml);

* **da atualização 1.6 até a 1.8.2**: acesse o arquivo **domain.xml** ([diretório\_instalação]/appserver/domain/configuration/domain.xml).

**02.** Localize as *tags* **<connection-url>**.

**03.** Adicione o parâmetro **;sendStringParametersAsUnicode=false** em todas as *tags* **<connection-url>**.

Atenção!

Nas atualizações mais recentes, esse parâmetro já é adicionado automaticamente na URL de conexão ao instalar a plataforma com o SQL Server. Por isso, verifique se o parâmetro já está configurado antes de adicioná-lo.

### Conexão criptografada por padrão

---

Por questões de segurança, a partir da atualização **Voyager (2.0)**, a comunicação com o banco de dados SQL Server passa a ser criptografada por padrão.

Mas, não se preocupe, se a configuração de criptografia não foi alterada em nenhum momento, o parâmetro ***trustServerCertificate*** será adicionado automaticamente com o valor ***true*** na URL de conexão ao atualizar a plataforma.

Caso você tenha configurado manualmente o parâmetro ***encrypt*** ou o ***trustServerCertificate***, a atualização não modificará a URL de conexão e a configuração já existente será mantida.

## Alteração do nível de isolamento

---

Para verificar se a opção de isolamento READ\_COMMITTED\_SNAPSHOT está habilitado para o banco de dados, execute o seguinte comando SQL:

sql

Onde **nome\_do\_banco** é o nome do banco para consulta do proprietário.

Caso o retorno da consulta anterior seja o valor **0**, é necessário executar o seguinte comando SQL:

sql

Onde **nome\_do\_banco** é o nome do banco de dados a ser utilizado para a plataforma.

Importante!

Esta operação de alteração do nível de isolamento padrão do SQL Server é realizada automaticamente pela plataforma. Porém, é importante atentar-se para o seguinte fator: na criação do banco de dados, é executada uma ação de alteração na base. É normal visualizar no *log* algumas mensagens de erro, tratando-se de um processo padrão para atualização. A situação será normalizada após o término da operação.

Assim que o servidor Fluig estiver no ar, recomendamos que ele seja reinicializado.

## Configuração da porta TCP 1433

---

Para liberação do protocolo TCP/IP e conexão do banco com o Fluig através da porta 1433, basta seguir os seguintes passos:

* Executar o **SQL Server Configuration Manager**, no caminho SQL Server Network Configuration > Protocols for <instância> > TCP/IP.
* Certificar-se de que o protocolo TCP/IP esteja ativo e habilitado.  
  Na sessão **IPAll** verifique se não há nenhuma porta dinâmica configurada diferente da 1433 e configure apenas a porta estática padrão **1433 em TCP Port**.
* **TCP Dynamic Ports precisa estar vazio**, caso esteja 0, será criada uma nova porta dinâmica na próxima inicialização do serviço.
* Após salvar as configurações, será necessário reiniciar o serviço do banco de dados para aplicar as alterações.
* Para validar se a porta correta está sendo escutada no servidor, pode-se executar um **netstat -an** no cmd.

Configuração TCP 1433
