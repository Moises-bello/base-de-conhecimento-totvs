---
article_id: 4402387710359
category: Financeiro - Baixas a Receber
content_hash: 09989f4321b21ddd0641a94595a29b8e5bc7feb2e40ee6e5fba868ffb973ad8d
fetched_at: '2026-06-28T22:37:43.710068+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA070 - Baixa a receber
  não considera o valor mínimo PCC informado no parâmetro MV_VL13137  em títulos com
  origem do faturamento
type: support-article
updated_at: '2025-07-30T16:53:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402387710359-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA070-Baixa-a-receber-n%C3%A3o-considera-o-valor-m%C3%ADnimo-PCC-informado-no-par%C3%A2metro-MV-VL13137-em-t%C3%ADtulos-com-origem-do-faturamento
---

**Dúvida**No módulo financeiro, ao efetuar uma baixa a receber FINA070 em títulos que calcula PCC, não é considerado o valor mínimo informado no parâmetro MV\_VL13137 em títulos com origem do módulo faturamento (Pedido de venda, MATA410)?  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Financeiro - FINA070 - Todas as versões  
  
**Solução**Independentemente de o PCC ser calculado na baixa ou na emissão, o pedido de venda considera, inicialmente, o campo *Ret. Operação*, localizado na guia 'Impostos' do Cadastro de Produtos (MATA010). Para que seja aplicado o valor mínimo de retenção definido no parâmetro ***MV\_VL13137***, é necessário ajustar o campo *Ret. Operação* para 'Não'.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402387446935)

**Importante**Esse procedimento terá efeito apenas para baixas originadas de pedidos de venda, realizadas por meio do módulo de Faturamento, e nos casos em que o valor calculado do PCC seja inferior ao definido no parâmetro ***MV\_VL13137***.

**Saiba mais**[Retenção de PIS COFINS CSLL](https://tdn.totvs.com/pages/releaseview.action?pageId=6076816)
