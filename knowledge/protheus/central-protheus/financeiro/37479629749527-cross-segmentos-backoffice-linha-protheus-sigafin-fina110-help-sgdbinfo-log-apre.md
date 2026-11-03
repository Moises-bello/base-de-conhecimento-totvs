---
article_id: 37479629749527
category: Financeiro
content_hash: 69c7ba4818c64c60a658e09919846a4a3e965d5f3d2197a6bf0c3ec6e4a44802
fetched_at: '2026-06-28T22:38:02.987793+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA110 - Help: SGDBINFO.
  Log apresentando ORA-00932: inconsistent datatypes: expected BLOB got CLOB'
type: support-article
updated_at: '2026-01-12T14:22:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37479629749527-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA110-Help-SGDBINFO-Log-apresentando-ORA-00932-inconsistent-datatypes-expected-BLOB-got-CLOB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37479582323735) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
FINA110 - Ao efetuar uma baixa automática a receber apresentando em tela Help: SGDBINFO, e ao abrir o log apresentando o erro "ORA-00932: inconsistent datatypes: expected BLOB got CLOB"

**Ambiente**  
Exemplo:  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro  - Todas as versões

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/37479795638551)](https://centraldeatendimento.totvs.com/hc/article_attachments/37479795638551)

**Erro dentro do log FR100LOG.log :**

01:40:00 [2920152] Function F110TOTRB Line 4424  
    [TEMPORARIA\_TITULOS] Error : 932 - **ORA-00932: inconsistent datatypes: expected BLOB got CLOB**  
( From tDBServer::ROP\_SQLEXEC )  
Thread ID [1332323]    User [Administrador]    IO [4344]    Tables [44]    MaxTables [70]    Comment [FINA110 - TCPIP - ThreadID(1332323)]    SP [ ]    Traced [No]    SQLReplay [No]    InTran [No]    Totvs [ORACLE/TOTVS\_DB]    DBThread [(SID 33,322,22)]    Started [04/01/2021]    IP [11.0.0.0]    IDLE [ ]    InTransact [ ]    Memory [0]    Running [ROP\_SQLEXEC for 0 s.]    RCV [323232]    SND [53134]    TCBuild [20240221-20250921]    TCVersion [24.1.1.0]    ARCH [64]    OS [LINUX]    BUILD [RELEASE]      
INSERT INTO TSC02\_33730731 ( E1\_FILIAL, E1\_PREFIXO, E1\_NUM, E1\_PARCELA, E1\_TIPO, E1\_NATUREZ, E1\_PORTADO, E1\_AGEDEP, E1\_NOMCLI, E1\_EMISSAO, E1\_VENCTO, E1\_VENCREA, E1\_VALOR, E1\_BASEIRF, E1\_ISS, E1\_IRRF, E1\_NUMBCO, E1\_INDICE, E1\_BAIXA, E1\_NUMBOR, E1\_DATABOR, E1\_EMIS1, E1\_HIST, E1\_LA, E1\_LOTE, E1\_MOTIVO, E1\_MOVIMEN, E1\_OP, E1\_SITUACA, E1\_CONTRAT, E1\_SALDO, E1\_SUPERVI, E1\_VEND1, E1\_VEND2, E1\_VEND3, E1\_VEND4, E1\_VEND5, E1\_COMIS1, E1\_COMIS2, E1\_COMIS3, E1\_COMIS4, E1\_DESCONT, E1\_COMIS5, E1\_MULTA, E1\_JUROS, E1\_CORREC, E1\_VALLIQ, E1\_VENCORI, E1\_CONTA, E1\_VALJUR, E1\_PORCJUR, E1\_MOEDA, E1\_BASCOM1, E1\_BASCOM2, E1\_BASCOM3, E1\_BASCOM4, E1\_BASCOM5, E1\_FATPREF, E1\_FATURA, E1\_OK, E1\_PROJETO, E1\_CLASCON, E1\_VALCOM1, E1\_VALCOM2, E1\_VALCOM3, E1\_VALCOM4, E1\_VALCOM5, E1\_OCORREN, E1\_INSTR1, E1\_INSTR2, E1\_PEDIDO, E1\_DTVARIA, E1\_VARURV, E1\_VLCRUZ, E1\_DTFATUR, E1\_NUMNOTA, E1\_SERIE, E1\_STATUS, E1\_ORIGEM, E1\_IDENTEE, E1\_NUMCART, E1\_FLUXO, E1\_DESCFIN, E1\_DIADESC, E1\_TIPODES, E1\_CARTAO, E1\_CARTVAL, E1\_CARTAUT, E1\_ADM, E1\_VLRREAL, E1\_TRANSF, E1\_BCOCHQ, E1\_AGECHQ, E1\_CTACHQ, E1\_NUMLIQ, E1\_ORDPAGO, E1\_RECIBO, E1\_INSS, E1\_FILORIG, E1\_DTACRED, E1\_TIPOFAT, E1\_TIPOLIQ, E1\_CSLL, E1\_COFINS, E1\_PIS, E1\_FLAGFAT, E1\_MESBASE, E1\_ANOBASE, E1\_PLNUCOB, E1\_CODINT, E1\_CODEMP, E1\_MATRIC, E1\_TXMOEDA, E1\_ACRESC, E1\_SDACRES, E1\_DECRESC, E1\_SDDECRE, E1\_MULTNAT, E1\_MSFIL, E1\_MSEMP, E1\_PROJPMS, E1\_DESDOBR, E1\_NRDOC, E1\_EMITCHQ, E1\_MODSPB, E1\_IDCNAB, E1\_PLCOEMP, E1\_PLTPCOE, E1\_CODCOR, E1\_PARCCSS, E1\_CODORCA, E1\_CODIM  
02:08:12 [2933220] Function F110TOTRB Line 4424

**Solução:**

No caso do exemplo acima, caso na tabela SE1 esteja configurado como E2\_CLOB = 2 não

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37611167257879)

Caso a empresa possua nos campos **customizados** da tabela SE1 com os dois tipos, CLOB e BLOB, irá apresentar o erro.

Ou caso na SX2 esteja definido como X2\_CLOB = 2 não, e na tabela SE1 tenha campos com o tipo CLOB, irá apresentar o erro

Exemplo

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/37479582324887)](https://centraldeatendimento.totvs.com/hc/article_attachments/37479582324887)

(Na imagem abaixo o modo correto conforme a SX2 da tabela SE1)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37611231847191)

