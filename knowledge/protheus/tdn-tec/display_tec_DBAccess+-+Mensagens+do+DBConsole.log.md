---
content_hash: 66ba8c66dc11a1bec3ccf310f9bf8cc0afefd141e4aab7feae05c0be6955c5e0
fetched_at: '2026-07-02T19:24:20.571539+00:00'
page_id: '258835222'
product: protheus
source: tdn-tec
title: DBAccess - Mensagens do DBConsole.log
type: documentation
url: https://tdn.totvs.com/display/tec/DBAccess+-+Mensagens+do+DBConsole.log
version: 8
---

O arquivo **dbconsole.log**, gerado automaticamente pelo true, contém informações sobre a inicialização e finalização do DBAccess, entrada e saída de conexões, entre outras informações sobre a execução de processos internos e informações adicionais para fins de diagnóstico.

Abaixo, alguns exemplos de informações gravadas neste arquivo, e o seu significado.

## Thread (<thread>) disconnected prematurely! (RECEIVEBLOCK)

true

## Begin TopClient Thread (<dbaccess-thread-id>,<appserver-ip>,<database>/<datasource-name>,<user-logged-os/renamed-user-protheus>,<user-logged-os>,<hostname>,DBApi <from-dbapi-version>)

true

## End TopClient Thread (<dbaccess-thread-id>) (IOs <io-count> / RCV <received-bytes> / SND <sent-bytes> )

true

## Exit TopClient Thread (<dbaccess-thread-id>) [TERMINATED] (IOs <io-count> / RCV <received-bytes> / SND <sent-bytes> )

true

## Exit with active transaction

true

## Formato de mensagem de erro padrão

Uma ocorrência de erro registrada no DBAccess, por consequência de um erro retornado pelo SGDB, é registrada no log de console (dbconsole.log) e no log de erros (dbaccess.log) no seguinte formato:

 () (RC= ) -  ( From  )
Thread ID [] User [] IO [] Tables [] MaxTables []
Comment [] Status [] SP [ ] Traced [] InTran []
DBEnv [/] DBThread [] Started [] LastIO [] IP []
RCV [] SND [] TCBuild []
[ OPERATION\_DETAILS ]]]>

Uma ocorrência de execução com sucesso, porém houveram informações adicionais relacionadas a execução, é registrada pelo DBAccess como uma ocorrência de advertência. Contém todos os dados da ocorrência de erro, mas é iniciada com "Warning :" ao invés de "Error :".

Na ocorrência acima, o Bando de Dados DB2 apenas informa que, para acrescentar a chave primária de registro em uma tabela, foi usado um índice já existente que atendia a condição, e não foi criado um índice novo. Este comportamento é o esperado, o índice de chave primária é criado em um momento anterior com uma parametrização específica.

Na ocorrência acima, uma aplicação Advpl tentou remover um flag de deleção lógica de um registro, porém o SGDB MSSQL utilizado não permitiu a remoção, pois isto violatia a chave única definida para a tabela em questão.

A ocorrência acima é praticamente a mesma da anterior – violação de índice de chave única – porém registrada pelo SGDB DB2.

## Informações de Check-Up na Primeira Conexão

Após subir o serviço do DBAccess, a primeira conexão feita com um Banco de Dados, registra no log de console várias informações sobre o SGDB em questão. Estas informações podem variar entre os tipos de bancos de dados homologados, segue abaixo o exemplo das informações coletadas da conexão com um Banco de Dados MSSQL:

 (Build 7601: Service Pack 1)
SQL ServerName: TST-DATA279\SQLINST1
SQL Collation.: Latin1\_General\_BIN
SQL Edition...: Enterprise Edition (64-bit)
SQL Version...: 10.50.6000.34
SQL P.Level...: SP3
MARS .........: ENABLED
-----------------------------------------------------------
--------------- ODBC Connection Check-Up ------------------
ODBC Mapped Functions ......: 1.0
ODBC DBMS Name..............: Microsoft SQL Server
ODBC DBMS Version...........: 10.50.6000
ODBC DBMS Database Name.....: P12TST
ODBC Data Source Name.......: P12TST
ODBC Server Name............: TST-P12\SQLINST1
ODBC Driver Name............: sqlncli10.dll
ODBC Driver Version ........: 10.50.4000
ODBC Support ODBC Version...: 03.52
-----------------------------------------------------------
------------- Generic Connection Check-Up -----------------
Prepared Stmt Cache .......: ENABLED
Index Trace ...............: DISABLED
ISAM Compatibility Mode ...: ENABLED
Connection Access Mode ....: READWRITE (DEFAULT)
ISAM DefaultRowCount ......: 40
ISAM FilteredRowCount .....: 250
DB Unified Connection .....: DISABLED (LEGACY)
Record Sequence Owner .....: DBACCESS (DEFAULT)
-----------------------------------------------------------]]>

## Table <table-name> has <numeric-field-count> numeric fields on DBMS, but <numeric-field-adjusted> was adjusted using TOP\_FIELD

true
