---
article_id: 360026517031
category: ADVPL - Web Service
content_hash: 8697e98f8d600eec25eb6ff412cfab4aea1b10e58b152769e988b3146d77b9dd
fetched_at: '2026-06-28T22:40:10.366630+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Acentuação no retorno
  de API REST
type: support-article
updated_at: '2024-04-04T21:15:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026517031-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Acentua%C3%A7%C3%A3o-no-retorno-de-API-REST
---

**Dúvida**Estou utilizando o FWRest para consumir uma API. Tal API, devolve um JSon, com palavras acentuadas. Consigo obter o retorno da API normalmente, porém os caracteres acentuados não estão sendo retornados de forma correta, mesmo setando o UTF-8.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas as versões.  
  
**Solução**Para os casos onde a API retorna dados encodados em UTF-8, para a exibição correta, se faz necessário a utilização da função **[DecodeUTF8](http://tdn.totvs.com/display/tec/DecodeUTF8)**.  
Exemplo:

```
DecodeUTF8('FabricaÃ§Ã£o', "cp1252")
```

```
Retorno "Fabricação"
```

**Saiba mais**  
[DecodeUTF8](https://tdn.totvs.com/display/tec/DecodeUTF8)  
[EncodeUTF8](https://tdn.totvs.com/display/tec/EncodeUTF8)
