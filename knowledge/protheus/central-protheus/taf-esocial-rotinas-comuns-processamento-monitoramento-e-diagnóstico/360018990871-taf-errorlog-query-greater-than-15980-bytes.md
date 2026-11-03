---
article_id: 360018990871
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 0a2b5091a8d242395b0cea732e075036ec14688f2ab945730dcc46b26e6d818d
fetched_at: '2026-06-28T22:45:21.193992+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: TAF - Error.log - "Query greater than 15980 bytes"
type: support-article
updated_at: '2021-06-15T12:45:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018990871-TAF-Error-log-Query-greater-than-15980-bytes
---

**Dúvida**Ao realizar qualquer atividade no TAF, é apresentada o Error.log: "Query greater than 15980 bytes".

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014602332/mceclip0.png)

**Ambiente**

TAF - eSocial - 11.80 a 12.1.23

**Solução**

 1. Parar os serviços do TAF

 2. Aplicar o parâmetro MaxQuerySize=31960 no bloco [General] do AppServer.ini do TAF.

 3. Iniciar os serviços do TAF.

**Observação:** A chave deve ser incluída no arquivo Appserver.ini do ERP e **não** no do **TSS**.
