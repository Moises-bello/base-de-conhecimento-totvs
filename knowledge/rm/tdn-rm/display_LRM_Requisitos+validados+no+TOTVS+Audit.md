---
content_hash: 2f2de41991823587bf9f05e488cee93b7cb46132495f292d7d3c284bf0159eeb
fetched_at: '2026-06-29T00:10:46.581795+00:00'
page_id: '554662592'
product: rm
source: tdn-rm
title: Requisitos validados no TOTVS Audit
type: documentation
url: https://tdn.totvs.com/display/LRM/Requisitos+validados+no+TOTVS+Audit
version: 4
---

**Critérios para correta execução do configurador do TOTVS Audit (Oracle)**

* Versão Da Base de Dados:  este critério impede que o configurador seja executado em bases com versões anteriores à 12.1.29, ou seja, será necessário converter sua base com o RM.Atualizador antes da utilização deste assistente de configuração do TOTVS Audit.
* FUNCTION SPLIT: este critério cita a ausência de uma função a qual espera-se que exista na base do cliente na versão 12.1.29 e que será utilizado na execução do configurador TOTVS Audit.
* TABELA GDIC: este critério cita a ausência/acesso à tabela gdic, que será utilizada na execução do configurador TOTVS Audit.
* TABELA ZLOGCAMPOS: este critério cita a ausência/acesso à tabela zlogcampos, que será utilizada na execução do configurador TOTVS Audit.
* TABELA ZAUDITCONFIG: este critério cita a ausência ou acesso à tabela zauditconfig e que será utilizada na execução do configurador TOTVS Audit.
* VALIDAÇÃO DO SCHEMA DO TOTVS Audit: este critério avalia na visão DBA\_USERS se o schema informado na coluna RM.ZAUDITCONFIG.AUDITSCHEMANAME  está presente ao qual será utilizado na execução no configurador.

**Critérios para correta execução do configurador do TOTVS Audit (Sql Server)**

* Versão Da Base de Dados:  este critério impede que o configurador seja executado em bases com versões anteriores à 12.1.29, ou seja, será necessário converter sua base com o RM.Atualizador antes da utilização deste assistente de configuração do TOTVS Audit.
* FUNCTION SPLIT: este critério cita a ausência de uma função a qual espera-se que exista na base do cliente na versão 12.1.29 e que será utilizado na execução do configurador TOTVS Audit.
* TABELA GDIC: este critério cita a ausência/acesso à tabela gdic, que será utilizada na execução do configurador TOTVS Audit.
* TABELA ZLOGCAMPOS: este critério cita a ausência/acesso à tabela zlogcampos, que será utilizada na execução do configurador TOTVS Audit.
* TABELA ZAUDITCONFIG: este critério cita a ausência ou acesso à tabela zauditconfig e que será utilizada na execução do configurador TOTVS Audit.
* VALIDAÇÃO DO SCHEMA DO TOTVS Audit: este critério avalia na visão SYS.schemas se o schema informado na coluna dbo.ZAUDITCONFIG.AUDITSCHEMANAME  está presente ao qual será utilizado na execução no configurador.

**Validação dos objetos dependentes para a execução das Procedures - SQL SERVER**

Esses objetos são validados na tela pré-requisitos e mostrar o status de inexistência/Acesso desses objetos caso ocorra.

GDIC, ZAUDITCONFIG, ZAUDITITEMS, ZLOGPARAMS, DBO.SPLIT, SYS.OBJECTS, SYS.INDEXES, SYS.INDEX\_COLUMNS, SYS.COLUMNS, SYS.SCHEMAS, SYS.TABLES, SYS.TYPES  
SYS.PARTITIONS INFORMATION\_SCHEMA.COLUMNS, ZLOGPROCESSOS ou ZLOGPROCESSOS\_OLD, ZLOGCAMPOS e SYS.VIEWS

**Validação dos objetos dependentes para a execução das Procedures - ORACLE**

Esses objetos são validados na tela pré-requisitos e mostrar o status de inexistência/Acesso desses objetos caso ocorra.

GDIC, USER\_TRIGGERS, USER\_SEQUENCES, USER\_TAB\_COLS, ALL\_TABLES, ALL\_TRIGGERS, ALL\_TAB\_COLS, DBA\_SEGMENTS, DBA\_SEQUENCES, DBA\_TAB\_PRIVS  
DBA\_TRIGGERS, DBA\_OBJECTS, DBA\_TABLES, DBA\_USERS, DBA\_LOBS, V$VERSION, DBMS\_OUTPUT, SPLIT e SPLIT\_TBL
