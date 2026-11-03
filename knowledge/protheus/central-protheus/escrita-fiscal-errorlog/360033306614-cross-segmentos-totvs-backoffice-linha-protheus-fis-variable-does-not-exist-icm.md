---
article_id: 360033306614
category: Escrita Fiscal - Error.log
content_hash: 42f8e4a7afa00d53becc959f4c0b8cc21d919965daa73a12897a84d4b953155d
fetched_at: '2026-06-28T22:39:32.877879+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - variable does not
  exist ICM on GRAVATIT(FISXAPUR.PRX)
type: support-article
updated_at: '2021-07-08T13:31:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033306614-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-variable-does-not-exist-ICM-on-GRAVATIT-FISXAPUR-PRX
---

**Ocorrência**Ao gerar apuração de ICMS (MATA953) está ocorrendo seguinte error log :

variable does not exist ICM on GRAVATIT(FISXAPUR.PRX)  
  
**Ambiente**Protheus – Livros Fiscais  – A partir da versão 12.1.17  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1.  Abra o parâmetro **MV\_PFAPUIC** pelo configurador;  
2.  Coloque ASPAS duplas = "ICM".

Exemplo : 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042719754/mceclip0.png)
