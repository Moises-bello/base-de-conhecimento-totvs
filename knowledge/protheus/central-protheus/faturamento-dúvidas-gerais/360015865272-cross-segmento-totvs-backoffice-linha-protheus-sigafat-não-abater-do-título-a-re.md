---
article_id: 360015865272
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 036bbe5e931ad7da739d99febdffae7769bd163dc476f7fb8c0e1e659cb52378
fetched_at: '2026-06-28T22:38:32.804480+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Não abater do
  título a receber o valor do frete proporcional ao item que não gera duplicata
type: support-article
updated_at: '2021-08-26T14:10:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015865272-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-N%C3%A3o-abater-do-t%C3%ADtulo-a-receber-o-valor-do-frete-proporcional-ao-item-que-n%C3%A3o-gera-duplicata
---

**Ocorrência**Ao incluir no mesmo Pedido de Vendas: TES que gera duplicata e TES que não gera duplicata; e atribuir um valor de despesa acessória, como frete, o sistema rateia esse valor de frete entre os itens e o proporcional ao item que não gera duplicata não é levado para o título a Receber.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 11.80.  
  
**Causa**Os valores de despesas, frete, seguro são sempre rateados por item. Esse rateio é necessário devido à tributação da despesa acessória que deve ser compatível com o valor do Item.

Detalhes de como é realizado o rateio, consulte em: **[Cálculo do Rateio das Despesas Acessórias (Frete / Seguro / Despesa) na Geração do Documento de Saída](https://tdn.totvs.com/x/mDc-Dg)**

Desta forma, se um dos itens está com TES que não gera duplicata (F4\_DUPLIC = Não), então o valor de despesa acessória atribuído a ele, de igual modo, não irá gerar duplicata.

**Solução**

* **1ª Opção:** Emitir Pedidos de Venda distintos.  
  Um Pedido para os itens que geram duplicata e outro Pedido para os itens que não geram;  
  Emitir notas de saída distintas, ou mesmo, aglutinar ambos os Pedidos numa única nota Fiscal: **[Aglutinar Pedidos de Venda similares no mesmo Documento de Saída](https://tdn.totvs.com/x/nkJtDQ)**
* **2ª Opção:** Deduzir valor da mercadoria da duplicata, ao invés de não gerar.  
  Utilize para este item um TES que gera duplicata: F4\_DUPLIC = SIM;  
  E configure no TES o campo F4\_AGREG = F definindo que Deduz o Valor da Mercadoria na Duplicata.

**Saiba mais:**  [**Não abater do título a receber o valor do frete proporcional ao item que não gera duplicata**](https://tdn.totvs.com/x/1ZNSDg)
