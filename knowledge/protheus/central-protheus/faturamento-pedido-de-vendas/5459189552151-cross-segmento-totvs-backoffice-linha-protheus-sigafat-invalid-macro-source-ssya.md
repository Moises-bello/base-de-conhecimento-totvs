---
article_id: 5459189552151
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: efc62cdb27d94458ae357473ef0f6492c1cd53ebe2bd357f814d12bba1f8235c
fetched_at: '2026-06-28T22:38:38.551439+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - invalid macro
  source (SSYacc0105e: Error token failed, no valid token):(3.001.001) on A410TUDOK(MATV410A.PRW)'
type: support-article
updated_at: '2022-04-19T13:43:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5459189552151-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-invalid-macro-source-SSYacc0105e-Error-token-failed-no-valid-token-3-001-001-on-A410TUDOK-MATV410A-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao confirmar o pedido, gera o erro: **invalid macro source (SSYacc0105e: Error token failed, no valid token):(3.001.001) on A410TUDOK(MATV410A.PRW) 28/01/2022 17:19:27 line : 157**  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Todas as versões  
  
**Causa**O erro ocorre por que o código da natureza está sendo passado como numérico e o **mv\_1dupnat** recebe o conteúdo carácter, veja a chamada do mv\_1dupnat sendo chamado no erro:  
   
  Local 42: **CMV1DUPNAT(C) :3.001.001**

![](https://totvssuporte.zendesk.com/attachments/token/RnKYxz29bU5VVjBc9mLkgiRxi/?name=image.png)  
  
**Solução**Por padrão, o parâmetro é preenchido com  **SA1->A1\_NATUREZ**  e pode ser mudado para **SC5->C5\_NATUREZ** , mas se vai apontar o código da natureza diretamente no parâmetro, coloque entre aspas (**"3.** **001.001"**),desta forma, o erro deixará de ocorrer.
