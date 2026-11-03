---
content_hash: b8408aa32454abe0d55a435024104b92a8caa1c4251b7f64059dc40927eaed2a
fetched_at: '2026-06-29T00:08:47.998972+00:00'
page_id: '322146156'
product: rm
source: tdn-rm
title: Pré Requisitos para migração e utilização do Novo Log de Auditoria.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=322146156
version: 24
---

---

**Pré Requisitos para migração e utilização do Novo Log de Auditoria.**

**ORACLE**

Por questões de organização, segurança e performance, foi criada uma rotina que é executada no momento da migração para o Novo Log de Auditoria, a mesma faz a criação do Esquema **TOTVSAUDIT** e dos **TABLESPACES** **TOTVSAUDIT\_DADOS** e **TOTVSAUDIT\_INDICES**.

Os tablespaces serão criados nos mesmos diretórios de dados onde já existem os arquivos de dados dos tablespaces de sistema **RM\_DADOS** e **RM\_INDICES. (Caso seja de sua preferência os tablespaces podem ser criados antecipadamente pela sua equipe de DBA's, assim pode-se definir um local diferente para os mesmos.)**

Para esta utilização é pré-requisito que o usuário possua as seguintes permissões:

**SELECT ANY DICTIONARY,****SELECT ON DBA\_LOBS e****SELECT ON DBA\_SEGMENTS.**

É necessário também que o parâmetro do SGBD Oracle **JOB\_QUEUE\_PROCESSES**esteja com o valor superior a 100.

Caso o usuário não atenda aos pré-requisitos acima, poderão ocorrer erros na conversão da Base de Dados para nova versão.

**A partir da versão 12.1.24** foi implementada uma nova ACTION que realiza algumas verificações na base de dados Oracle, a mesma tem a funcionalidade de verificar se existem problemas no Schema ou objetos do Novo Log de Auditoria, para que não ocorra problemas na Conversão da base de dados.

Caso apresente o erro abaixo durante a conversão, deve-se realizar as seguintes verificações.

As verificações acima devem ser executadas com o Owner do Sistema RM no banco de dados. (Padrão, Schema RM)

**Testes de Homologação de Novas versões em Bases de Dados Oracle**

Caso seja necessário restaurar uma base de dados Oracle em um ambiente de homologação, utilizando-se das ferramentas IMP ou IMPDP, deve-se restaurar o Schema RM,  após o final da restauração deve-se executar a Stored Procedure p\_FixNovoLog.(Disponível nas versões 12.1.22 e superiores, verificar junto ao suporte o Patch que possui esta feature disponível)

Comando:**EXEC p\_FixNovoLog;**

Esta nova Stored Procedure faz uma verificação e cria ou recria os objetos necessários para o correto funcionamento do Novo Log de Auditoria como Schema de Auditoria, Tabelas, Grants, Etc.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**SQL SERVER**

**Caso esteja sendo utilizado o Novo Log de Auditoria em MS SQL Server e aplicações em Delphi é necessário se atentar ao seguinte ponto:**

Devido ao funcionamento do Delphi o parâmetro **CONCAT\_NULL\_YIELDS\_NULL**  e **ANSI\_WARNINGS** devem estar ligados.

Este será o comportamento padrão do MS SQL Server em versões futuras de acordo com a Microsoft.

******Parâmetro****CONCAT\_NULL\_YIELDS\_NULL**

<https://docs.microsoft.com/en-us/sql/t-sql/statements/set-concat-null-yields-null-transact-sql?view=sql-server-2017>

****Parâmetro ANSI\_WARNINGS****

**<https://docs.microsoft.com/en-us/sql/t-sql/statements/set-ansi-warnings-transact-sql?view=sql-server-2017>**

Este parâmetro deve ser alterado a nível de banco de dados, conforme exemplo abaixo:

****Parâmetro CONCAT\_NULL\_YIELDS\_NULL****

**USE [master]**

**GO**  
**ALTER DATABASE [CorporeRM]\* SET CONCAT\_NULL\_YIELDS\_NULL ON WITH NO\_WAIT**  
**GO**

**Parâmetro ANSI\_WARNINGS** 

**USE [master]**

**GO**  
**ALTER DATABASE [Corpore]\* SET ANSI\_WARNINGS ON WITH NO\_WAIT**  
**GO**

\* **CorporeRM** será o nome do Database em uso pela aplicação.

**Observações sobre Grants no Oracle para o user RM e user TOTVSAudit:**

Na versão 12.1.31 não utilizamos mais sinônimos, contudo o RM precisa ter atribuição de DBA para execução/configuração do TOTVSAudit.

Na versão 12.1.32 foi retirada a atribuição de DBA para o RM, porém, é necessário atribuir alguns grants para execução/configuração do TOTVSAudit:

**Sugestão de comandos para adequação do RM nesta versão:**

GRANT ALTER ANY TABLE, CREATE ANY TABLE, DROP ANY TABLE, DELETE ANY TABLE, SELECT ANY TABLE, INSERT ANY TABLE, CREATE ANY INDEX, DROP ANY INDEX, CREATE ANY SEQUENCE, DROP ANY SEQUENCE, SELECT ANY SEQUENCE TO RM;
