---
article_id: 4414388478359
category: ADVPL - Classe e Função
content_hash: f161a94b6ccddb20ac74d5a3d3084216fb0d43c17b867141f9f7e0a7015bd4d5
fetched_at: '2026-06-28T22:40:20.618553+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL  - RpcSetEnv com o
  conceito de filial e unidade de negócio
type: support-article
updated_at: '2021-11-29T14:04:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414388478359-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-RpcSetEnv-com-o-conceito-de-filial-e-unidade-de-neg%C3%B3cio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como funciona **RpcSetEnv** com o conceito de filial e unidade de negócio?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**Caso utilize o unidade de negócio, deve ser encaminhado no **RpcSetEnv** seu conteúdo na filial.   
  
Exemplo:   
Filial 01 e unidade de negócio 01, o campo filial será 0101.

```
RpcSetEnv( "99","0101", "Administrador", " ", "CTB", "CTBA102", aTables, , , , )
```

**Saiba mais**  
[RpcSetEnv - Abertura do ambiente em rotinas automáticas](https://tdn.totvs.com/pages/releaseview.action?pageId=6814927)
