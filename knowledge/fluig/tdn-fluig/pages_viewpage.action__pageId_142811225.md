---
content_hash: eca95e7c6643642ce9ade904f227bbd73455e0c56d52ebf3cca5496d5baafe0b
fetched_at: '2026-06-28T21:35:17.844287+00:00'
page_id: '142811225'
product: fluig
source: tdn-fluig
title: ARQ - Como configurar o banco de dados Oracle na release 1.5.13 ou anterior?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=142811225
version: 47
---

Atenção

Página destinada a atualizações 1.5.13 e anteriores.

Acesse a página original a partir da atualização 1.6: [Configuração do banco de dados Oracle](http://tdn.totvs.com/pages/viewpage.action?pageId=257623480).

## Versões homologadas do Oracle

Para verificar as versões homologadas do Oracle acesse a 

## Configuração do banco

É necessário que o administrador do banco Oracle® (DBA) efetue algumas alterações de segurança no banco de dados Oracle®, fazendo com que o usuário (schema) informado na instalação do TOTVS Fluig Plataforma não possua permissão de leitura/alteração em outros schemas do banco Oracle®, caso existam.  
Deve possuir permissão de leitura/alteração somente no usuário (*schema*) utilizado pela plataforma.

## Criação do usuário e concessão de privilégios

Para a criação de um novo usuário em banco de dados Oracle usamos a instrução CREATE USER, conforme sintaxe abaixo:

sql

Onde:

* **userid:** Nome do usuário que será criado;
* **password:** Senha do usuário que será criado;
* **tablespace (opcional):** Tablespace padrão onde os objetos do banco de dados serão armazenados. Se essa opção for omitida, o Oracle assume a tablespace SYSTEM padrão;
* **temp\_tablespace (opcional):** Tablespace padrão onde são armazenados os objetos temporários, como por exemplo tabelas temporárias. Se essa opção for omitida, o Oracle assume um tablaspace temporário TEMP.

Após criado o usuário é necessário conceder os privilégios de sistema (conexão e instruções DLL por exemplo) necessários para ele, conforme sintaxe abaixo:

sql

Onde:

* **userid:** Nome do usuário criado anteriormente;

Neste momento é necessário executar os procedimentos SQL abaixo com o usuário **userid** no banco de dados a ser usado para a plataforma:

Atenção!

* É imprescindível conectar no banco de dados com o usuário **userid** para a execução dos procedimentos abaixo, a fim de garantir o isolamento e integridade da operação.
* O servidor deve estar parado no momento da execução do script.
sql 'SYS') AND (AUX\_USERCONNECTED <> 'SYSTEM') THEN
EXECUTE IMMEDIATE ('CREATE OR REPLACE VIEW ' ||AUX\_USERCONNECTED|| '.ALL\_OBJECTS AS' ||
' SELECT \* FROM SYS.ALL\_OBJECTS WHERE OWNER IN (SELECT USER FROM DUAL)');
EXECUTE IMMEDIATE ('CREATE OR REPLACE VIEW ' ||AUX\_USERCONNECTED|| '.ALL\_SYNONYMS AS' ||
' SELECT \* FROM SYS.ALL\_SYNONYMS WHERE OWNER IN (SELECT USER FROM DUAL)');
EXECUTE IMMEDIATE ('CREATE OR REPLACE VIEW ' ||AUX\_USERCONNECTED|| '.ALL\_SEQUENCES AS' ||
' SELECT \* FROM SYS.ALL\_SEQUENCES WHERE SEQUENCE\_OWNER IN (SELECT USER FROM DUAL)');
EXECUTE IMMEDIATE ('CREATE OR REPLACE VIEW ' ||AUX\_USERCONNECTED|| '.ALL\_CONSTRAINTS AS' ||
' SELECT \* FROM SYS.ALL\_CONSTRAINTS WHERE OWNER IN (SELECT USER FROM DUAL)');
EXECUTE IMMEDIATE ('CREATE OR REPLACE VIEW ' ||AUX\_USERCONNECTED|| '.ALL\_CONS\_COLUMNS AS' ||
' SELECT \* FROM SYS.ALL\_CONS\_COLUMNS WHERE OWNER IN (SELECT USER FROM DUAL)');
EXECUTE IMMEDIATE ('CREATE OR REPLACE VIEW ' ||AUX\_USERCONNECTED|| '.ALL\_INDEXES AS' ||
' SELECT \* FROM SYS.ALL\_INDEXES WHERE OWNER IN (SELECT USER FROM DUAL)');
EXECUTE IMMEDIATE ('CREATE OR REPLACE VIEW ' ||AUX\_USERCONNECTED|| '.ALL\_IND\_COLUMNS AS' ||
' SELECT \* FROM SYS.ALL\_IND\_COLUMNS WHERE TABLE\_OWNER IN (SELECT USER FROM DUAL)');
EXECUTE IMMEDIATE ('CREATE OR REPLACE VIEW ' ||AUX\_USERCONNECTED|| '.ALL\_TABLES AS' ||
' SELECT \* FROM SYS.ALL\_TABLES WHERE OWNER IN (SELECT USER FROM DUAL)');
EXECUTE IMMEDIATE ('CREATE OR REPLACE VIEW ' ||AUX\_USERCONNECTED|| '.ALL\_TAB\_COLUMNS AS' ||
' SELECT \* FROM SYS.ALL\_TAB\_COLUMNS WHERE OWNER IN (SELECT USER FROM DUAL)');
END IF;
END;]]>

**Oracle 12c**

Caso seja utilizado Oracle 12c ou superior é necessário alterar o arquivo **<INSTALL\_FLUIG>\jboss\bin\standalone.conf.bat**(standalone.conf em ambientes Linux) e incluir a seguinte linha:

bashObservação

**NLS** (National Language Support) é utilizado para definir datas, números, moeda e configurações de idioma.

O *NLS\_CHARACTERSET* para a plataforma é **AL32UTF8**.

# Datasource - Finalidade da Tag new-connection-sql

No arquivo de configuração **standalone.xml** ([Instalação fluig]/jboss/standalone/configuration) da plataforma é incluído pela wizard de instalação, quando selecionado o banco de dados Oracle, a tag abaixo, tendo a seguinte finalidade:

xmlEclipsestandalone.xmlalter session set nls\_comp = 'LINGUISTIC' nls\_sort = 'BINARY\_CI']]>

* O parâmetro **nls\_comp** especifica o comportamento de agrupamento da sessão do banco de dados. É utilizado como *LINGUISTIC*, aonde as comparações irão ignorar maiúsculos e minúsculos inclusive quando utilizamos *LIKE*, pois a busca passa a ser alfabética, e não a padrão binária.
* O parâmetro **nls\_sort** especifica a sequência de agrupamento para consultas *ORDER BY*. É usado como *BINARY\_CI*, ou seja valor *BINARY.* Significa que a ordenação dos caracteres seguirão de acordo com a ordem em que os caracteres aparecem no *Character Set* em uso, e o CI é para ignorar maiúsculas e minusculas.
