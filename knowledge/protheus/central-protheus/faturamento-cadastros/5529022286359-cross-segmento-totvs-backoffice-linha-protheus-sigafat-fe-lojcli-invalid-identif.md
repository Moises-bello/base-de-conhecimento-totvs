---
article_id: 5529022286359
category: Faturamento - Cadastros
content_hash: a54b3f935d5ff6810d40b484301d608340ab099e13f85c9ec7c36812d110b969
fetched_at: '2026-06-28T22:38:35.357200+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat- "FE_LOJCLI":
  invalid identifier'
type: support-article
updated_at: '2022-04-19T13:42:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5529022286359-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-FE-LOJCLI-invalid-identifier
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**

Ao excluir um cliente na rotina nova CRMA980 mas está ocorrendo o error log abaixo.

THREAD ERROR ([17281], sergios, TI-N20) 31/03/2022 13:42:16  
**SCGN0003EE: Error : 904 - ORA-00904: "FE\_LOJCLI": invalid identifier**  
( From tOracleConnection::GetQueryFile )  
Thread ID [17359] User [sergios] IO [4434] Tables [55] MaxTables [56] Comment [CRMA980 - TCPIP - ThreadID(17281)] SP [ ] Traced [No] SQLReplay [No] InTran [No] DBEnv [ORACLE/PROT12] DBThread [(SID 587,34837,1)] Started [31/03/2022 13:40:36] IP [192.168.0.86:10017] IDLE [ ] InTransact [ ] Memory [0] Running [ROP\_QUERY for 0 s.] RCV [292395] SND [815666] TCBuild [20210202-20210930] TCVersion [21.1.1.0] ARCH [64] OS [LINUX] BUILD [RELEASE]  
SELECT 1 REG FROM SA1010 DOM WHERE A1\_FILIAL = ' ' AND A1\_COD = '178494' AND A1\_LOJA = '01' AND EXISTS (SELECT 1 FROM SFE010 CDOM WHERE FE\_FILIAL <> ' ' AND FE\_CLIENTE = '178494' AND FE\_LOJCLI = '01' AND CDOM.D\_E\_L\_E\_T\_ = ' ' ) on FWESX9EXEC(FWEVALSX9.PRW) 30/12/2021 15:45:47 line : 514

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat-  12.1.27 em diante  
  
**Causa**

A tabela SFE tem relacionamento com a tabela SA1 através do campo A1\_COD + A1\_LOJA, dentro da tabela de relacionamentos SX9.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5528677035799/mceclip0.png)

O erro ocorre por que no momento migração de release, o campo **FE\_LOJCLI** não foi criado no dicionário de dados (SX3) e banco de dados, ocasionando o erro, na comparação de tabelas demonstrada no select:

**SELECT 1 REG FROM SA1010** DOM WHERE A1\_FILIAL = ' ' AND **A1\_COD = '178494'** AND **A1\_LOJA = '01**' AND EXISTS (S**ELECT 1 FROM SFE010** CDOM WHERE FE\_FILIAL <> ' ' AND **FE\_CLIENTE = '178494'** AND **FE\_LOJCLI = '01'** AND CDOM.D\_E\_L\_E\_T\_ = ' ' ) on FWESX9EXEC

**Solução**

Para solucionar essa ocorrência, efetue o download novamente do dicionário de dados relacionado a sua release de migração no portal do cliente (<https://suporte.totvs.com/portal/p/10098/download#000006/>) e rode o updistr para que o campo seja criado de forma correta.

A tabela SFE é relacionada a retenção de impostos.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5528901715479/mceclip1.png)
