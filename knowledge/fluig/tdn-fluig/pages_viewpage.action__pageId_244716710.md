---
content_hash: 28f683233104968cdf937b71ab4652af3b8e6e06114156f9f23f461d2db318d7
fetched_at: '2026-06-28T21:35:23.252493+00:00'
page_id: '244716710'
product: fluig
source: tdn-fluig
title: Modelos de Armazenamento de Formulários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244716710
version: 12
---

# Índice

4true.\*ndicenone

# Objetivo

---

O objetivo deste documento é descrever e diferenciar os tipos de armazenamento de dados de formulários na base do fluig.

## Definição do Modelo de Armazenamento

---

O modelo de armazenamento é definido pelo desenvolvedor durante a  através do . Esta opção só é exibida ao exportar um novo formulário para o servidor.

Na imagem abaixo são exibidos os dois modelos disponíveis:

* "Numa única tabela (para pequenas quantidades de registros)", também chamado de modelo "Registros de formulário (Tabela única)".

* "Tabelas de Banco de Dados (recomendado)", também chamado de "Meta Lista (Tabelas múltiplas)".

## Tabelas de Banco de Dados (recomendado)

---

Um formulário configurado para armazenar seus dados em tabelas múltiplas, quando exportado criará uma nova tabela no banco de dados cujo nome seguirá o padrão MLEEELLL, onde EEE representa o código da empresa precedido por zeros e LLL representa o código da lista (gerado de forma sequencial pela plataforma) também precedido por zeros.

Exemplo

Se o código da empresa for "1" e já foram criados 20 formulários previamente, o próximo formulário criado (de nº 21) irá gerar a tabela ML001021.

Os registros destes formulários também serão separados em Meta Listas filhas, que seguirão o mesmo padrão de criação e serão relacionadas através da tabela META\_LISTA\_REL.

O modelo de tabelas múltiplas, por segmentar os dados dos formulários e tornar mais eficiente a consulta a estes registros, é o **modelo recomendado** e também o padrão para a exportação de novos formulários para o servidor fluig.

### Nomes dos campos

---

Quando em armazenado em tabelas de banco dados, cada campo do formulário vira uma coluna com o mesmo nome.

Isso gera duas limitações quanto ao nome dos campos:

* O tamanho do nome, que é limitado à 30 caracteres;
* Os bancos de dados possuem palavras reservadas, que não podem ser usadas como nome da colunas. Abaixo é apresentada uma lista de termos reservados (além de alguns campos que são usados internamente para o vínculo ao registro do formulário):

