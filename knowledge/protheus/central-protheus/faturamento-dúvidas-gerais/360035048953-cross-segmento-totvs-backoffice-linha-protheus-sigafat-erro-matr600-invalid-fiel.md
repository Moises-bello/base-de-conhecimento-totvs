---
article_id: 360035048953
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: efe59d8fea4fe739253993b0d2e820a31441b394ecf946427777e26cb9a22a30
fetched_at: '2026-06-28T22:38:28.462069+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) -  SIGAFAT - ERRO MATR600
  - Invalid Field Order in Query - Memo fields must be grouped at the end of the Query
type: support-article
updated_at: '2023-01-30T18:05:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035048953-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-ERRO-MATR600-Invalid-Field-Order-in-Query-Memo-fields-must-be-grouped-at-the-end-of-the-Query
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:04:00 min****Ocorrência**Ao tentar gerar o relatório **MATR600**, ocorre o erro;

*TOP Error -19 - **Invalid Field Order in Query -- Memo fields must be grouped at the end of the Query.** ( From tODBCStatement::BindCols )*  
*Thread ID [43716] User [ana] IO [383] Tables [17] MaxTables [17] Comment [**MATR600** - TCPIP - ThreadID(93768)] SP [ ] Traced [No] SQLReplay [No] InTran [No] DBEnv [MSSQL/CMTTWK] DBThread [(SPID 369,634)] Started [16/08/2019 16:38:01] IP [127.0.0.1:12871] IDLE [ ] InTransact [ ] Memory [369464] Running [ROP\_QUERY] RCV [11005] SND [30733] TCBuild [20180606-20181019] TCVersion [18.1.1.4] ARCH [64] OS [WINDOWS] BUILD [RELEASE]*   
*on \_\_EXECSQL(APLIB300.PRW) 10/04/2019 14:27:47 line : 149*

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FAT - a partir da release 12.1.17  
  
**Causa**O erro ocorre ao acionar a opção de impressão do cadastro onde ,o cadastro que possui algum campo memo, gerando error.log em ambientes com dicionário no banco de dados.

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

**1.** Efetue download da última **LIB** disponível no portal para o seu ambiente:

**[Ambiente 32 Português](https://suporte.totvs.com/portal/p/10098/download?e=914679)**

**[Ambiente Lobo Português](https://suporte.totvs.com/portal/p/10098/download?e=914676)**

e aplique ao RPO do ambiente via TDS - Totvs developer Studio ou o antigo IDE.

**Obs**: Lembrando que para 12.1.17 e anteriores, o pacote de lib é sempre nomeado como: *LIB\_P12 - TOPCONNECT - 32*  
E para as releases da 12.1.23 em diante, a lib é nomeada como: *LIB\_P12 - TOPCONNECT - Lobo.*

**2.** Efetue download do último **Dbacess** conforme o seu ambiente, e faça atualização do mesmo: **[Downloads e Atualizações Dbaccess](https://suporte.totvs.com/portal/p/10098/download?e=763291#000006/368/TFDBA/search/searchAll)**

**3.** Reinicie o smartclient e refaça o processo.

**Obs**: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.
