---
article_id: 20594758770199
category: Materiais - Compras (SIGACOM)
content_hash: fe5fda425296fb5ace520788ada488f8ca53bc6f91f44faa9a6e2a4b4d8e1bc2
fetched_at: '2026-06-28T22:41:17.530244+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - É possível Gerar Cotação
  Aglutinada para Solicitações de Compras com Ordem de Produção?
type: support-article
updated_at: '2024-01-15T19:50:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20594758770199-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-%C3%89-poss%C3%ADvel-Gerar-Cota%C3%A7%C3%A3o-Aglutinada-para-Solicita%C3%A7%C3%B5es-de-Compras-com-Ordem-de-Produ%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20594758740247) Tempo aproximado para leitura: **00:01:00min** **Dúvida**É possível Gerar Cotação Aglutinada para Solicitações de Compras com Ordem de Produção?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Protheus Compras - Versão 12  
  
**Solução**Ao gerar cotação onde as solicitações de compras possuam ordens de produção, deve-se informar o parâmetro "Considera C1\_OP na quebra?" = SIM. Para que ao dar entrada do produto, não haja divergências nas requisições de empenhos do PCP (SD4).  
  
**Observação:** Para os cenários onde as solicitações de compras já foram aglutinadas, deve-se utilizar a rotina MATA381 (Empenho Múltiplos) para ajuste nas requisições de empenhos do PCP (SD4).  
  
**Saiba Mais:**

[Centralizadora Compras](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)  
  
[Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010-)
