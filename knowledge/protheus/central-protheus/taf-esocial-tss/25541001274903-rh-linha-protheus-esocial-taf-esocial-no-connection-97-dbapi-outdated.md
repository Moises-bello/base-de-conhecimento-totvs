---
article_id: 25541001274903
category: TAF - eSocial -TSS
content_hash: 69c1d448465c2f52ec967653f3f123ebf03cd16056e5608cc9a517c611cd1541
fetched_at: '2026-06-28T22:45:21.864285+00:00'
product: protheus
section_id: 1500001536761
source: central-protheus
title: 'RH (Linha Protheus) - eSocial - TAF eSocial - No connection: -97 - DBAPI_OUTDATED'
type: support-article
updated_at: '2026-06-18T12:13:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25541001274903-RH-Linha-Protheus-eSocial-TAF-eSocial-No-connection-97-DBAPI-OUTDATED
---

**Dúvida**Error - TOPCONN - No connection: -97 - DBAPI\_OUTDATED, como ajustar?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - TSS -  Todas as versões

**Solução**

**1.**Acesse a pasta **Dbaccess/Client**  do **TAF**.

**Caminho exemplo**: TAF \TafDbAccess64\ client

Copie o arquivo **dbapi.dll.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25541016582295)

**2.**Cole o arquivo **dbapi.dll,**na estrutura do TSS.

**Caminho exemplo:** TSS\BIN\appserver.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25541531302551)

**3**. Reinicie o serviço do TSS e valide novamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25541016586007)

**Atenção: Antes de iniciar todo o processo, realize um backup.**
