---
article_id: 33770056028823
category: eSocial - Middleware
content_hash: 3005e7a78058060db90795bcdf9268abc23597a7f523d2755d768c358b6c45c2
fetched_at: '2026-06-28T22:47:05.502104+00:00'
product: rm
section_id: 1500000834541
source: central-rm
title: 'RH - RM - FOP - eSocial - Middleware: Relatório de Conferência INSS - PIS/PASEP'
type: support-article
updated_at: '2025-07-30T19:33:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33770056028823-RH-RM-FOP-eSocial-Middleware-Relat%C3%B3rio-de-Confer%C3%AAncia-INSS-PIS-PASEP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33770034199063) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como gerar o Relatório de Conferência INSS para consultar as bases e valores do PIS/PASEP?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial  - A partir da 12.1.2406.280  
  
**Solução**  
Foi implementada no **Relatório de Conferência INSS** uma nova funcionalidade que permite comparar a **base e o valor do PIS/PASEP** calculados pelo sistema com os dados enviados ao **eSocial no evento S-5001.**  
  
Exemplo  
Relatório de Conferência INSS Coluna PIS-PASEP:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33770336175127)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33770336180119)

**ATENÇÃO:** A base de cálculo do PIS/PASEP (tag <vrBcPisPasep> do S-5001) é retornada por filial, e não por lotação tributária. Diante disso, foi necessário criar uma aba separada no relatório especificamente para o PIS/PASEP.  
  
Saiba mais:   
[Middleware - Relatório de Conferência de INSS](https://tdn.totvs.com/pages/viewpage.action?pageId=536721262)
