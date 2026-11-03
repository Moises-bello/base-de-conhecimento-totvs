---
article_id: 38267755458583
category: Financeiro - Contas a Receber
content_hash: 9878bf540a8d14eee719ea6319ed694ec0d4889564475bc83b4a629eb89f4450
fetched_at: '2026-06-28T22:38:12.656586+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - O cálculo de juros
  é realizado com base na data de vencimento real ou vencimento original
type: support-article
updated_at: '2026-02-09T14:46:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38267755458583-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-O-c%C3%A1lculo-de-juros-%C3%A9-realizado-com-base-na-data-de-vencimento-real-ou-vencimento-original
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38267788283159) Tempo aproximado para leitura: 00**:05 min**  
  
**Dúvida**  
O cálculo de juros e multa no Protheus é realizado com base na data de vencimento real ou na data de vencimento original do título?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Por padrão, o sistema realiza o cálculo de juros e multa utilizando como referência a **data de vencimento original** do título **E1\_VENCTO**.

A data de vencimento real **E1\_VENCREA** é considerada pelo sistema exclusivamente para fins de tolerância em dias não úteis. Isso significa que, se o vencimento original recair em um final de semana ou feriado, o sistema permite o pagamento no próximo dia útil (vencimento real) sem a incidência de encargos.

Entretanto, caso o pagamento **não seja efetuado** até a data de vencimento real, o sistema desconsidera a tolerância e retroage o cálculo dos juros, passando a contabilizá-los a partir da **data de vencimento original**.

###
