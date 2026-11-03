---
article_id: 360026704491
category: Escrita Fiscal - Error.log
content_hash: d8ea8fa662807d62bffffe6a9f08748df50052442d7d10e7965608cd0e61f6a4
fetched_at: '2026-06-28T22:39:32.885797+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: MP - Extrator Fiscal - Alias does not exist F2Q.
type: support-article
updated_at: '2021-04-28T15:43:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026704491-MP-Extrator-Fiscal-Alias-does-not-exist-F2Q
---

**Ocorrência**

No módulo Fiscal, ao executar a rotina do Extrator Fiscal, é apresentado o seguinte error.log:

![F2Q.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360025988011/F2Q.PNG)

**Ambiente**  
MP - SIGAFIS – 12.1.17  
   
 **Causa**

Este incidente ocorre pois a tabela F2Q não existe na base de dados.

**Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:

1. Fazer o Download do Dicionário de dados abaixo:

<https://suporte.totvs.com/portal/p/10098/download?e=688783>

2. Copiar os arquivos sdfbra.txt e sx2.unq para a pasta SYSTEMLOAD do Protheus e Executar o UPDDISTR.

3. Executar a rotina novamente.
