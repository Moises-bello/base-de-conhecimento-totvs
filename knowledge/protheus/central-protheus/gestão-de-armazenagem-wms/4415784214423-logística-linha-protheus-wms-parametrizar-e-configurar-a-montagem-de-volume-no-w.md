---
article_id: 4415784214423
category: Gestão de Armazenagem (WMS)
content_hash: 2ce758e661e89e25d9ef781bc1742a0ce767bb1f6fae8ea56560bebfafb73294
fetched_at: '2026-06-28T22:45:48.069156+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Parametrizar e configurar a montagem de
  volume no WMS Atual
type: support-article
updated_at: '2025-10-31T20:05:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415784214423-Log%C3%ADstica-Linha-Protheus-WMS-Parametrizar-e-configurar-a-montagem-de-volume-no-WMS-Atual
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35447263036311) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como parametrizar e configurar a montagem de volume no WMS Atual?  
  
**Ambiente**TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (SIGAWMS) -  A partir da versão 12  
  
**Solução**Pontualmente no **WMS - *Warehouse Management System* - Atual** deve ser ativado o parâmetro **MV\_WMSVEMB - Habilita funcionalidade de montagem de volumes** e configurada a **Função Exec** **DLApanheVL**, no serviço de expedição, a partir do cadastro de **Serviços Vs Tarefas - WMSA070**.  
  
Consequentemente, a montagem de volume poderá ser utilizada pelas rotinas **WMSA391 - Volumes Expedição** e **WMSV081 -** **Mnt. Vol. Expedição**.  
  
**Saiba mais**Mais detalhes podem ser verificados na documentação: [Parametrizar e configurar a montagem de volume no WMS atual.](https://tdn.totvs.com/x/XywRJw)  
Também assista ao *Webinar* sobre o cadastro **Serviços** **Vs** **Tarefas** e conheça todas as configurações disponíveis: [Webinar TOTVS | Serviços](https://www.youtube.com/watch?v=f1K8WBRCUUc) [Vs Tarefas #TOTVS\_Logística\_Linha\_Protheus](https://www.youtube.com/watch?v=f1K8WBRCUUc)
