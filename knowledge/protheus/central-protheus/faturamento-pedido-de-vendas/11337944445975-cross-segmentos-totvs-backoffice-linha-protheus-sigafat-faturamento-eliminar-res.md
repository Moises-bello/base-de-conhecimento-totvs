---
article_id: 11337944445975
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: db3e52eaf3b8bab267e26ac1a5d6261691d46f05a07cfe7bd002e4b84f21ccba
fetched_at: '2026-06-28T22:38:42.629194+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento)
  - Eliminar resíduos do controle de reservas
type: support-article
updated_at: '2022-12-30T20:34:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11337944445975-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Eliminar-res%C3%ADduos-do-controle-de-reservas
---

**Dúvida**Qual o comportamento e configuração da funcionalidade de eliminação de resíduos das reservas no Faturamento?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - Todas as versões.  
  
**Solução**

Esta opção é utilizada quando ocorre também a eliminação de resíduos no pedido de venda.

Quando o pedido de venda é faturado parcialmente a nota fiscal é emitida com referência à apenas alguns produtos ou quantidade parcial.

**Caminho: Atualizações** > Pedidos > Controle de Reservas > Outras Ações > **Eliminar Resíduos**

**Exemplo:**

Inclua uma reserva com 3 produtos e vincule ao pedido, faturando apenas 2 produtos, ficando uma unidade do produto como resíduo.

Neste caso, elimine o resíduo do Pedido de Venda e da rotina Controle de Reservas.

A reserva ficará com a legenda em azul, descrita como eliminação de resíduos e será gravado no campo **C0\_QTDELIM** a quantidade do resíduo eliminado.

**Saiba mais:**

[FAT0131 Rotina Controle de Reservas (MATA430)](https://tdn.totvs.com/x/P5AjDw)
