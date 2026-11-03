---
article_id: 360050353833
category: ADVPL - Ponto de Entrada
content_hash: ff056eb8779d718ab4546582fbe195b40d35e2c8bf10afb38a646d130a89ad3b
fetched_at: '2026-06-28T22:40:11.621996+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus  - ADVPL - Ponto de entrada
  MA065TOK
type: support-article
updated_at: '2021-12-29T17:35:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050353833-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-MA065TOK
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Se no MATA120 permite criar registros no Grupo x Fornecedor  (SAD), qual o motivo de não passar no PE MA065TOK?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas as versões  
  
**Solução**O ponto de entrada em questão deve ser considerado apenas para inclusões manuais pela rotina **MATA065.**  
A **criação automática** via Pedido de Compras da amarração utiliza o recurso **RecLock()** para gravação dos dados direto na tabela do banco de dados. Desta forma não passa pelo ponto de entrada.