"ABSOLUTE", "ACCESS", "ACCESSIBLE", "ACCOUNT", "ACTION", "ACTIVATE", "ADD",  
 "ADMIN", "ADVISE", "AFTER", "AGGREGATE", "ALIAS", "ALL", "ALLOCATE", "ALL\_ROWS", "ALTER", "ANALYZE", "AND",  
 "ANY", "ARCHIVE", "ARCHIVELOG", "ARE", "ARRAY", "AS", "ASC", "ASENSITIVE", "ASSERTION", "AT", "AUDIT",  
 "AUTHENTICATED", "AUTHORIZATION", "AUTOEXTEND", "AUTOMATIC", "BACKUP", "BECOME", "BEFORE", "BEGIN",  
 "BETWEEN", "BFILE", "BIGINT", "BINARY", "BIT", "BITMAP", "BLOB", "BLOCK", "BODY", "BOOLEAN", "BOTH",  
 "BREADTH", "BREAK", "BROWSE", "BULK", "BY", "CACHE", "CACHE\_INSTANCES", "CALL", "CANCEL", "CASCADE",  
 "CASCADED", "CASE", "CAST", "CATALOG", "CFILE", "CHAINED", "CHANGE", "CHAR", "CHARACTER", "CHAR\_CS",  
 "CHECK", "CHECKPOINT", "CHOOSE", "CHUNK", "CLASS", "CLEAR", "CLOB", "CLOSE", "CLOSE\_CACHED\_OPEN\_CURSORS",  
 "CLUSTER", "CLUSTERED", "COALESCE", "COLLATE", "COLLATION", "COLUMN", "COLUMNS", "COMMENT", "COMMIT",  
 "COMMITTED", "COMPATIBILITY", "COMPILE", "COMPLETE", "COMPLETION", "COMPOSITE\_LIMIT", "COMPRESS",  
 "COMPUTE", "CONDITION", "CONNECT", "CONNECTION", "CONNECT\_TIME", "CONSTRAINT", "CONSTRAINTS",  
 "CONSTRUCTOR", "CONTAINS", "CONTAINSTABLE", "CONTENTS", "CONTINUE", "CONTROLFILE", "CONVERT",  
 "CORRESPONDING", "COST", "CPU\_PER\_CALL", "CPU\_PER\_SESSION", "CREATE", "CROSS", "CUBE", "CURRENT",  
 "CURRENT\_DATE", "CURRENT\_PATH", "CURRENT\_ROLE", "CURRENT\_SCHEMA", "CURRENT\_TIME", "CURRENT\_TIMESTAMP",  
 "CURRENT\_USER", "CURSOR", "CYCLE", "DANGLING", "DATA", "DATABASE", "DATABASES", "DATAFILE", "DATAFILES",  
 "DATAOBJNO", "DATE", "DAY", "DAY\_HOUR", "DAY\_MICROSECOND", "DAY\_MINUTE", "DAY\_SECOND", "DBA", "DBCC",  
 "DBHIGH", "DBLOW", "DBMAC", "DEALLOCATE", "DEBUG", "DEC", "DECIMAL", "DECLARE", "DEFAULT", "DEFERRABLE",  
 "DEFERRED", "DEGREE", "DELAYED", "DELETE", "DENY", "DEPTH", "DEREF", "DESC", "DESCRIBE", "DESCRIPTOR",  
 "DESTROY", "DESTRUCTOR", "DETERMINISTIC", "DIAGNOSTICS", "DICTIONARY", "DIRECTORY", "DISABLE",  
 "DISCONNECT", "DISK", "DISMOUNT", "DISTINCT", "DISTINCTROW", "DISTRIBUTED", "DIV", "DML", "DOMAIN",  
 "DOUBLE", "DROP", "DUAL", "DUMMY", "DUMP", "DYNAMIC", "EACH", "ELSE", "ELSEIF", "ENABLE", "ENCLOSED",  
 "END", "END-EXEC", "ENFORCE", "ENTRY", "EQUALS", "ERRLVL", "ESCAPE", "ESCAPED", "EVERY", "EXCEPT",  
 "EXCEPTION", "EXCEPTIONS", "EXCHANGE", "EXCLUDING", "EXCLUSIVE", "EXEC", "EXECUTE", "EXISTS", "EXIT",  
 "EXPIRE", "EXPLAIN", "EXTENT", "EXTENTS", "EXTERNAL", "EXTERNALLY", "FAILED\_LOGIN\_ATTEMPTS", "FALSE",  
 "FAST", "FETCH", "FILE", "FILLFACTOR", "FIRST", "FIRST\_ROWS", "FLAGGER", "FLOAT", "FLOAT4", "FLOAT8",  
 "FLOB", "FLUSH", "FOR", "FORCE", "FOREIGN", "FOUND", "FREE", "FREELIST", "FREELISTS", "FREETEXT",  
 "FREETEXTTABLE", "FROM", "FULL", "FULLTEXT", "FUNCTION", "GENERAL", "GET", "GLOBAL", "GLOBALLY",  
 "GLOBAL\_NAME", "GO", "GOTO", "GRANT", "GROUP", "GROUPING", "GROUPS", "HASH", "HASHKEYS", "HAVING",  
 "HEADER", "HEAP", "HIGH\_PRIORITY", "HOLDLOCK", "HOST", "HOUR", "HOUR\_MICROSECOND", "HOUR\_MINUTE",  
 "HOUR\_SECOND", "ID", "IDENTIFIED", "IDENTITY", "IDENTITYCOL", "IDENTITY\_INSERT", "IDGENERATORS",  
 "IDLE\_TIME", "IF", "IGNORE", "IGNORE\_SERVER\_IDS", "IMMEDIATE", "IN", "INCLUDING", "INCREMENT", "INDEX",  
 "INDEXED", "INDEXES", "INDICATOR", "IND\_PARTITION", "INFILE", "INITIAL", "INITIALIZE", "INITIALLY",  
 "INITRANS", "INNER", "INOUT", "INPUT", "INSENSITIVE", "INSERT", "INSTANCE", "INSTANCES", "INSTEAD", "INT",  
 "INT1", "INT2", "INT3", "INT4", "INT8", "INTEGER", "INTERMEDIATE", "INTERSECT", "INTERVAL", "INTO", "IS",  
 "ISOLATION", "ISOLATION\_LEVEL", "ITERATE", "JOIN", "KEEP", "KEY", "KEYS", "KILL", "LABEL", "LANGUAGE",  
 "LARGE", "LAST", "LATERAL", "LAYER", "LEADING", "LEAVE", "LEFT", "LESS", "LEVEL", "LIBRARY", "LIKE",  
 "LIMIT", "LINEAR", "LINENO", "LINES", "LINK", "LIST", "LOAD", "LOB", "LOCAL", "LOCALTIME",  
 "LOCALTIMESTAMP", "LOCATOR", "LOCK", "LOCKED", "LOG", "LOGFILE", "LOGGING", "LOGICAL\_READS\_PER\_CALL",  
 "LOGICAL\_READS\_PER\_SESSION", "LONG", "LONGBLOB", "LONGTEXT", "LOOP", "LOW\_PRIORITY", "MANAGE", "MAP",  
 "MASTER", "MASTER\_HEARTBEAT\_PERIOD", "MASTER\_SSL\_VERIFY\_SERVER\_CERT", "MATCH", "MAX", "MAXARCHLOGS",  
 "MAXDATAFILES", "MAXEXTENTS", "MAXINSTANCES", "MAXLOGFILES", "MAXLOGHISTORY", "MAXLOGMEMBERS", "MAXSIZE",  
 "MAXTRANS", "MAXVALUE", "MEDIUMBLOB", "MEDIUMINT", "MEDIUMTEXT", "MEMBER", "MIDDLEINT", "MIN",  
 "MINEXTENTS", "MINIMUM", "MINUS", "MINUTE", "MINUTE\_MICROSECOND", "MINUTE\_SECOND", "MINVALUE", "MLSLABEL",  
 "MLS\_LABEL\_FORMAT", "MOD", "MODE", "MODIFIES", "MODIFY", "MODULE", "MONTH", "MOUNT", "MOVE",  
 "MTS\_DISPATCHERS", "MULTISET", "NAMES", "NATIONAL", "NATURAL", "NCHAR", "NCHAR\_CS", "NCLOB", "NEEDED",  
 "NESTED", "NETWORK", "NEW", "NEXT", "NO", "NOARCHIVELOG", "NOAUDIT", "NOCACHE", "NOCHECK", "NOCOMPRESS",  
 "NOCYCLE", "NOFORCE", "NOLOGGING", "NOMAXVALUE", "NOMINVALUE", "NONCLUSTERED", "NONE", "NOORDER",  
 "NOOVERRIDE", "NOPARALLEL", "NOREVERSE", "NORMAL", "NOSORT", "NOT", "NOTHING", "NOWAIT",  
 "NO\_WRITE\_TO\_BINLOG", "NULL", "NULLIF", "NUMBER", "NUMERIC", "NVARCHAR2", "OBJECT", "OBJNO", "OBJNO\_REUSE",  
 "OF", "OFF", "OFFLINE", "OFFSETS", "OID", "OIDINDEX", "OLD", "ON", "ONLINE", "ONLY", "OPCODE", "OPEN",  
 "OPENDATASOURCE", "OPENQUERY", "OPENROWSET", "OPENXML", "OPERATION", "OPTIMAL", "OPTIMIZE",  
 "OPTIMIZER\_GOAL", "OPTION", "OPTIONALLY", "OR", "ORDER", "ORDINALITY", "ORGANIZATION", "OSLABEL", "OUT",  
 "OUTER", "OUTFILE", "OUTPUT", "OVER", "OVERFLOW", "OWN", "PACKAGE", "PAD", "PARALLEL", "PARAMETER",  
 "PARAMETERS", "PARTIAL", "PARTITION", "PASSWORD", "PASSWORD\_GRACE\_TIME", "PASSWORD\_LIFE\_TIME",  
 "PASSWORD\_LOCK\_TIME", "PASSWORD\_REUSE\_MAX", "PASSWORD\_REUSE\_TIME", "PASSWORD\_VERIFY\_FUNCTION", "PATH",  
 "PCTFREE", "PCTINCREASE", "PCTTHRESHOLD", "PCTUSED", "PCTVERSION", "PERCENT", "PERMANENT", "PLAN",  
 "PLSQL\_DEBUG", "POSTFIX", "POST\_TRANSACTION", "PRECISION", "PREFIX", "PREORDER", "PREPARE", "PRESERVE",  
 "PRIMARY", "PRINT", "PRIOR", "PRIVATE", "PRIVATE\_SGA", "PRIVILEGE", "PRIVILEGES", "PROC", "PROCEDURE",  
 "PROFILE", "PUBLIC", "PURGE", "QUEUE", "QUOTA", "RAISERROR", "RANGE", "RAW", "RBA", "READ", "READS",  
 "READTEXT", "READUP", "READ\_WRITE", "REAL", "REBUILD", "RECONFIGURE", "RECOVER", "RECOVERABLE", "RECOVERY",  
 "RECURSIVE", "REF", "REFERENCES", "REFERENCING", "REFRESH", "REGEXP", "RELATIVE", "RELEASE", "RENAME",  
 "REPEAT", "REPLACE", "REPLICATION", "REQUIRE", "RESET", "RESETLOGS", "RESIGNAL", "RESIZE", "RESOURCE",  
 "RESTORE", "RESTRICT", "RESTRICTED", "RESULT", "RETURN", "RETURNING", "RETURNS", "REUSE", "REVERSE",  
 "REVOKE", "RIGHT", "RLIKE", "ROLE", "ROLES", "ROLLBACK", "ROLLUP", "ROUTINE", "ROW", "ROWCOUNT",  
 "ROWGUIDCOL", "ROWID", "ROWNUM", "ROWS", "RULE", "SAMPLE", "SAVE", "SAVEPOINT", "SB4", "SCAN\_INSTANCES",  
 "SCHEMA", "SCHEMAS", "SCN", "SCOPE", "SCROLL", "SD\_ALL", "SD\_INHIBIT", "SD\_SHOW", "SEARCH", "SECOND",  
 "SECOND\_MICROSECOND", "SECTION", "SEGMENT", "SEG\_BLOCK", "SEG\_FILE", "SELECT", "SENSITIVE", "SEPARATOR",  
 "SEQUENCE", "SERIALIZABLE", "SESSION", "SESSIONS\_PER\_USER", "SESSION\_CACHED\_CURSORS", "SESSION\_USER",  
 "SET", "SETS", "SETUSER", "SHARE", "SHARED", "SHARED\_POOL", "SHOW", "SHRINK", "SHUTDOWN", "SIGNAL", "SIZE",  
 "SKIP", "SKIP\_UNUSABLE\_INDEXES", "SLOW", "SMALLINT", "SNAPSHOT", "SOME", "SORT", "SPACE", "SPATIAL",  
 "SPECIFIC", "SPECIFICATION", "SPECIFICTYPE", "SPLIT", "SQL", "SQLEXCEPTION", "SQLSTATE", "SQLWARNING",  
 "SQL\_BIG\_RESULT", "SQL\_CALC\_FOUND\_ROWS", "SQL\_SMALL\_RESULT", "SQL\_TRACE", "SSL", "STANDBY", "START",  
 "STARTING", "STATE", "STATEMENT", "STATEMENT\_ID", "STATIC", "STATISTICS", "STOP", "STORAGE", "STORE",  
 "STRAIGHT\_JOIN", "STRUCTURE", "SUCCESSFUL", "SWITCH", "SYNONYM", "SYSDATE", "SYSDBA", "SYSOPER", "SYSTEM",  
 "SYSTEM\_USER", "SYS\_OP\_ENFORCE\_NOT\_NULL$", "SYS\_OP\_NTCIMG$", "TABLE", "TABLES", "TABLESPACE",  
 "TABLESPACE\_NO", "TABNO", "TEMPORARY", "TERMINATE", "TERMINATED", "TEXTSIZE", "THAN", "THE", "THEN",  
 "THREAD", "TIME", "TIMESTAMP", "TIMEZONE\_HOUR", "TIMEZONE\_MINUTE", "TINYBLOB", "TINYINT", "TINYTEXT", "TO",  
 "TOP", "TOPLEVEL", "TRACE", "TRACING", "TRAILING", "TRAN", "TRANSACTION", "TRANSITIONAL", "TRANSLATION",  
 "TREAT", "TRIGGER", "TRIGGERS", "TRUE", "TRUNCATE", "TSEQUAL", "TX", "TYPE", "UB2", "UBA", "UID",  
 "UNARCHIVED", "UNDER", "UNDO", "UNION", "UNIQUE", "UNKNOWN", "UNLIMITED", "UNLOCK", "UNNEST",  
 "UNRECOVERABLE", "UNSIGNED", "UNTIL", "UNUSABLE", "UNUSED", "UPDATABLE", "UPDATE", "UPDATETEXT", "USAGE",  
 "USE", "USER", "USING", "UTC\_DATE", "UTC\_TIME", "UTC\_TIMESTAMP", "VALIDATE", "VALIDATION", "VALUE",  
 "VALUES", "VARBINARY", "VARCHAR", "VARCHAR2", "VARCHARACTER", "VARIABLE", "VARYING", "VIEW", "WAITFOR",  
 "WHEN", "WHENEVER", "WHERE", "WHILE", "WITH", "WITHOUT", "WORK", "WRITE", "WRITEDOWN", "WRITETEXT",  
 "WRITEUP", "XID", "XOR", "YEAR", "YEAR\_MONTH", "ZEROFILL", "ZONE"

