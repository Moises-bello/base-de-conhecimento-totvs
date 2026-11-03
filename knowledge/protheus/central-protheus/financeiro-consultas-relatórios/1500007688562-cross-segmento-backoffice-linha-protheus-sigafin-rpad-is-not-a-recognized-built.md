---
article_id: 1500007688562
category: Financeiro - Consultas / Relatórios
content_hash: 8a5b06fcf87ea42726c5d2c2a6decca30c09f1a0d4458a38d4153e059827c011
fetched_at: '2026-06-28T22:37:58.399006+00:00'
product: protheus
section_id: 1500001539561
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - 'RPAD' is not a recognized
  built-in function name
type: support-article
updated_at: '2023-01-25T23:21:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007688562-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-RPAD-is-not-a-recognized-built-in-function-name
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**Na geração de relatório Modulo Protheus ocorre o erro.log abaixo:

**Error : 195 (37000) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]'RPAD' is not a recognized built-in function name.**  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Descrição incorreta do Banco Dados  
  
**Solução**

Para o error.log apresentado em seu ambiente, se faz necessário que altere o nome do banco de MSSQL7 para MSSQL, o problema da Query.  

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500010900722/mceclip0.png)

​
