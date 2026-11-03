---
content_hash: 8909032cc733ef31e8527dedfb359db7f76a38df5874b5c4d63e51184f6b47bc
fetched_at: '2026-06-28T21:35:23.666284+00:00'
page_id: '257623480'
product: fluig
source: tdn-fluig
title: Configuração do banco de dados Oracle
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=257623480
version: 26
---

Fique atento!

Esta página é válida para atualizações **1.6** e **superiores** do TOTVS Fluig.

Caso possua uma atualização anterior acesse:

4.\*ndice

# Versões homologadas do Oracle

---

Para verificar as versões homologadas do Oracle acesse a 

# Configuração do banco

---

**Pré-requisitos**

* É necessário que o administrador do banco Oracle® (DBA) efetue algumas alterações de segurança no banco de dados Oracle®, fazendo com que o usuário (*schema*) informado na instalação da plataforma não possua permissão de leitura/alteração em outros *schemas* do banco Oracle®, caso existam.

* Deve possuir permissão de leitura/alteração somente no usuário (*schema*) utilizado pela plataforma.

Importante!

Por questões de segurança é altamente recomendável efetuar a encriptação da senha conforme o procedimento informado na documentação [encriptação de senha de banco do dados](http://tdn.totvs.com/x/Oh4WGw).

## Criação do usuário e concessão de privilégios

---

falseoraclePasso 1

Para a criação de um novo usuário em banco de dados Oracle usamos a instrução CREATE USER, conforme sintaxe abaixo:

sql

Onde:

* userid: Nome do usuário que será criado;

* password: Senha do usuário que será criado;

* tablespace (opcional): Tablespace padrão onde os objetos do banco de dados serão armazenados. Se essa opção for omitida, o Oracle assume a tablespace SYSTEM padrão;

* temp\_tablespace (opcional): Tablespace padrão onde são armazenados os objetos temporários, como por exemplo tabelas temporárias. Se essa opção for omitida, o Oracle assume um tablespace temporário TEMP.

Passo 2

Após criado o usuário é necessário conceder os privilégios de sistema (conexão e instruções DLL por exemplo) necessários para ele, conforme sintaxe abaixo:

sql

Onde:

* userid: Nome do usuário criado anteriormente;

OBS: 

* O alter user foi necessário na hora de subir o Fluig para criar as tabelas;

Passo 3

Neste momento é necessário executar os procedimentos SQL abaixo com o usuário **userid** no banco de dados a ser usado para a plataforma:

Atenção!

* É imprescindível conectar no banco de dados com o usuário userid para a execução dos procedimentos acima, a fim de garantir o isolamento e integridade da operação.

* O servidor Fluig deve estar parado no momento da execução do *script*.
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

O **NLS** (*National Language Support*) é utilizado para definir datas, números, moeda e configurações de idioma. O *NLS\_CHARACTERSET* (charset) para a plataforma é **AL32UTF8**.

# *Datasource* - finalidade da *tag* new-connection-sql

---

Ao instalar a plataforma selecionando o banco de dados Oracle, o instalador inclui a *tag* abaixo no arquivo de configuração, de acordo com a atualização:

* **a partir da atualização 2.0:**no arquivo **standalone.xml** ([diretório\_instalação]/appserver/standalone/configuration/standalone.xml);

* **da atualização 1.6 até a 1.8.2**:no arquivo **domain.xml** ([diretório\_instalação]/appserver/domain/configuration/domain.xml).

xmlEclipsealter session set nls\_comp = 'LINGUISTIC' nls\_sort = 'BINARY\_CI']]>

Onde:

* o parâmetro **nls\_comp** especifica o comportamento de agrupamento da sessão do banco de dados. É utilizado como *LINGUISTIC*, onde as comparações irão ignorar maiúsculos e minúsculos, inclusive quando utilizamos *LIKE*, pois a busca passa a ser alfabética e não mais a padrão binária;

* o parâmetro **nls\_sort** especifica a sequência de agrupamento para consultas *ORDER BY*. É usado como BINARY\_CI, ou seja, valor *BINARY*. Significa que a ordenação dos caracteres seguirão de acordo com a ordem em que os caracteres aparecem no *Character Set* em uso e o CI é para ignorar maiúsculas e minúsculas.
