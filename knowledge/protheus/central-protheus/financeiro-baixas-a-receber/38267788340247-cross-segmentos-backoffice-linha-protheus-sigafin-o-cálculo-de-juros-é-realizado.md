---
article_id: 38267788340247
category: Financeiro - Baixas a Receber
content_hash: 42c1e4adb7b0d25ce31cd39f100ba330696ff552fe71c2fb100e1d5d52a8e308
fetched_at: '2026-06-28T22:37:43.809639+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - O cálculo de juros
  é realizado com base na data de vencimento real ou vencimento original
type: support-article
updated_at: '2026-02-09T14:46:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38267788340247-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-O-c%C3%A1lculo-de-juros-%C3%A9-realizado-com-base-na-data-de-vencimento-real-ou-vencimento-original
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38267755503767) Tempo aproximado para leitura: 00**:05 min**  
  
**Dúvida**  
O cálculo de juros e multa no Protheus é realizado com base na data de vencimento real ou na data de vencimento original do título?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Por padrão, o sistema realiza o cálculo de juros e multa utilizando como referência a **data de vencimento original** do título **E1\_VENCTO**.

A data de vencimento real **E1\_VENCREA** é considerada pelo sistema exclusivamente para fins de tolerância em dias não úteis. Isso significa que, se o vencimento original recair em um final de semana ou feriado, o sistema permite o pagamento no próximo dia útil (vencimento real) sem a incidência de encargos.

Entretanto, caso o pagamento **não seja efetuado** até a data de vencimento real, o sistema desconsidera a tolerância e retroage o cálculo dos juros, passando a contabilizá-los a partir da **data de vencimento original**.

###
