---
article_id: 35832257052567
category: Financeiro - Conciliador Backoffice
content_hash: 5d59e447030eeac1dad160882e116d61e7d73bac0c1749ee7ffc9be6863c25d5
fetched_at: '2026-06-28T22:37:47.185880+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Conciliação
  Automática: Bloqueio de Match entre Registros com Valores Divergentes'
type: support-article
updated_at: '2025-10-23T18:04:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35832257052567-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Concilia%C3%A7%C3%A3o-Autom%C3%A1tica-Bloqueio-de-Match-entre-Registros-com-Valores-Divergentes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35832270875799) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Durante o uso da conciliação manual, o sistema não bloqueia o match entre registros com valores divergentes entre a SIG x FK5

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.2310  
  
**Solução**

O comportamento observado está de acordo com o padrão do sistema.  
O sistema não impede a realização do Match, apenas exibe um alerta para confirmar a ação. Caso o cliente confirme, as informações são migradas para a aba de **Dados Conciliados** com o status “Manual Divergente (MD)”, indicando que houve conciliação de valores que não estavam batendo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35835586844439)  
   
Esse é o funcionamento esperado tanto para conciliações manuais quanto para totais, dentro do processo 0023 (conciliação automática).

Em nenhum dos casos o sistema bloqueia a ação do usuário — apenas alerta e, se ele optar por prosseguir, registra a conciliação como **Manual Divergente, ajudando o usuário a identificar conciliações não batidas.** Não há parâmetros ou pontos de entradas já desenvolvidos que bloqueiem esta ação do usuário.
