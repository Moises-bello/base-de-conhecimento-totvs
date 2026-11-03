---
article_id: 360034576914
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: dcf8f739f2f0b373427c57b73bf2cb97dafff70770a59321b3f589450becdb29
fetched_at: '2026-06-28T22:38:30.080025+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'Cross Segmentos- TOTVS Backoffice (Linha Protheus)-SIGAFAT  -ORA-00942: table
  or view does not exist'
type: support-article
updated_at: '2021-09-03T14:26:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034576914-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-ORA-00942-table-or-view-does-not-exist
---

**Ocorrência**

Ao excluir um cliente (MATA030) sem movimentação, gera o erro:

: Error : 942 - ORA-00942: **table or view does not exist**  
  
**Ambiente**

Cross Segmentos- TOTVS Backoffice (Linha Protheus)-SIGAFAT - a partir da release 12.1.17.  
  
**Causa**

Cabeçalho completo do erro:

**Error : 942 - ORA-00942: table or view does not exist  
( From tOracleConnection::GetQueryFile )  
Thread ID [5510] User [MARCELO VICENTE] IO [1369] Tables [41] MaxTables [41] Comment [MATA030 - TCPIP - ThreadID(5525)] SP [ ] Traced [Yes] SQLReplay [No] InTran [No] DBEnv [ORACLE/ODBP12] DBThread [(SID 2739,37551,1)] Started [28/08/2019 11:36:21] IP [10.0.0.253:7100] IDLE [ ] InTransact [ ] Memory [1125144] Running [ROP\_QUERY] RCV [259684] SND [1181953] TCBuild [20181212-20190211] TCVersion [18.2.1.0] ARCH [64] OS [LINUX] BUILD [RELEASE]   
SELECT AC8.AC8\_CODENT FROM AC8010 AC8 WHERE AC8.AC8\_FILIAL = ' ' AND AC8.AC8\_ENTIDA = 'SA1' AND AC8.AC8\_FILENT = ' ' AND AC8.AC8\_CODENT = 'FUN4B301' AND EXISTS(SELECT ADE.ADE\_CHAVE FROM ADET10 ADE WHERE ADE.ADE\_FILIAL = '01' AND ADE.ADE\_CODCON = AC8.AC8\_CODCON AND ADE.ADE\_ENTIDA = AC8.AC8\_ENTIDA AND ADE.ADE\_CHAVE = AC8.AC8\_CODENT AND ADE.D\_E\_L\_E\_T\_= ' ' ) AND AC8.D\_E\_L\_E\_T\_= ' ' on \_\_EXECSQL(APLIB300.PRW) 15/02/2019 09:10:59 line : 134**

O erro ocorre por que na query da função **Tk510TAxEn**, o nome da tabela ADE estava codificada com filial, **ADET10**.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Efetue o download do pacote **TMKA510**, e acordo com a release do seu ambiente:

12.1.25:<https://suporte.totvs.com/portal/p/10098/download?e=777123> ; 12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=777122> ; 12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=777121> ;

2. Atualize o RPO com o pacote em questão via TDS - Totvs Developer Studio ou antigo IDE.

3. Reinicie o Smartclient e efetue o processo novamente.

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
