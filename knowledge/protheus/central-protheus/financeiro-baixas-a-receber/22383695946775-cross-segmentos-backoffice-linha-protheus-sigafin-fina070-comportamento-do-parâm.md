---
article_id: 22383695946775
category: Financeiro - Baixas a Receber
content_hash: f42a317cd2226d6d1d23bc622e3df0f72988b9b24ce7ec648e1aa139be710233
fetched_at: '2026-06-28T22:37:43.787200+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA070 - Comportamento
  do parâmetro MV_DESCFIN
type: support-article
updated_at: '2025-07-30T17:41:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22383695946775-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA070-Comportamento-do-par%C3%A2metro-MV-DESCFIN
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22383695916183) Tempo aproximado para leitura: **05:00 min** **Cenário:**Comportamento do parâmetro **MV\_DESCFIN**  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
  
**Solução**

O parâmetro ***MV\_DESCFIN*** define a forma de aplicação do desconto financeiro sobre os títulos na rotina de Baixas a Receber (FINA070). Pode ser configurado com os seguintes valores:

* **'I'** – o desconto financeiro será aplicado integralmente no primeiro pagamento;
* **'P'** – o desconto financeiro será proporcional ao valor pago em cada parcela.

O parâmetro ***MV\_DESCFI**N* considera exclusivamente o valor de desconto financeiro informado no campo ***'Desc. Financ.'* (*E1\_DESCFIN*)** do título.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22383695919127)

O desconto financeiro poderá ser considerado de forma integral ou proporcional ao valor pago, conforme a configuração do parâmetro***MV\_DESCFIN*.**

**Exemplo:**

* Valor total da parcela: R$ 2.500,00
* Desconto financeiro: 10%

**Configuração: *MV\_DESCFIN = P***  
Neste caso, o desconto será aplicado proporcionalmente ao valor pago.  
Se for realizada uma baixa parcial no valor de R$ 1.000,00, o desconto concedido será proporcional, ou seja, R$ 100,00 (10% de R$ 1.000,00)."

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22383695922327)

Quando o parâmetro ***MV\_DESCFIN*** está configurado como 'I', o desconto financeiro é concedido integralmente, independentemente do valor pago na baixa.

**Exemplo:**

* Valor total do título: R$ 2.500,00
* Desconto financeiro: 10%

Se for realizada uma baixa parcial de R$ 500,00, o sistema poderá considerar o desconto total de R$ 250,00 (10% de R$ 2.500,00), já deduzido do valor informado para a baixa.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22383700515863)  
  
É possível alterar o valor de desconto cedido, caso este deva ser menor que o percentual máximo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22383695928343)

**Saiba mais**[MV\_DESCFIN - Desconto financeiro dos títulos](https://tdn.totvs.com/pages/releaseview.action?pageId=6070814)
