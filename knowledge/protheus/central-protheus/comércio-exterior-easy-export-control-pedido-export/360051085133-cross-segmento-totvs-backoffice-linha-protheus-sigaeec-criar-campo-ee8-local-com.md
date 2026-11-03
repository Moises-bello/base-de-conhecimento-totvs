---
article_id: 360051085133
category: Comércio Exterior - Easy Export Control - Pedido - Export
content_hash: b9cad94af34e9da211a54333865b71397759da13ba525d885b0ce7bce23fcc7d
fetched_at: '2026-06-28T22:36:58.996394+00:00'
product: protheus
section_id: 1500001538181
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Criar campo EE8_LOCAL
  com mesmo padrão do C6_LOCAL
type: support-article
updated_at: '2021-08-23T21:02:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051085133-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Criar-campo-EE8-LOCAL-com-mesmo-padr%C3%A3o-do-C6-LOCAL
---

**Dúvida**Criar campo EE8\_LOCAL com mesmo padrão do C6\_LOCAL.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões.  
  
**Solução**Apesar de ter um tratamento para quando o campo EE8\_LOCAL existir, para que o conteúdo deste possa ser integrado com o pedido.

Por não se tratar de um campo padrão, vale dizer que ao criar o campo customizado EE8\_LOCAL, o ideal é que não seja aproveitada a mesma consulta padrão utilizada no campo C6\_LOCAL, pois a mesma contém regras do faturamento, que inviabiliza seu uso na exportação. Sugerimos que seja criada uma consulta customizada para o uso neste campo EE8\_LOCAL.

Ponto de entrada função "PE\_GRVITEM" <https://tdn.totvs.com/pages/releaseview.action?pageId=309408592>
