---
content_hash: ffb969cf35e6d7f0ec16bcc07bf8931e3c5d5e79b6067f4ea31a956a7e176579
fetched_at: '2026-06-29T00:08:50.163469+00:00'
page_id: '331868191'
product: rm
source: tdn-rm
title: Guia de instalação e configuração - TAF (TOTVS Automação Fiscal) e TSS (TOTVS
  Service SOA)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=331868191
version: 89
---

# Índice

---

.\*ndice:

# Objetivo

---

       O objetivo deste documento é auxiliar os clientes da linha RM na instalação e configuração do TAF - TOTVS Automação Fiscal e TSS - TOTVS Service SOA.

# Introdução

---

             "O TAF - TOTVS Automação Fiscal é a nova plataforma da TOTVS especializada na consolidação dos movimentos fiscais de forma + compacta para atender as obrigações acessórias impostas pelo Governo, e tem como objetivo suportar o processo tributário permeando as Obrigações Principais e Acessórias pelas Demonstrações, Apurações e Cálculos de Tributos.

       Trata-se de uma plataforma segregada com controles próprios e funcionalidades importantes para conferir as informações e agilizar entregas, reduzindo complexidades, removendo e unificando a carga de manutenção das informações, além de possuir um repositório segregado para histórico das movimentações declaradas."

# Pré-requisitos

---

Pré-requisitosBanco de dados

Para que a instalação do **TAF** (TOTVS Automação Fiscal) e do **TSS** seja executada com sucesso, é imprescindível que o ambiente de instalação já possua um **SGBD** instalado, conforme premissas abaixo:

