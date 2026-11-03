---
article_id: 40797649648535
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 0d06d788813f9f342d5f334b45c76edb374d30886448398fa87f914205fad37c
fetched_at: '2026-06-28T22:37:22.987946+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help: CNTA120_07 no
  estorno de medição'
type: support-article
updated_at: '2026-05-28T15:37:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40797649648535-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-CNTA120-07-no-estorno-de-medi%C3%A7%C3%A3o
---

O erro Help CNTA020\_07 ao estornar medições de contratos ocorre porque o parâmetro MV\_CNFVIGE está configurado como N, impedindo estornos fora do período de vigência. Para resolver, ajuste MV\_CNFVIGE para S, permitindo o estorno da medição.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40797635864087) Tempo aproximado para leitura: **00:04:00 min**  
  
**Ocorrência**  
  
Help CNTA020\_07 - Contrato fora do período de vigência, no estorno da medição de contratos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797635866775)

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Gestão de contratos - Todas as versões

**Causa**

Esse help ocorre, pois o parâmetro MV\_CNFVIGE está configurado com N, no caso, para não se permitir realizar medições ou estornos fora do período de vigência do contrato.

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:  
1. Ajuste o parâmetro MV\_CNFVIGE para S para que possa permitir o estorno da medição. Feche a rotina do sistema e acesse novamente para realização de um novo teste.

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Inclusão de Parcelas / Cronograma e Medições fora da Vigência / Vencimento - Parâmetro MV\_CNFVIGE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028935871-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Inclus%C3%A3o-de-Parcelas-Cronograma-e-Medi%C3%A7%C3%B5es-fora-da-Vig%C3%AAncia-Vencimento-Par%C3%A2metro-MV-CNFVIGE)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
