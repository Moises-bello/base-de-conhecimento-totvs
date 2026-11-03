---
article_id: 36438205203479
category: SIGAACD - Automação e Coleta de Dados
content_hash: da58ec887f285db11e24b54134a2e6117e48e62edf8f44a1eaced55eca6e6387
fetched_at: '2026-06-28T22:39:11.259452+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDV120 - Inserir
  uma linha de chave duplicada no objeto 'dbo.SD1010'
type: support-article
updated_at: '2025-11-19T12:09:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36438205203479-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDV120-Inserir-uma-linha-de-chave-duplicada-no-objeto-dbo-SD1010
---

O problema de erro de chave duplicada e aglutinação indevida de itens no recebimento de mercadorias com controle de lote e endereço.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36438189053207) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como corrigir, durante o recebimento de mercadorias com controle de lote e endereço, o sistema apresentou um erro de chave duplicada ao finalizar a conferencia. E quando não há o controle de lote, o sistema esta aglutinando itens da nota fiscal de mesmo código de produto indevidamente.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
O problema foi solucionado após ajustes no processo de conferencia e gravação dos itens da nota fiscal. Com a correção aplicada, o sistema passou a tratar corretamente os produtos com e sem controle de lote, evitando a geração de chave duplicada e impedindo que itens de mesmo código fossem aglutinados indevidamente.

Aplicar a correção em base de homologação, realizando o backup das informações.

**12.1.2210:**<https://r.totvs.io/p/1221910> ; **12.1.2310**:<https://r.totvs.io/p/1221911> ; **12.1.2410**:<https://r.totvs.io/p/1221909> ; **12.1.2510:**<https://r.totvs.io/p/1221913> ;

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
