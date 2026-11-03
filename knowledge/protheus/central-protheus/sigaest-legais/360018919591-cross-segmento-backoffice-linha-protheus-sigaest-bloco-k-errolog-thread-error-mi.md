---
article_id: 360018919591
category: SIGAEST - LEGAIS
content_hash: 33ed4a5f652321133a0286cb6a72102cc81c1edba7ff84ee8682cf60d05464cb
fetched_at: '2026-06-28T22:38:51.439015+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - BLOCO K - ERROLOG
  THREAD ERROR [Microsoft][SQL Server Native Client 10.0][SQL Server]Invalid column
  name 
type: support-article
updated_at: '2023-02-01T20:02:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018919591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-BLOCO-K-ERROLOG-THREAD-ERROR-Microsoft-SQL-Server-Native-Client-10-0-SQL-Server-Invalid-column-name
---

Tempo aproximado para leitura:**00:01:50 min**

**Ocorrência**

No módulo **Estoque-Custos**, ao tentar realizar a extração do BLOCO K  é apresentado o error.log

THREAD ERROR [Microsoft][SQL Server Native Client 10.0][SQL Server]Invalid column name

Error : 207 (S0022) (RC=-1) - [Microsoft][ODBC Driver 11 for SQL Server][SQL Server]Nome de coluna 'OI' inválido.  
Error : 207 (S0022) (RC=-1) - [Microsoft][ODBC Driver 11 for SQL Server][SQL Server]Nome de coluna 'PI' inválido.  
Error : 207 (S0022) (RC=-1) - [Microsoft][ODBC Driver 11 for SQL Server][SQL Server]Nome de coluna 'SP' inválido.  
Error : 207 (S0022) (RC=-1) - [Microsoft][ODBC Driver 11 for SQL Server][SQL Server]Nome de coluna 'PA' inválido.  
Error : 207 (S0022) (RC=-1) - [Microsoft][ODBC Driver 11 for SQL Server][SQL Server]Nome de coluna 'PP' inválido.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**Esse incidente ocorre, pois a parametrização usada nos parâmetro a baixo estão sem aspas, ou com aspas incorretas, assim o sistema não entende a funcionalidade do parâmetro e gera-se Error.log

**MV\_BLKTP00  'PA'**

**MV\_BLKTP01 ''MP'**

**MV\_BLKTP02   PI**

**MV\_BLKTP03**

**MV\_BLKTP04**

**MV\_BLKTP05**

**MV\_BLKTP06**

**MV\_BLKTP10**

**Solução**Para correção, ajustar o preenchimento dos tipos de produtos, é necessária a utilização do **apóstrofo ( ' )** e ***vírgula ( , )*** para seleção de dois ou mais tipos.

**Exemplo**:

MV\_BLKTP00 = **'ME', 'XX', 'YY'**.

***Saiba Mais:***  
*[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)*