Poderá executar o select de exemplo abaixo no banco de dados oracle para identificar se existe algum campo **DATA\_TYPE = BLOB junto com CLOB**

SELECT COLUMN\_NAME, DATA\_TYPE  
FROM USER\_TAB\_COLUMNS  
WHERE TABLE\_NAME = 'SE1010' AND  
DATA\_TYPE IN ('CLOB','BLOB')

Caso tenha dúvida para efetuar esse tipo de alteração, sugerimos um DBA para realizar o ajuste ou poderá verificar a possibilidade de excluir o campo customizado e inclui-lo com o tipo correto com o tipo BLOB,  primeiramente faça em base de teste e faça as validações

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/37480691378071)](https://tdn.totvs.com/pages/releaseview.action?pageId=22479521)

Os campos memos quando utilizados em ambiente com TOPCONECT, portanto, banco de dados relacionais, podem utilizar 2 tipos de campos: BLOB ou CLOB. O padrão de criação do tipo de memo é definido pelo SX2, no campo **X2\_MEMTYPE**.

O padrão do sistema é o BLOB, que cria campos binários, caso for definido a utilização de CLOB o campo será criado como um caractere especial dependendo do banco. Se utilizado BLOB não é permitido utilizar o campo em índice e filtros.

**Saiba mais:**

 - [FWTemporaryTable](https://tdn.totvs.com/display/public/framework/FWTemporaryTable)  
 - [X2\_MEMTYPE - Determina se o campo memo das tabelas será armazenado no banco de dados como BLOB ou CLOB. Caso esteja em branco ou com “1” será BLOB, caso esteja com “2” – CLOB.](https://tdn.totvs.com/display/public/framework/SX2+-+Tabelas+de+Dados)

 - [Tipos de dados - Dicionário de Dados](https://tdn.totvs.com/pages/releaseview.action?pageId=22479521)

[- DFRM4-6950 DT Campo MEMO tipo BLOB com X2\_CLOB = 1](https://tdn.totvs.com/display/public/framework/DFRM4-6950+DT+Campo+MEMO+tipo+BLOB+com+X2_CLOB+%3D+1)

[- JUR0095\_Configuração O1A com X2\_CLOB ativado](https://tdn.totvs.com/pages/releaseview.action?pageId=874588225)
