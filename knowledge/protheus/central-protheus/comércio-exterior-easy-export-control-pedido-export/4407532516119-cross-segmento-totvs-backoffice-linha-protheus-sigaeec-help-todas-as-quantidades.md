---
article_id: 4407532516119
category: Comércio Exterior - Easy Export Control - Pedido - Export
content_hash: 5ab4b073cf7d033f755a3982d6fcb5dd9aa80e9e785092752210e451667ea81f
fetched_at: '2026-06-28T22:36:59.014848+00:00'
product: protheus
section_id: 1500001538181
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Help: Todas as
  quantidades dos itens do pedido já foram embarcadas'
type: support-article
updated_at: '2021-09-01T20:21:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407532516119-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Help-Todas-as-quantidades-dos-itens-do-pedido-j%C3%A1-foram-embarcadas
---

**Dúvida**Como faço para editar o pedido de exportação (**EECAP100**) uma vez que o embarque já foi finalizado e é exibido uma mensagem ao alterar o processo . **"Todas as quantidades dos itens do pedido já foram embarcadas. O sistema não permitirá alterações."**

![ALTERAR_PEDIDO_EXPORTA__O.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4407537688087/ALTERAR_PEDIDO_EXPORTA__O.PNG)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**Temos uma parametrização que define se o sistema bloqueia a edição do pedido quando todas as quantidades estão embarcadas. Para que seja possível alterar o pedido de exportação mesmo se as quantidades já foram embarcadas é só alterar o conteúdo do parâmetro **MV\_AVG0090 = . F.**  .
