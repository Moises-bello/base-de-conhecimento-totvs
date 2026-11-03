---
article_id: 10601220705303
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 05053d6f0986cb3f897a350c86bb1eb95b31b97665f1673b7bb85e9e6ca8ef84
fetched_at: '2026-06-28T22:38:45.226883+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -  E1_CCUSTO
type: support-article
updated_at: '2022-11-30T18:12:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10601220705303-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-E1-CCUSTO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como gerar informações no campo E1\_CCUSTO por meio da integração do Faturamento com o Financeiro ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**O Modulo Faturamento Protheus não preenche o centro de custo na SE1 na geração da nota, o campo E1\_CCUSTO somente é gravado por funções do financeiro , o mata461 não tem tratamento para levar a informação de centro de custo para o financeiro.  
  
O que pode ser feito é utilizar o ponto de entrada M460FIM (<https://tdn.totvs.com/pages/viewpage.action?pageId=6784180>) para pegar o conteúdo gravado do campo D2\_CCUSTO  e gravar no campo E1\_CCUSTO. O campo D2\_CCUSTO é alimentado pelo conteúdo do campo C6\_CC.
