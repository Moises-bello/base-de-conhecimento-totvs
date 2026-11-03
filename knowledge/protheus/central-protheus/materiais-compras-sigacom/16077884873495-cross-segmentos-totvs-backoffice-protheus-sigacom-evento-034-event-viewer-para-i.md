---
article_id: 16077884873495
category: Materiais - Compras (SIGACOM)
content_hash: 38b7fbaea3352a7d2f4c4de08efac17a298133d36e26ccfbf71bbb76aaf7e682
fetched_at: '2026-06-28T22:41:17.669434+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Evento 034 Event Viewer
  para informar quando o pedido estiver liberado para compra
type: support-article
updated_at: '2024-11-19T13:25:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16077884873495-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Evento-034-Event-Viewer-para-informar-quando-o-pedido-estiver-liberado-para-compra
---

**Dúvida**  
Evento 034 - Event Viewer para informar quando o Pedido estiver liberado para compra.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Compras - Todas as versões  
  
**Solução**

Este evento tem a funcionalidade de disparar email para o usuário que incluiu o Pedido de Compras quando este pedido tiver sua alçada liberada.

1. Segue exemplo de Configuração de e-mail de envio do Messenger e Event Viewer para que possa realizar a configuração em seu ambiente:

[- Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Exemplo de configuração Messenger](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011724292-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Exemplo-de-configura%C3%A7%C3%A3o-Messenger-Disparo-de-e-mail-de-eventos)

[- Como configurar o Event Viewer para disparar notificações](https://tdn.totvs.com/x/76s4E)

2. Cadastrar todos usuários Compradores para receber o evento 034.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16077860077463)

**Obs:**

O evento é disparado somente quando o pedido for liberado por completo.

![](https://totvssuporte.zendesk.com/attachments/token/JpIgbCBrvA6tbnUGs8cEbaa1P/?name=image.png)

**Obs:**

Somente o usuário que incluiu o Pedido de Compras vai receber o e-mail do evento 034 de liberação. Caso este evento seja vinculado a outros usuários que não foi o que incluiu o Pedido de Compras, eles não receberão o email deste evento para este pedido incluido e liberado.

**Obs:**

A rotina M-messenger (MATA045) será descontinuada em 31/10/2024.

**Rotina Substituta:**  
[CFGA040 - Event Viewer](https://tdn.totvs.com/x/76s4E)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Substituição da Rotina Messenger(MATA045)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23139788947607-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Substitui%C3%A7%C3%A3o-da-Rotina-Messenger-MATA045?source=search)
