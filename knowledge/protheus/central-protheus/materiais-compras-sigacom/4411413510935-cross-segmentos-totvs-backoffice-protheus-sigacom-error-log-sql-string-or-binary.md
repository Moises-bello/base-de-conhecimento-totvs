---
article_id: 4411413510935
category: Materiais - Compras (SIGACOM)
content_hash: 672a4fc22a1aeeec5cae4a2841eef41488f8fa37e529c97ecb5564313be566d3
fetched_at: '2026-06-28T22:41:17.648046+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Error Log SQL " String
  or binary data would be truncated. " na inclusão do Documento de Entrada no release
  12.1.33
type: support-article
updated_at: '2022-10-26T13:58:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411413510935-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Error-Log-SQL-String-or-binary-data-would-be-truncated-na-inclus%C3%A3o-do-Documento-de-Entrada-no-release-12-1-33
---

**Dúvida**

Na inclusão de um documento de entrada no release 33, o sistema gera error log na tabela MP\_CUSTOM\_METRICS\_EXP.

*[FWCustomMetrics:InsertMetric] TCSQLError(): Error : 8152 (22001) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]String or binary data would be truncated.*

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM Compras  - 12.1.33  
  
**Solução**

*Informações do Erro:*

[FWCustomMetrics:InsertMetric] TCSQLError(): Error : 8152 (22001) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]String or binary data would be truncated.  
( From tDBServer::ROP\_SQLEXEC )  
Thread ID [9616] User [Administrador] IO [21526] Tables [213] MaxTables [214] Comment [MATA103 - TCPIP - ThreadID(11784)] SP [ ] Traced [No] SQLReplay [No] InTran [Yes] DBEnv [MSSQL/PROTHEUS12133MIGRA] DBThread [(SPID 63,66,129)] Started [11/10/2021 19:52:19] IP [10.70.0.4:1240] IDLE [ ] InTransact [3 s.] Memory [0] Running [ROP\_SQLEXEC for 0 s.] RCV [877299] SND [5480736] TCBuild [20210202-20210930] TCVersion [21.1.1.0] ARCH [64] OS [WINDOWS] BUILD [RELEASE]  
INSERT INTO MP\_CUSTOM\_METRICS\_EXP (MP\_FEDERID, MP\_MODULO, MP\_ROTINA, MP\_USER, MP\_SUBROT, MP\_IDMETRI, MP\_VALUE, MP\_LAPTIME, MP\_DTCREAT, MP\_DTSEND, MP\_TPMETRI) VALUES ('08845775000170', 2, 'mata103', '000000', 'mata103-inc-tela-inc- -average', 'media-itens-notas-fiscais-entrada', '1', 0, '20211011', '20211029', 'AVG') on INSERTMETRIC(FWCUSTOMMETRICS.TLPP) 06/10/2021 13:57:35 line : 472

Nesta parte do erro, temos que : **Error : 8152 (22001) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]String or binary data would be truncated,** o mesmo é gerado no banco de dados e replicado pelo DBAccess,  ocorre quando um valor está tentando ser inserido ou atualizado na *Statement*  em uma tabela e ele é maior que o tamanho máximo do campo.

E nesta parte do erro :

**Thread ID [9616] User [Administrador] IO [21526] Tables [213] MaxTables [214] Comment [MATA103 - TCPIP - ThreadID(11784)] SP [ ] Traced [No] SQLReplay [No] InTran [Yes] DBEnv [MSSQL/PROTHEUS12133MIGRA] DBThread [(SPID 63,66,129)] Started [11/10/2021 19:52:19] IP [10.70.0.4:1240] IDLE [ ] InTransact [3 s.] Memory [0] Running [ROP\_SQLEXEC for 0 s.] RCV [877299] SND [5480736] TCBuild [20210202-20210930] TCVersion [21.1.1.0] ARCH [64] OS [WINDOWS] BUILD [RELEASE]**  
**INSERT INTO MP\_CUSTOM\_METRICS\_EXP (MP\_FEDERID, MP\_MODULO, MP\_ROTINA, MP\_USER, MP\_SUBROT, MP\_IDMETRI, MP\_VALUE, MP\_LAPTIME, MP\_DTCREAT, MP\_DTSEND, MP\_TPMETRI) VALUES ('08845775000170', 2, 'mata103', '000000', 'mata103-inc-tela-inc- -average', 'media-itens-notas-fiscais-entrada', '1', 0, '20211011', '20211029', 'AVG') on INSERTMETRIC(FWCUSTOMMETRICS.TLPP) 06/10/2021 13:57:35 line : 472**

Na análise do error.log constatamos que a variável ***cTipo*** estava sendo **gravada com espaços em branco**, e ao concatenar com outras variáveis para gravar a ***variável cSubRoutine***, referente a métrica de dados da rotina Documento de Entrada, gerava o error.log por conta do tamanho da string maior que o tamanho do campo **MP\_SUBROT**.

A***cTipo* é uma variável *Private* do fonte MATA103**, porém há pontos de entrada que podem alterá-la para " " o que altera o processo padrão também.  
Com a implementação da métrica, o programa espera que a *cTipo* entregue o tipo da nota fiscal (N, B, C, D) , qualquer informação diferente disso ocarionará a geração do erro em questão  
Vale ressaltar que em outros releases esse erro não ocorria, pois a variável após ser alterada por Pontos de Entrada não era chamada pelo programa padrão, mas com a evolução de persistir métricas no final da gravação da nota precisaremos que a variável *cTipo* esteja consistente conforme a finalidade da mesma.

Nesse cenário sugerimos avaliar os Pontos de entrada usados na MATA103 para tentar localizar qual está gerando a gravação de espaços em branco na variável cTipo.

***Saiba Mais :***

*[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)*

*[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)*
