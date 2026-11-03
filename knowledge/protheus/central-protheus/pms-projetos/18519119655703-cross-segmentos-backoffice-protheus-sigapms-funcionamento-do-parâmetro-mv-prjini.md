---
article_id: 18519119655703
category: PMS - Projetos
content_hash: 024624d9e57afff9d8ad90d8bc196c7a0af13761917530df4cceea6bce18ff2a
fetched_at: '2026-06-28T22:37:15.187093+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Funcionamento do parâmetro
  MV_PRJINIC na fase inicial do projeto
type: support-article
updated_at: '2024-02-26T18:32:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18519119655703-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Funcionamento-do-par%C3%A2metro-MV-PRJINIC-na-fase-inicial-do-projeto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18519105762327) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Qual o funcionamento do parâmetro **MV\_PRJINIC** na fase inicial do projeto?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões  
  
**Solução**O parâmetro **MV\_PRJINIC** serve para determinar qual a fase que um projeto novo incluído no módulo SIGAPMS começará (automaticamente), seja ele incluído manualmente ou integrado de outro sistema.

O valor informado no campo **MV\_PRJINIC** deve ser algum código de fase (PMSA070) válido (campo AEA\_COD):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18519099955991)

**Exemplo:**

1 - Parâmetro **"MV\_PRJINIC"** atribui o valor inicial do Campo do projeto **"AF8\_FASE":**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18519059068439)

2 - Ao incluir um projeto/integrar:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18519089283223)
