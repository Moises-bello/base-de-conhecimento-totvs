---
article_id: 11569381611287
category: SIGAEST - SALDOS
content_hash: e94e2322197e0a6b618861eeb8ea2ffefce3adce9f355bbb49255b8bb11e7342
fetched_at: '2026-06-28T22:39:14.865482+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Identificar quando
  ocorreu a última Saída ou último movimento de um produto no Estoque
type: support-article
updated_at: '2023-01-10T18:20:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11569381611287-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Identificar-quando-ocorreu-a-%C3%BAltima-Sa%C3%ADda-ou-%C3%BAltimo-movimento-de-um-produto-no-Estoque
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como posso identificar a data da última saída ou último movimento de um produto no saldo em Estoque?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Na rotina ***SALDOS EM ESTOQUE (MATA225)*** existe o campo ***Última Saída (B2\_USAI)*** que apresenta a última saída do produto tanto por Vendas (SD2) como por Movimentos Internos (SD3), ou seja sempre que consumido saldo do produto esse campo é atualizado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11570002480279)

Também na mesma rotina, existem os campos ***Data do Movimento (B2\_DMOV)*** e ***Hora do Movimento (B2\_HMOV).***

O campo ***B2\_DMOV*** é atualizado tanto com as saídas de saldos como as entradas de saldos.

O campo ***B2\_HMOV*** é atualizado sempre com a hora da última atualização de um dos 2 campos.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11570325412247)

***Saiba Mais:***

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)*
