---
article_id: 24245650456343
category: ADVPL - Classe e Função
content_hash: 9dd77edbed77ed9ac4c0d407c0370b773d2201682871428d42eb853d3c2c3303
fetched_at: '2026-06-28T22:40:21.528507+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL- É possível efetuar
  a pesquisa por coluna no browser em campo virtual do tipo numérico?
type: support-article
updated_at: '2024-10-24T14:52:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24245650456343-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-%C3%89-poss%C3%ADvel-efetuar-a-pesquisa-por-coluna-no-browser-em-campo-virtual-do-tipo-num%C3%A9rico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24245650442007) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**É possível efetuar a pesquisa por coluna no browser em campo virtual do tipo numérico?  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**

O campo virtual somente será exibido para pesquisa no browser se for do tipo *varchar/string/clob/character,* pois sua pesquisa é feita por like.  
Além disso, é necessário que no inicializador de browser do campo criado utilize um *posicione*.

**Saiba Mais**

[Campo Virtual](https://tdn.totvs.com/display/public/framework/Posicione+com+Campo+Virtual)

[Posicione](https://tdn.totvs.com/display/public/framework/Posicione+-+Posiciona+tabela+em+registro)
