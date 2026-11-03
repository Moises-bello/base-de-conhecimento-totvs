---
article_id: 360021851532
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 846f31899455c48a6de95fb7ec05d1e9c100dfd3a9637d3335342f96bf37892e
fetched_at: '2026-06-28T22:42:08.862877+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Error log
  DCTF Incorrect syntax near ''‘''.'
type: support-article
updated_at: '2024-06-13T19:26:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021851532--Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Error-log-DCTF-Incorrect-syntax-near
---

**Ocorrência**Ao gerar o arquivo da DCTF ocorre o error log abaixo, relacionado a uma query:  
  
THREAD ERROR ([11076], totvsservice, NEOTSMAS007) 16/01/2019 11:17:09  
: Error : 102 (37000) (RC=-1) - [Microsoft][ODBC SQL Server Driver][SQL Server]Incorrect syntax near '‘'.  
( From tMSSQLConnection::GetQueryFile )  
Thread ID [3832] User [Administrador] IO [391] Tables [18] MaxTables [18] Comment [MATA978 - TCPIP - ThreadID(11076)] SP [ ] Traced [No] SQLReplay [No] InTran [No] DBEnv [MSSQL/FPTVT] DBThread [(SPID 197,198)] Started [16/01/2019 11:15:48] IP [172.22.209.9:7025] IDLE [ ] InTransact [ ] Memory [345728] Running [ROP\_QUERY] RCV [11915] SND [42513] TCBuild [20180606-20180904] TCVersion [18.1.1.3] ARCH [64] OS [WINDOWS] BUILD [RELEASE]   
SELECT E2\_FILIAL,E2\_PREFIXO,E2\_NUM,E2\_PARCELA,E2\_TIPO,E2\_NATUREZ,E2\_FORNECE,E2\_LOJA,E2\_VALOR,E2\_EMISSAO,E2\_VENCREA,E2\_CODRET,E2\_PARCSLL,E2\_PARCPIS,E2\_PARCCOF,E2\_PARCIR,E2\_EMIS1,E2\_IRRF,E2\_PIS,E2\_COFINS,E2\_CSLL,E2\_CODAGL,E2\_PERIOD,E2\_VARIAC,E2\_DIRF,E2\_FILORIG,E2\_ORIGEM,E2\_BAIXA,SA2.A2\_TIPO,SA2.A2\_CALCIRF,E2\_NUMPRO,E2\_INDPRO,E2\_MULTA,E2\_JUROS,E2\_PARCCID,E2\_CIDE,E2\_IDDARF,E2\_DATASUS FROM SE2010 SE2 LEFT JOIN SA2010 SA2 ON(SA2.A2\_FILIAL= ' ' AND SA2.A2\_COD=SE2.E2\_FORNECE AND SA2.A2\_LOJA=SE2.E2\_LOJA AND SA2.D\_E\_L\_E\_T\_= ' ') WHERE SE2.D\_E\_L\_E\_T\_= ' ' AND E2\_FILIAL='01' AND (E2\_CODRET NOT IN (' ') OR (E2\_PARCELA IN('0',' ') OR(E2\_PARCELA IN ('0',' ') AND (E2\_BAIXA=' ' OR E2\_BAIXA <= '20190131')) AND E2\_TIPO='TX ')) AND ((E2\_TIPO IN(‘NFE’,’TX’,’NCI’,‘NFS'’) AND ( ( (( E2\_IRRF>0 OR E2\_CODRET <> '' ) AND (E2\_VENCREA>='20190101' AND E2\_VENCREA<='20190131') OR (E2\_BAIXA BETWEEN '20190101' AND '20190131' AND SA2.A2\_CALCIRF='2')) ) ) ) OR ( ( (E2\_TIPO='TX ' OR E2\_TIPO='TXA') OR (E2\_TIPO='DP ' AND E2\_ORIGEM='MATA996 ' OR E2\_ORIGEM='FISA001 ') ) AND E2\_PREFIXO <> 'AGP' AND E2\_PREFIXO <> 'AGL' AND E2\_NATUREZ <> '' AND E2\_FORNECE= 'UNIAO ' AND E2\_LOJA= '00' AND E2\_EMISSAO>= '20190101' AND E2\_EMISSAO<= '20190131' AND ( E2\_NATUREZ IN('IPI ') OR (E2\_NATUREZ IN('IRF ') AND E2\_ORIGEM NOT IN('MATA100')) OR (E2\_NATUREZ IN('CSLL ') AND E2\_ORIGEM NOT IN('MATA100')) OR (E2\_NATUREZ IN('"PIS" ') AND E2\_ORIGEM NOT IN('MATA100')) OR (E2\_NATUREZ on \_\_EXECSQL(APLIB300.PRW) 31/08/2018 13:40:09 line : 134

**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80  
  
**Causa**Este error log ocorre pois o parâmetro **MV\_TPTITU** foi preenchido de forma incorreta, possivelmente pelo fato do conteúdo ter sido copiado de algum outro lugar e colocado no parâmetro, onde a aspa simples utilizada está diferente do padrão suportada pela query que o Protheus realiza.  
  
**Solução**Para correção do problema é necessário rescrever o parâmetro **manualmente**para que as aspas simples sejam colocadas de maneira correta no arquivo.  
  
Exemplo:  
'NF','TX','FOL'
