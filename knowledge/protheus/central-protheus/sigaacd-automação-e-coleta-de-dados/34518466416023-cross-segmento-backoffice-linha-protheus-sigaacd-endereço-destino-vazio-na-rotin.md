---
article_id: 34518466416023
category: SIGAACD - Automação e Coleta de Dados
content_hash: d5b43f329e30f569357aeeb0d56f5758aad886a40b4c9c1481847f1de3cc14c4
fetched_at: '2026-06-28T22:39:12.700714+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Endereço destino vazio
  na rotina de Transferência entre Endereço
type: support-article
updated_at: '2025-08-28T17:13:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34518466416023-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Endere%C3%A7o-destino-vazio-na-rotina-de-Transfer%C3%AAncia-entre-Endere%C3%A7o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34518466395287) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como não permitir informar o endereço destino como vazio, na rotina de Transferência entre Endereço(ACDV150)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**

Quando o endereço de destino é confirmado como **vazio** na rotina de **transferência de endereço via rotina ACDV150**, por padrão, o sistema entende que o produto não tem destino definido.

Para que o sistema não permita esse comportamento no endereço destino, existe o parâmetro **MV\_CBENDDV** que tem o objetivo de **permitir ou não o endereço destino vazio na transferência via rotina ACDV150.**

Segue uma documentação mais detalhada sobre o assunto:

[Endereço destino vazio na transferência via rotina acdv150](https://tdn.totvs.com/pages/releaseview.action?pageId=828004047)

**Saiba Mais:**

[*Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
