---
article_id: 11315265150231
category: Financeiro - Contas a Receber
content_hash: 0a509ca5fc9315fa0115896ea87b900cf6fc33e7aec8cb956a19693752cb44c8
fetched_at: '2026-06-28T22:38:14.090329+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA460 - Por qual
  motivo é criado o ISS com a alíquota do parâmetro MV_ALIQISS ao invés de utilizar
  a alíquota do produto
type: support-article
updated_at: '2023-01-02T15:10:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11315265150231-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA460-Por-qual-motivo-%C3%A9-criado-o-ISS-com-a-al%C3%ADquota-do-par%C3%A2metro-MV-ALIQISS-ao-inv%C3%A9s-de-utilizar-a-al%C3%ADquota-do-produto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Ao gerar o pedido de Venda com ISS (imposto) vindo do módulo faturamento, ao utilizar a rotina de negociação "FINA460 liquidação". Por qual motivo é criado o ISS com a alíquota do parâmetro MV\_ALIQISS ao invés de utilizar a alíquota do produto?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**No momento da negociação feita através da **rotina "FINA460 - liquidação**" caso utilize uma natureza diferente que está no pedido, o sistema irá utilizar a alíquota do parâmetro **MV\_ALIQISS** ao invés de utilizar a alíquota que está no produto. Neste caso terá que utilizar a mesma natureza que está no pedido.   
  
**Saiba mais**  
[FINA460 - Liquidação a receber - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=545236275)
