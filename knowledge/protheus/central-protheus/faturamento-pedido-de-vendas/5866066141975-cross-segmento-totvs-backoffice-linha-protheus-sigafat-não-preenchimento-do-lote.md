---
article_id: 5866066141975
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 9e9aa5454bd27ca8c4bbc6ab399a198487084049adfe0a830cf1897329b20667
fetched_at: '2026-06-28T22:38:38.567291+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Não preenchimento
  do lote na SC9 e SD2 onde o pedido utiliza TES que não movimenta estoque
type: support-article
updated_at: '2022-05-04T17:37:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5866066141975-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-N%C3%A3o-preenchimento-do-lote-na-SC9-e-SD2-onde-o-pedido-utiliza-TES-que-n%C3%A3o-movimenta-estoque
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**

Não preenchimento do lote na SC9 e Sd2 onde o pedido utiliza tes que não movimenta estoque.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat -12.1.27 em diante

**Causa**O erro ocorria por havia uma validação indevida de tabela no comando de banco DbCloseArea, fazendo com a tabela correta não fosse avaliada.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1 Aplique o pacote da issue DSERFAT-24425 de correção correspondente a release utilizada:

12.1.27: <https://suporte.totvs.com/portal/p/10098/download?e=1066791> ; 

12.1.33: <https://suporte.totvs.com/portal/p/10098/download?e=1066792> ;

2. Via VS-CODE, aplique o pacote ao RPO.  
3. Reinicie o smartclient e efetue o procedimento novamente.
