---
article_id: 14339501555351
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: 267bf45868d134983151ec5a7719038f01dec7992766baf0d85fce2c257b11ab
fetched_at: '2026-06-28T22:38:24.057285+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - PGV - Error
  [SQL Server]Incorrect syntax near '|'
type: support-article
updated_at: '2023-05-04T12:49:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14339501555351-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-PGV-Error-SQL-Server-Incorrect-syntax-near
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**

Ao logar no **Portal Gestão de Vendas**, no **console** do appserver do **REST** é exibida a **mensagem** de erro:

**[SQL Server]Incorrect syntax near '|'.**

E na página web do Portal são exibidos os **helps abaixo**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14338803983767)

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

No arquivo "**appserver.ini**" do ambiente **REST** altere a chave **[DBAccess]** com o parâmetro **"DataBase=MSSQL7"** para **"DataBase=MSSQL"**

**Exemplo**

**De:**

```
[DBAccess]
Database=MSSQL7
```

**Para:**

```
[DBAccess]   
Database=MSSQL
```

**Saiba Mais**

**[Application Server - [DBAccess] - Database](https://tdn.totvs.com/x/_Ypc)**