* **Plataformas homologadas**:
  + **Para o TAF temos somente os SGBDs DB2, Informix, MS SQL Server e Oracle.** Para mais detalhes, acesse [<<aqui>>](http://tdn.totvs.com/display/tec/DBAccess+-+Banco+de+dados) e veja as informações dos SGBDs mencionados. Importante verificar e parametrizar o [Collation](http://tdn.totvs.com/display/tec/Character+Set+x+Collation+para+DBAccess) correto.
  + Caso já tenha disponível e pronto para uso uma instalação do sistema de banco de dados com os pré-requisitos acima (Sgbd e Collation), pode-se utilizar esta mesma instalação para a base de dados do TAF utilizando um database diferente (específico do TAF);
    - Caso já possua algum produto Protheus, pode-se utilizar o mesmo database do ERP.
  + **Para o TSS temos somente os SGBDs DB2, Informix, MS SQL Server, My SQL e Oracle.**
* **Segurança**: É necessário que a autenticação de acesso ao banco de dados seja através de uma senha do SGBD ou uma autenticação mista, ou seja, através de uma senha do SGBD ou do SO. A autenticação automática pelo SO impede a inicialização do serviço.
Java

Para o correto funcionamento do instalador completo, é necessário que o **Java 32 Bits** esteja instalado na máquina.

O download pode ser realizado diretamente clicando [<<aqui>>](http://javadl.oracle.com/webapps/download/AutoDL?BundleId=230540_2f38c3b165be4555a1fa6e98c45e0808). Será efetuado o download da última versão 32 bits que estiver disponível.

Caso queira realizar o download manual, veja abaixo qual arquivo deverá ser baixado:

# Criação de Base de dados

---

Antes de qualquer processo de instalação **deverão ser criadas duas bases vazias**, uma com o nome de TAF e a outra de TSS:

## TAF e TSS utilizando SQL Server

---

Base de Dados

Caso o **SGBD** utilizado seja o **SQL Server**, segue procedimento para a criação da base de dados.

1º Passo

Acesse o SQL Management Studio, clique com o botão direito do mouse sobre “**Bancos de Dados**” (Databases) e em seguida em “**Novo banco de dados**” (New Database).

2º Passo

Digite o nome da base a ser criada para integração com o TAF:

3º Passo

Em seguida acesse o menu “Opções” para realizar a alteração do “**collation**” (Agrupamento).

Obs: O collation a ser utilizado na criação da base de dados é o Latin1\_General\_BIN e o modo de compatibilidade é o 2008 (100).

4º Passo

Após a criação da base de dados, execute o script abaixo para criar o usuário padrão:

IF NOT EXISTS(SELECT \* FROM MASTER.DBO.SYSLOGINS WHERE NAME = 'esocial')  
BEGIN  
CREATE LOGIN esocial WITH PASSWORD = 'esocial',CHECK\_POLICY=OFF  
END  
ALTER AUTHORIZATION ON database::TAF TO [esocial];

5º Passo

Novamente clique com o botão direito do mouse sobre “**Bancos de Dados**” (Databases) e em seguida em “**Novo banco de dados**” (New Database).

6º Passo

Digite o nome da base que será utilizada para integração com o TSS:

7º Passo

Em seguida acesse o menu “**Opções**” para realizar a alteração do “**collation**” (Agrupamento).

Obs: O collation a ser utilizado na criação da base de dados é o Latin1\_General\_BIN e o modo de compatibilidade é o 2008 (100).

8º Passo

Após a criação da base de dados, execute o script abaixo para criar o usuário padrão:

IF NOT EXISTS(SELECT \* FROM MASTER.DBO.SYSLOGINS WHERE NAME = 'esocial')  
BEGIN  
CREATE LOGIN esocial WITH PASSWORD = 'esocial',CHECK\_POLICY=OFF  
END  
ALTER AUTHORIZATION ON database::TSS TO [esocial];

## Criação do ODBC (Somente para base de dados SQL)

---

Criação e configuração ODBC - TAF e TSS

Criação e configuração ODBC - TAF1º Passo

É necessário que o ODBC seja criado em 32 bits, então execute o comando “%**systemdrive%\Windows\System32\odbcad32.exe**” - para TOTVS | DBAccess 32 bits em sistemas operacionais 64 bits.

2º Passo

Após executar o comando, o Windows abre o “Administrador de Fonte de dados ODBC”.

Crie a fonte de dados acessando a aba “**Fonte de dados do sistema**” e clicando em “**Adicionar**”:

3º Passo

Selecione o driver "**SQL Server Native Client 11.0**"

4º Passo

Informe o nome da nova fonte de dados (por padrão utilizamos o nome **TAF**) e o nome do servidor onde a base de dados foi criada e clique em “Avançar”:

5º Passo

Na tela seguinte, informe o usuário e senha de banco de dados que serão utilizados para realizar a conexão. Por padrão, o script criará o usuário “**esocial**” com a senha “**esocial**”. Preencha as informações e clique em “Avançar”:

6º Passo

Na opção “Alterar o banco de dados padrão para”, selecione a base de dados criada para o TAF e marque as opções “Usar identificadores ANSI entre aspas” e “Usar nulos, preenchimentos e avisos ANSI” e clique em “Avançar”:

7º Passo

Marque a opção “Executar conversão dos dados de caracteres” e clique em “Concluir”:

8º Passo

Utilize a opção “Testar fonte de dados” para validar as informações passadas na criação do ODBC.

9º Passo

Após a conclusão do processo de criação do ODBC para a base de dados TAF, vamos realizar o mesmo procedimento para a base **TSS**.

Crie a fonte de dados acessando a aba “**Fonte de dados do sistema**” e clicando em “**Adicionar**”.

Informe o nome da nova fonte de dados (por padrão utilizamos o nome **TSS**) e o nome do servidor onde a base de dados foi criada e clique em “Avançar”:

10º Passo

Na tela seguinte, informe o usuário e senha de banco de dados que serão utilizados para realizar a conexão. Por padrão, o script criará o usuário “**esocial**” com a senha “**esocial**”. Preencha as informações e clique em “Avançar”:

11º Passo

Na opção “Alterar o banco de dados padrão para”, selecione a base de dados criada para o**TSS** e marque as opções “Usar identificadores ANSI entre aspas” e “Usar nulos, preenchimentos e avisos ANSI” e clique em “Avançar”:

12º Passo

Marque a opção “Executar conversão dos dados de caracteres” e clique em “Concluir”:

13º Passo

Utilize a opção “Testar fonte de dados” para validar as informações passadas na criação do ODBC.

14º Passo

Caso o ODBC tenha sido criado corretamente, a mensagem abaixo será apresentada:

## TAF e TSS utilizando Oracle

---

Oracle

Caso o **SGBD** utilizado seja o **Oracle**, segue procedimento para a criação da instância.

**Observação Importante: Deverão ser criadas duas instâncias, uma para o TAF e outra para o TSS com os mesmos acessos concedidos no script de criação de usuário.**

1º Passo

Abra o assistente de configuração do Banco de dados e selecine a opção “Criar Banco de Dados”

2º Passo

Na tela **modo de criação** informe o “Nome do Banco de dados”  o chracter set deve ser o **WE8MSWIN1252** conforme abaixo. Determine uma senha e confirme a mesma.

Obs: Esta senha será atribuída ao usuário ‘sys’. Para criação de outro usuário você pode utilizar após criação da instância o script de criação do usuário que consta na documentação, o indicado é que seja feito. Clique em “próximo”.

3º Passo

Esta tela apresenta um resumo das informações da instância. Clique em “ Finalizar”.

4º Passo

Ao ser apresentada a seguinte tela, basta aguardar o processo de criação da instância ser concluído.

5º Passo

O processo esta finalizado após apresentação da seguinte tela.

6º Passo

Para criar o **tnsnames.ora**, acesse o Net Manager e clique em “Configurações do Oracle Net”.

7º Passo

Espanda até encontrar a opção “Nomeação de Serviço”, selecione a mesma e após clique no ícone de adição.

8º Passo

A configuração do nome do serviço é feita neste momento, informe o nome desejado.

9º Passo

Selecione o protocolo de rede e clique em “Próximo”

10º Passo

Informe neste momento o nome do servidor onde foi criado o banco de dados e o número da porta a ser utilizada.

11º Passo

Neste caso deve ser informado o mesmo nome da instância já criada.

12º Passo

Você pode realizar um teste da conexão nesta tela. Caso seja necessário realizar outras validações referentes a conexão criada, clique [aqui](http://tdn.totvs.com/pages/releaseview.action?pageId=270922659) e acesse o documento no TDN .

13º Passo

Após a criação da base de dados, execute o script abaixo para criar o usuário padrão:

--Criação de tablespaces específicas para o TAF - Motivo: Desempenho e gerenciamento

CREATE TABLESPACE ESOCIAL\_DADOS

DATAFILE 'C:\BasesOracle\Taf\ESOCIALDADOS1.DAT' SIZE 120M  AUTOEXTEND ON NEXT 10M

   DEFAULT STORAGE ( INITIAL 8K

                 NEXT    256K

                 MINEXTENTS 1

                 MAXEXTENTS 121

                 PCTINCREASE 50);

CREATE TABLESPACE ESOCIAL\_INDICES

   DATAFILE 'C:\BasesOracle\Taf\RMIND1.IDX' SIZE 30M  AUTOEXTEND ON NEXT 10M

   DEFAULT STORAGE ( INITIAL 8K

                 NEXT    84K

                 MINEXTENTS 1

                 MAXEXTENTS 121

                 PCTINCREASE 50);

CREATE TEMPORARY TABLESPACE ESOCIAL\_TMP

   TEMPFILE 'C:\BasesOracle\Taf\ESOCIALTMP1.DAT' SIZE 10M  AUTOEXTEND ON NEXT 5M

EXTENT MANAGEMENT LOCAL;

-- Criação de Usuários

CREATE      USER ESOCIAL

      IDENTIFIED BY ESOCIAL

      DEFAULT TABLESPACE  ESOCIAL\_DADOS

      TEMPORARY TABLESPACE ESOCIAL\_TMP;

GRANT CONNECT,DBA,RESOURCE TO ESOCIAL;

GRANT CONNECT, RESOURCE, CREATE VIEW TO ESOCIAL;

GRANT SELECT ANY DICTIONARY TO ESOCIAL;

GRANT EXECUTE ON DBMS\_SYS\_SQL TO ESOCIAL;

GRANT EXECUTE ON DBMS\_SQL TO ESOCIAL;

GRANT CREATE TRIGGER TO ESOCIAL;

GRANT DROP ANY TRIGGER TO ESOCIAL;

GRANT SELECT ON V\_$SESSION TO ESOCIAL;

GRANT SELECT ON V\_$STATNAME TO ESOCIAL;

GRANT SELECT ON V\_$SESSTAT TO ESOCIAL;

GRANT SELECT ON V\_$INSTANCE TO ESOCIAL;

GRANT SELECT ON SYS.OBJ$ TO ESOCIAL;

GRANT SELECT ON SYS.COL$ TO ESOCIAL;

GRANT SELECT ON SYS.ICOL$ TO ESOCIAL;

GRANT SELECT ON SYS.IND$ TO ESOCIAL;

# Instalação do TAF

---

Após a realização dos procedimentos anteriores é hora de iniciar a instalação do TAF.

## Primeira parte - Execução do instalador

---

Instalação do TAFDownload

Para iniciarmos a instalação do TAF, extraia o conteúdo do instalador baixado e execute. A tela referente ao Contrato de Licença de uso será apresentada. Após a leitura e aceite do mesmo, clique na opção “Avançar”:

1º Passo

Selecione o diretório onde o sistema será instalado e clique em “Avançar”. Por padrão, a instalação é realizada no caminho C:\TOTVS\TAF:

2º Passo

Nesta tela são apresentados os componentes que serão instalados. Selecione o DbAccess a ser instalado e clique em avançar, sem desmarcar nenhuma opção:

3º Passo

Selecione o diretório para a criação de atalhos e clique em “Avançar”:

4º Passo

A tela abaixo será apresentada com as informações referentes aos componentes selecionados para serem instalados. Clique em instalar para iniciar o processo:

5º Passo

Durante a instalação as seguintes telas serão apresentadas. Este processo leva alguns minutos:

6º Passo

Após a finalização da configuração da instalação, o assistente será apresentado. Clique em avançar para prosseguir com a instalação:

7º Passo

Selecione a opção de SGBD que foi configurado no início do procedimento (MSSQL ou Oracle) e informe o nome da conexão que foi criada no ODBC.

Desça a tela utilizando a barra de rolagem e informe usuário e senha. Caso os mesmos tenham sido criados utilizando o script padrão do início do documento, digite:

Usuário = **esocial**  
Senha = **esocial**

**Importante:** Caso a base de dados seja **Oracle**, selecione o caminho da **oci.dll** criada na instalação do Oracle. Para facilitar, a DLL está localizada na pasta **bin** da home do Oracle.

Obs: Caso o usuário/senha tenham sido alterados no início do procedimento, favor utilizar a informar os dados utilizados.

Clique em “Avançar” para que o assistente faça as configurações necessárias no ambiente.

8º Passo

Após a criação dos arquivos de configuração do DbAccess, a mensagem informando que a configuração foi efetuada corretamente será apresentada. Clique em “Fechar” para que a instalação do TAF seja iniciada:

Caso seja apresentada a mensagem abaixo referente a falha de conexão, finalize o sistema, reinicie o serviço do DbAccess (Taf-DbAccess) e execute o sistema novamente. Além disso, valide a conexão criada utilizando o DbMonitor. (Veja no menu "Configuração DbMonitor", como realizar a validação através do aplicativo.)

9º Passo

Neste momento a instalação do TAF será iniciada. Informe a porta para comunicação com o Smartclient HTML. Por padrão, a 8095 é apresentada na instalação. Caso seja necessário, realize a alteração. (Verifique a aba de dicas para verificar se a porta está liberada.)

Caso seja possível que outras máquinas atualizem o aplicativo que está sendo instalado, informe os IP’s das mesmas utilizando o campo \*Opcional apresentado na tela e clique em “Avançar”:

10º Passo

Na tela que será apresentada, informe o IP e a porta do servidor de licenças, para que seja feita a validação e o consumo das mesmas.

11º Passo

Após fornecer as informações referentes ao License Server, será apresentada a tela para a seleção dos “Menus” a serem instalados. Orientamos que todos sejam selecionados, para evitar a necessidade de reinstalação, caso algum outro módulo seja integrado com o TAF em sua empresa. Clique em “Avançar” para prosseguir com a instalação:

12º Passo

Após a seleção dos menus a serem instalados, será apresentada a tela abaixo com alguns links úteis para maiores informações sobre o TAF e os componentes da sua instalação. Clique em “Finalizar” para que a instalação seja iniciada:

Durante a execução do instalador, a tela abaixo permanecerá aberta.

13º Passo

Após a finalização do processo, a tela abaixo será apresentada e os atalhos serão criados na área de trabalho. Finalize o assistente de instalação para que a configuração inicial do sistema seja realizada.

Caso a instalação executada tenha sido a “Instalação Completa – TAF + TSS”, conforme orientado no início do processo, aguarde alguns instantes para que a instalação do TSS seja iniciada. Caso a tela não seja apresentada, execute o comando Alt+Tab e verifique se o ícone abaixo será apresentado e selecione o mesmo.

Dicas!

Dica1: Para verificar se a porta está em uso, utilize o comando netstat -n -a | find ":8095" (onde 8095 é a porta que está sendo testada) no prompt. No exemplo abaixo, a porta está sendo utilizada:

No exemplo abaixo nenhum status foi apresentado, portanto a porta está liberada:

  

## Configuração DbMonitor

---

**Importante:** A conexão deverá ser criada para o **TAF** (conforme exemplo abaixo) e para o **TSS**, seguindo as mesmas configurações.

Caso a conexão do TAF já tenha sido criada na instalação do sistema, crie somente a do TSS.

Configuração DbMonitor1º Passo

Para realizar a validação da conexão do TAF com o DbAccess, acesse o caminho de instalação do mesmo para a realização do teste. Por padrão, o mesmo é instalado em "C:\totvs\TAF\TafDbAccess32".

Neste diretório, localize o arquivo "dbaccess.ini" e abra com um editor de texto. Nele será possível identificar a porta que foi utilizada para realizar a comunicação entre os sistemas.

2º Passo

Após identificar a porta, execute o aplicativo "DbMonitor.exe", localizado no mesmo diretório. Informe o nome da máquina em que a instalação está sendo realizada e a porta que foi identificada no passo anterior e clique em "Ok":

3º Passo

Acesse a aba “Configurações” e depois selecione a aba de acordo com o SGBD utilizado para a criação da base de dados. Clique em novo para configurar a conexão que será validada no teste.

**Importante**: Caso seja **Oracle**, utilize a aba correspondente ao SGBD.

4º Passo

Informe o nome da conexão criada no início (Por padrão, a conexão foi criada como TAF) e clique em “Ok”:

5º Passo - SQL

Selecione o ambiente, informe o usuário e a senha de banco de dados e clique em "Salvar". Na criação da base de dados, executamos o script para a criação do usuário. (Usuário: esocial e senha: esocial)

5º Passo - Oracle

Selecione o ambiente, informe o usuário e a senha de banco de dados e clique em "Salvar". Na criação da base de dados, executamos o script para a criação do usuário. (Usuário: esocial e senha: esocial)

6º Passo

Após fornecer as informações, selecione a aba “Assistentes” e em seguida a opção “Validação de Conexão”:

7º Passo

A tela de boas-vindas do assistente será apresentada. Clique na opção “Avançar” para que a tela de seleção de banco de dados seja apresentada:

8º Passo

Selecione o banco de dados utilizado para a criação das bases de dados e clique em “Avançar”:

9º Passo

Informe o nome da conexão que será testada e clique em “Finalizar”:

10º Passo

Caso a configuração da conexão esteja correta, a mensagem abaixo será apresentada. Clique em "Ok" para concluir a validação da conexão e finalize o DbMonitor.

# Instalação do TSS

---

Instalação do TSS

Após a instalação do TAF, utilizando a opção de instalação completa, a instalação do TSS será iniciada automaticamente. Siga os procedimentos abaixo para realizar a parametrização:

1º Passo

Selecione o idioma de instalação e clique em “OK”:

2º Passo

A tela de “Boas Vindas” será apresentada. Clique em “Próximo” para prosseguir com a instalação:

3º Passo

A tela referente ao Contrato de Licença de uso será apresentada. Após a leitura e aceite do mesmo, clique na opção “Avançar”:

4º Passo

\*\* Selecione o caminho para instalação e clique em “Próximo”. Por padrão, a instalação é realizada no caminho C:\totvssped, porem orientamos que o caminho seja alterado para "C:\TOTVS\TAF\totvssped, para facilitar a manutenção de arquivos:

Obs: Após a definição do caminho a ser utilizado, a mensagem abaixo será apresentada. No exemplo foi utilizado o caminho padrão:

5º Passo

Na tela seguinte, mantenha a opção referente a instalação do TOTVS Service SOA “Online” marcada e clique em “Próximo”:

6º Passo

Nesta tela, iremos utilizar algumas informações que já foram configuradas anteriormente:

Sobre as configurações do TSS, informe o nome da máquina em que o mesmo foi instalado e a porta que será utilizada para a comunicação.

Nas informações pertinentes ao banco de dados que será utilizado pelo TSS, utilize as mesmas configurações que foram preenchidas ou identificadas no DbMonitor (nome da máquina, alias e porta)

7º Passo

Como o DbAccess já foi instalado junto com o TAF, apenas mantenha as opções que foram marcadas como Default e clique em "Próximo":

8º Passo

Nesta tela, apenas altere a porta, caso a Default esteja sendo utilizada e clique em "Próximo":

9º Passo

Neste momento, o sistema será instalado. Aguarde a conclusão do processo e clique em "Próximo":

10º Passo

Agora, vamos definir as preferências em relação a utilização do sistema e a criação de atalhos. Após realizar a seleção, clique em "Próximo":

11º Passo

O sistema irá realizar as configurações finais da instalação e iniciar os serviços utilizando as mesmas. Clique em "Próximo" para concluir o processo:

12º Passo

Clique em "Pronto" para finalizar o wizard:

# Configuração inicial do TAF (primeiro acesso)

---

Configuração inicial do TAF (primeiro acesso):1º Passo

Localize o atalho criado na área de trabalho e execute o aplicativo:

2º Passo

Informe o usuário “admin”, deixe o campo referente a senha vazio e clique no botão “Entrar”:

3º Passo

Na tela de boas-vindas ao usuário, verifique as informações apresentadas e clique novamente em “Entrar”:

4º Passo

Selecione a localização e clique em “Ok”:

5º Passo

A tela referente a criação das tabelas do sistema será apresentada:

6º Passo

Selecione o diretório dos arquivos de dados (C:\totvs\TAF\data) e clique em abrir:

7º Passo

Novamente a tela de criação de tabelas na base de dados será apresentada:

8º Passo

Ao finalizar a criação das tabelas, será apresentada a tela de cadastro de moedas. Apenas clique em “Confirmar”:

9º Passo

Neste momento será apresentada a tela informando que existe uma divergência nas informações. Clique em "Avançar" para corrigir/atualizar a informação.

10º Passo

Clique no menu "Efetuar amarração dos Estabelecimentos" para iniciar o procedimento:

11º Passo

Na tela abaixo, de um duplo clique no campo "Código Complementar" até que apareça a informação 99 (onde 99 equivale ao Grupo de Empresa) + 01 (onde 01 equivale ao Código da Filial).

Neste caso ficaria 9901. Após alterar as informações, clique em "Confirmar" para prosseguir.

12º Passo

Aguarde o termino do processamento das informações, conforme tela abaixo e posteriormente clique em finalizar. Neste momento será necessário efetuar um **novo login** no TAF.

# Configuração inicial do TAF (segundo acesso)

---

Configuração inicial do TAF (segundo acesso):1º Passo

Após efetuar o **segundo login** no sistema, a tela de apresentação do processo de configuração do TAF será apresentada. Clique em “Avançar”:

2º Passo

Na tela de seleção do Grupo para processamento, selecione as empresas habilitadas para processamento e clique em “Avançar”:

3º Passo

Selecione as opções marcadas abaixo e clique em “Avançar”:

4º Passo

Na opção “Porta de Conexão do DbAccess” a informação deverá ser a mesma que foi utilizada no início da instalação. (Verifique a informação conforme a configuração realizada no DbMonitor):

5º Passo

Na tela seguinte, por padrão a “Porta de conexão do Web Services” vem como 8080, porém essa porta geralmente já é usada no RM Portal. Orientamos que utilize a porta 8090, caso a mesma não esteja em uso. Clique em “Avançar” após o preenchimento das informações:

6º Passo

Clique em “Processar as configurações realizadas neste assistente” para finalizar a configuração:

7º Passo

Será exibida a tela de status do processamento das informações.

8º Passo

Ao finalizar o procedimento solicitado, será exibida a tela anterior com o log de execução:

9º Passo

Clique em finalizar e reinicie o sistema para prosseguir com as parametrizações:

10º Passo

Ao finalizar o wizard, um resumo das configurações utilizadas será apresentado. Apenas confirme as informações e clique em "Sair":

falsefalse

**Produto:** TAF e TSS

false

**Versão:** 12.1.XX

false

**Processo:** Instalação e configuração do TAF - TOTVS Automação Fiscal e TSS - TOTVS Service SOA.

falsefalse

**Status:** Publicado

false

**Data:**

false

**Autores:**
