---
article_id: 4414425385239
category: SIGAEST - PROCESSAMENTOS
content_hash: a4d4cebcca25ac078f9092f8a7c039d99bc3c8ded1aafc4d0c4317e496dbbfd6
fetched_at: '2026-06-28T22:39:05.003343+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - [Microsoft][SQL Server
  Native Client 11.0][SQL Server]The instance of the SQL Server Database Engine cannot
  obtain a LOCK resource at this time.
type: support-article
updated_at: '2021-11-29T21:11:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414425385239-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Microsoft-SQL-Server-Native-Client-11-0-SQL-Server-The-instance-of-the-SQL-Server-Database-Engine-cannot-obtain-a-LOCK-resource-at-this-time
---

**Ocorrência**Durante a execução da determinadas rotinas do estoque, ocorre o erro abaixo:

The instance of the SQL Server Database Engine cannot obtain a LOCK resource at this time. Rerun your statement when there are fewer active users. Ask the database administrator to check the lock and memory configuration for this instance, or to check for long-running transactions.  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) -Estoque/Custos - Todas as versões.  
  
**Causa**

Esse erro é causado quando há bloqueios de abertura ou fechamento de estruturas no banco de dados.  
  
**Solução**

Por se tratar de um erro relacionado a permissão no Banco de Dados recomendamos que seja acionado o DBA ou responsável pelo Banco de Dados da empresa, para que faça as liberações necessárias para abertura e fechamento da estrutura de comandos SQL.

Para mais informações sobre esse erro **[clique aqui](https://support.microsoft.com/pt-br/topic/how-to-troubleshoot-sql-server-lock-related-problems-and-errors-b88d0c28-7190-b7f9-53c6-453a4ee63fa5):**

**Saiba Mais:**

*[Clique aqui e veja mais artigos sobre Processamentos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538861-SIGAEST-PROCESSAMENTOS)*