### Tipos de campos e imutabilidade

---

Independente da quantidade de versões de um formulário, sempre é utilizada a mesma tabela. Assim, em um formulário com 50 versões, terão registros de formulários, possivelmente, das 50 versões do formulário.

Por esta razão, uma vez criado um campo este campo não é mais modificado nem removido.

Então, mesmo com valores pequenos como um checkbox, radio ou select, são criados como um campo texto armazenamento grande, porque, por mais que nesta versão eles são apenas um select, nada impede que no futuro ele se torne um text area.

Sendo assim, todos os campos do formulário fluig possuem um limite de 4000 caracteres.

### Quantidade de campos por formulário

---

Como já falado, cada campo do formulário vira uma coluna. Isso acaba esbarrando em duas outras limitações: Quantidade de campos por linha e tamanho da linha. A primeira, que seria de 1000 campos, acaba não sendo atingido pela segunda limitação: Tamanho da linha. Esse limite é em torno de 400 campos dependendo do banco de dados e versão. Por mais que o seu formulário não tenha essa quantidade no momento, pode ser que em outras versões houvessem outros campos que estão ocupando espaço na tabela e impedindo a criação de novos campos

## Numa única tabela (para pequenas quantidades de registros)

---

Um formulário configurado para armazenar seus dados em tabela única terá as informações de cada registro gravadas na tabela FICHA do banco de dados. Por acumular muitos registros rapidamente, dependendo do fluxo de uso dos formulários e das solicitações que os utilizam, esse modelo é pouco eficiente e **não é recomendado** para a construção de formulários atualmente, sendo mantido seu suporte para situações específicas e para manter formulários importados de versões anteriores. Quando se utiliza formulários pai x filho, também não é recomendado a configuração para utilização de tabela única, pois o filtro de registros *(query constrains)* não trará como resultado os registros do formulário filho.
