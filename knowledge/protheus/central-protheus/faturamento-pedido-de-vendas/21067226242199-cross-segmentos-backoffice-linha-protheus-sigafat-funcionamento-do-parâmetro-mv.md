---
article_id: 21067226242199
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 17cbf97b1df879698b1bf7722fefef7fcc847f1a777736937d31c9b27dcf6585
fetched_at: '2026-06-28T22:38:42.474928+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - SIGAFAT - Funcionamento do
  parâmetro MV_FATNATR
type: support-article
updated_at: '2026-03-02T19:23:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21067226242199-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Funcionamento-do-par%C3%A2metro-MV-FATNATR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21067226212631) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Qual é funcionamento do parâmetro MV\_FATNATR?  
  
**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - A partir da versão 12

**Solução**Esse parâmetro é válido no pedido de venda, quando:

* O cliente possuir o campo "Recolhe IRRF (A1\_RECIRRF)" = '2 - Não'
* O produto nos itens possuir o campo "Impos.Renda (B1\_IRRF)" = "S - Sim".
* Natureza do Cliente (A1\_NATUREZ) ou Pedido de venda (C5\_NATUREZ) possuir em si os campos "Recolhe IRRF (ED\_RECIRRF)" = ' ', '2', '3' e "Calcula IRRF (ED\_CALCIRF)" = '1 - Sim'.

**MV\_FATNATR** = .T.

Ao salvar o pedido de venda sem informar a natureza de rendimentos no campo **"Nat. Ren (C6\_NATREN)"** dispara um aviso informativo (se tudo estiver conforme campos acima) ao usuário final que aquele item do pedido não está com a natureza de rendimento preenchida, e não será considerada na EFD-REINF.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21067207367703)

**MV\_FATNATR** = .F.

Não dispara o HELP ao salvar o pedido de venda.

**OBSERVAÇÃO 1:** Ao incluir um item no pedido de venda, não é automaticamente puxado mais a natureza de rendimentos no campo **"Nat. Ren (C6\_NATREN)".**

**OBSERVAÇÃO 2:** Em cópias de pedidos de venda que possuem o campo **"Nat. Ren (C6\_NATREN)"** preenchido, o valor também será copiado no novo pedido cópia.

**Saiba mais:**

* [Campo "Nat. Rend." (C6\_NATREN) para REINF 2.1.2](https://totvssuporte.zendesk.com/knowledge/editor/01GSG1VE1QHSR1SPMQ251VDT8X/pt-br?brand_id=1509248&return_to=%2Fhc%2Fpt-br%2Farticles%2F12494179468183)
* [Help: NATREN na inclusão da Natureza de Rendimento no Pedido de Venda](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17687168113047-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-NATREN-na-inclus%C3%A3o-da-Natureza-de-Rendimento-no-Pedido-de-Venda)
