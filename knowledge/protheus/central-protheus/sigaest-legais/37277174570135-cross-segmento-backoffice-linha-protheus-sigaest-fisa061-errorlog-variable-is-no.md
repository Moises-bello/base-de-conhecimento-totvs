---
article_id: 37277174570135
category: SIGAEST - LEGAIS
content_hash: 53c237ffe1f70160a1e016500cf4a50f0eab979f1e6f8d37f3455441aa1918eb
fetched_at: '2026-06-28T22:38:51.688985+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - FISA061 - Error.log
  "variable is not array - Type [C] on BACKOFFICE.STOCK.CALCULATIONFCI.FCICFGTRIB"
type: support-article
updated_at: '2026-01-06T18:22:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37277174570135-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-FISA061-Error-log-variable-is-not-array-Type-C-on-BACKOFFICE-STOCK-CALCULATIONFCI-FCICFGTRIB
---

O erro "variable is not array - Type [C] on BACKOFFICE.STOCK.CALCULATIONFCI.FCICFGTRIB" no TOTVS Backoffice pode ser resolvido aplicando o pacote de correção correspondente à versão do sistema, disponível para download, e processando novamente a rotina FCI (FISA061) no módulo de Estoque. Recomenda-se aplicar o patch primeiro em ambiente de homologação com backup do RPO.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37277174555671) Tempo aproximado para leitura: **00:01:17 min**  
  
**Dúvida**  
Como resolver o error.log *"variable is not array - Type [C] on BACKOFFICE.STOCK.CALCULATIONFCI.FCICFGTRIB"*  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
  
**Solução**  
Para solucionar este incidente, realize os seguintes passos:

1. Aplicar o pacote de correção do erro conforme seu release (e em caso de release expirado, se houver garantia estendida):

**12.1.2210:**[**Clique aqui e baixe**](https://r.totvs.io/p/1229113)**| 12.1.2310:**[**Clique aqui e baixe**](https://r.totvs.io/p/1229114)**12.1.2410:**[**Clique aqui e baixe**](https://r.totvs.io/p/1229112)**| 12.1.2510:** [**Clique aqui e baixe**](https://r.totvs.io/p/1229115)

Observação: sempre aplicar pacotes primeiramente em ambiente de homologação com backup prévio do RPO.

2. Abrir o ambiente, no módulo de Estoque e processar novamente a rotina de Processamento do FCI (FISA061).

3 - O incidente não ocorrerá mais.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Legais/Fiscais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538741-LEGAIS-BLOCO-H-MATR460)
