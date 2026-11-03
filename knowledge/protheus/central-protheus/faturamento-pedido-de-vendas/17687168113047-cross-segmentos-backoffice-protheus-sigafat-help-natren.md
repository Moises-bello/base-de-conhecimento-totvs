---
article_id: 17687168113047
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 29ca07e8a2f06a11a0171ce98eb1f7efce312f0314b18f15413dab75c2d62a59
fetched_at: '2026-06-28T22:38:39.806866+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Help "NATREN"
type: support-article
updated_at: '2025-04-29T19:22:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17687168113047-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-NATREN
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17687160608151) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como resolver o Help "NATREN" ao realizar a inclusão da "Natureza de Rendimento (C6\_NATREN)" e (UB\_NATREN)" nos itens?

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da versão 12.1.33

**Solução**

**OBS:** Essa documentação serve também para o módulo Call Center (SIGATMK).

A geração do **REINF** no módulo de **Faturamento**, ocorre apenas em casos de **auto-retenção**, enviando seus registros para o bloco **R-4080**, sendo assim as naturezas de rendimento, utilizadas nesse bloco são iniciadas em 20:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17686935067799)

* Para não ser validado se foi informado natureza de rendimentos ou não, deixe o MV\_FATNATR = .F.

* Para não ser levado valor ao campo "Natureza de rendimentos (C6\_NATREN)", não configure o produto na SB1 ou preencha o parâmetro MV\_CADPROD.

**Saíba mais:**

[DT Pedidos de Venda - Assistente de validação do preenchimento da Natureza de Rendimento](https://tdn.totvs.com/pages/releaseview.action?pageId=817638151)

[Webinar | MP - SIGATAF - Evento: Processo EFD REINF](https://youtu.be/Miy-B10g_CM?si=28-DilTRWyNjVH87)

[Cross Segmentos - Backoffice (Linha Protheus) - SIGAFAT - Campo "Nat. Rend." (C6\_NATREN) para REINF 2.1.2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12494179468183-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-FATURAMENTO-Campo-C6-NATREN-Nat-Rend-para-REINF-2-1-1?source=search)

[Campo "Nat. Rend." (C6\_NATREN) para REINF 2.1.2](https://totvssuporte.zendesk.com/knowledge/editor/01GSG1VE1QHSR1SPMQ251VDT8X/pt-br?brand_id=1509248&return_to=%2Fhc%2Fpt-br%2Farticles%2F12494179468183)
