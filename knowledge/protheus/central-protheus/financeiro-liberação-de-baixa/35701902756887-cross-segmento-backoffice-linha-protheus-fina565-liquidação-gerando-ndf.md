---
article_id: 35701902756887
category: 'Financeiro - Liberação de Baixa '
content_hash: d8f6c1eb2af36a42dc0fdb229b34e74e6ec7f22c31f413faf54e4ec399508159
fetched_at: '2026-06-28T22:37:33.008855+00:00'
product: protheus
section_id: 35057590391959
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA565 - Liquidação gerando NDF
type: support-article
updated_at: '2026-03-04T16:48:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35701902756887-Cross-Segmento-Backoffice-Linha-Protheus-FINA565-Liquida%C3%A7%C3%A3o-gerando-NDF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35701902740887) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Ao realizar a liquidação, está sendo gerada uma NDF. Como proceder nesse caso?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Quando os títulos gerados apresentam valor superior ao total informado na liquidação, o sistema gera automaticamente uma Nota de Débito do Fornecedor (NDF) correspondente à diferença. O prefixo da NDF será “LIQ”, o número corresponderá ao número da liquidação, e o tipo será definido como “NDF”.

Exemplo de liquidação no valor de R$ 10.000, acrescentando um valor de R$ 5000.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35701902741527)

Título liquidado, gerando a NDF.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35701911811479)

A liquidação tem como finalidade permitir a renegociação do valor do débito do fornecedor. Assim, quando é informado na liquidação um valor superior ao devido, o sistema gera uma NDF como crédito para o fornecedor.

Caso seja necessário incluir um valor adicional, este deve ser inserido no título antes da liquidação, para que o valor seja corretamente agregado ao total do título.

**Saiba mais**

[Liquidação a Pagar - FINA565](https://tdn.totvs.com/pages/releaseview.action?pageId=312167645)
