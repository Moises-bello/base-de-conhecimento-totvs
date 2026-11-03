---
article_id: 360041611493
category: Comércio Exterior - Easy Export Control - Pedido - Export
content_hash: 205d67b34cb12857e5581c175864f8cb696fdf6551e37024ef06307ab705c82b
fetched_at: '2026-06-28T22:36:59.083696+00:00'
product: protheus
section_id: 1500001538181
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus- SIGAEEC - Aumento de Casas
  Decimais Pedido/Embarque de Exportação '
type: support-article
updated_at: '2021-11-29T11:44:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041611493-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Aumento-de-Casas-Decimais-Pedido-Embarque-de-Exporta%C3%A7%C3%A3o
---

**Dúvida**Como aumentar as Casas Decimais no Pedido/Embarque de Exportação?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões.  
  
**Solução**

Neste caso, os tamanhos das decimais do SIGAEEC devem estar de acordo com as decimais do SIGAFAT, os campos do SIGAEEC encontra-se no boletim: <https://tdn.totvs.com/pages/releaseview.action?pageId=311631781>

Alterar também os parâmetros **MV\_AVG0109** e **MV\_AVG0110** para definir o arredondamento. 

**MV\_AVG0109** - Define o número de casas decimais para arredondamento do preço unitário dos itens no pedido/embarque.

**MV\_AVG0110 -**Define o número de casas decimais para arredondamento do preço total dos itens no pedido/embarque
