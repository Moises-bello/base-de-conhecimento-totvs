---
article_id: 11334342699799
category: Materiais - Compras (SIGACOM)
content_hash: 062692246ce3aa6e817133f7afd37599ca2a4498a8bdf0496859d36dfdc16664
fetched_at: '2026-06-28T22:41:11.685718+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Mile na rotina
  de Pedido de Compras e os campos C7_DINICQ, C7_DINITRA, C7_DINICOM e C7_DATPRF.
type: support-article
updated_at: '2022-12-30T19:01:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11334342699799-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Mile-na-rotina-de-Pedido-de-Compras-e-os-campos-C7-DINICQ-C7-DINITRA-C7-DINICOM-e-C7-DATPRF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Mile na rotina de Pedido de Compras  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**

Os campos Data início de CQ (C7\_DINICQ), Data início de trânsito (C7\_DINITRA) e Data p/ início da compra (C7\_DINICOM) são utilizados para calcular o Lead Time do Pedido de Compra e esse cálculo é acionado via gatilho do campo Data Entrega (C7\_DATPRF).

Nesse ponto, temos 2 opções:  
1 - Preencher os cadastros para que o Lead Time seja calculado pelo sistema.  
2 - Alterar a ordenação dos campos na tabela Pedido de Compra / Autorização de Entrega (SC7) para que o campo Data Entrega (C7\_DATPRF) fica antes dos campos de Lead Time, fazendo com que os valores enviados nesses campos não sejam sobrepostos.

O cálculo do Lead Time é feita da seguinte maneira:

C7\_DINICQ    = C7\_DATPRF - (Formula (B5\_FPRZCQ) ou Prazo (B5\_PRZCQ))  
C7\_DINITRA   = C7\_DINICQ  - (Cadastro Prd x Forn (A5\_TEMPTRA))  
C7\_DINICOM = C7\_DINITRA - (Formula do PCP)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
