---
article_id: 360050376473
category: RH - Cadastros
content_hash: 4244e91d691fde61caf3236870f24a596730d3e0703d9b44a2a6b2946fee6c27
fetched_at: '2026-06-28T22:44:53.131656+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Tolerância para Atraso e Saída Antecipada por Marcação
  e Período
type: support-article
updated_at: '2026-02-04T18:37:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050376473-RH-Linha-Protheus-PON-Toler%C3%A2ncia-para-Atraso-e-Sa%C3%ADda-Antecipada-por-Marca%C3%A7%C3%A3o-e-Per%C3%ADodo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35165232507671) Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
Como configurar Tolerância para Atraso e Saída Antecipada por Marcação e Período?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para os exemplos abaixo, foi considerado um funcionário com Jornada Prevista:  
**08:00 - 12:00 - 13:00 - 17:00**.

Na regra de apontamento, foi definida:  
- Tolerância de 00:05 **por marcação;**  
- Tolerância de 00:10 **por período apenas para** **atraso e saída antecipada** (Tol. Atr. Per e Tol. S. A. Per.):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31747089749143)

**Atrasos:**  
- Para o dia **01/01/2020:** Foi apontado **atraso de 00:06** - na entrada da jornada, a tolerância por marcação não foi respeitada;  
- Para o dia **02/01/2020:** Foi apontado **atraso de 00:11** - a tolerância por período **não foi respeitada;**  
- Para o dia **03/01/2020:** **Não** foi apontado **evento de atraso** - as duas tolerâncias **foram respeitadas;**  
- Para o dia **13/01/2020:** **Não** foi apontado **evento de atraso -** as duas tolerâncias **foram respeitadas;**  
- Para o dia **14/01/2020:** Foi apontado **atraso de 00:11** - a tolerância por período **não foi respeitada;**  
- Para o dia **15/01/2020: Não** foi apontado **evento de atraso** - as duas tolerâncias **foram respeitadas.**  
  
**Saída Antecipada:**  
- Para o dia **06/01/2020:** Foi apontado **saída antecipada 00:06** - na saída para o almoço, a tolerância por marcação **não foi respeitada;**  
- Para o dia **07/01/2020:** Foi apontado **saída antecipada de 00:11** - a tolerância por período **não foi respeitada;**  
- Para o dia **08/01/2020:** **Não** foi apontado **evento de saída antecipada** - as duas tolerâncias **foram respeitadas;**  
- Para o dia **13/01/2020:** **Não** foi apontado **evento de saída antecipada** - as duas tolerâncias **foram respeitadas;**  
- Para o dia **14/01/2020:Não** foi apontado **evento de saída antecipada** - as duas tolerâncias **foram respeitadas;**  
- Para o dia **15/01/2020:** Foi apontado **saída antecipada de 00:11** - a tolerância por período **não foi respeitada.**

![Capturar8.PNG](https://tdn.totvs.com/download/attachments/496398394/Capturar8.PNG?version=2&modificationDate=1579782095867&api=v2)

**Observação:**  
Se na Regra de Apontamento estiverem preenchidas as tolerâncias de atraso e saída antecipada por período, o sistema validará os eventos separadamente (dias 13, 14 e 15):  
- atraso, com a tolerância de atraso;  
- saída antecipada, com a tolerância de saída antecipada.

**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
