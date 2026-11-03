---
article_id: 33644437707799
category: Financeiro - Contas a Receber
content_hash: 49b635b256ad7e134112bb417df713dd47ba75d8722b965dafcaabce8f012865
fetched_at: '2026-06-28T22:38:14.087462+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA460 - Onde é gravado
  o campo E1_DESCFIN na liquidação
type: support-article
updated_at: '2025-07-22T19:34:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33644437707799-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA460-Onde-%C3%A9-gravado-o-campo-E1-DESCFIN-na-liquida%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33644437684631) Tempo aproximado para leitura: **00:03 min**  
  
**Dúvida**  
O campo **E1\_DESCFIN** é informado em qual campo na liquidação?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA460 - Todas as versões  
  
**Solução**  
Ao realizar a liquidação, o sistema preenche o campo **FO1\_DESCON (Valor do Desconto)** com a informação contida no campo **E1\_DESCFIN**. Quando há múltiplos títulos selecionados e diferentes percentuais de desconto aplicados, o sistema recalcula os valores automaticamente, garantindo a correta geração dos novos movimentos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33644415553559)

**Saiba mais**

[**FINA460 - Liquidação a receber - P12**](https://tdn.totvs.com.br/pages/releaseview.action?pageId=545236275#FINA460Liquida%C3%A7%C3%A3oareceberP12-09.COMISS%C3%83O)
