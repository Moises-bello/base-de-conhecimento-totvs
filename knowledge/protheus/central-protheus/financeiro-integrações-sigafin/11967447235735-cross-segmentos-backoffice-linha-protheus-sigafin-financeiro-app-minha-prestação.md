---
article_id: 11967447235735
category: Financeiro - Integrações (SIGAFIN)
content_hash: f862db034b0d752e921311a69b6cb25b4a840faee46e5d12fc439e501c97cd1f
fetched_at: '2026-06-28T22:38:18.539459+00:00'
product: protheus
section_id: 1500001539241
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Financeiro - APP minha
  prestação de contas - Erro ao baixar customers
type: support-article
updated_at: '2024-11-18T20:20:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11967447235735-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Financeiro-APP-minha-presta%C3%A7%C3%A3o-de-contas-Erro-ao-baixar-customers
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Ao acessar o App minha prestação de contas o sistema apresenta erro:  *"**ERRO AO BAIXAR CUSTOMERS*" como corrigir?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Existe um ajuste no **webservice** de sincronismo de clientes do **aplicativo Minha Prestação de Contas** para **retornar** ou **não os clientes** de acordo com o parâmetro **MV\_MPCSCLI**:

* **MV\_MPCSCLI**: Se **desabilitado (.F.)**, os clientes **não serão sincronizados**.
* O *default* é **habilitado (.T.)**.

Para ajuste do problema citado acima, deixar o parâmetro conforme print abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11967415507095)
