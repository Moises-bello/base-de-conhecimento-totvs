---
article_id: 20284744228375
category: Financeiro - Contas a Pagar
content_hash: bd0c694747edaa5f4a3fbe09fb4317b138903b7a068c82c26c8bbc9fcf43b767
fetched_at: '2026-06-28T22:38:09.586100+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA080 - Pagamento
  via cartão de crédito de compras realizadas pela empresa
type: support-article
updated_at: '2024-01-22T14:59:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20284744228375-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA080-Pagamento-via-cart%C3%A3o-de-cr%C3%A9dito-de-compras-realizadas-pela-empresa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20284744219415) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Existe alguma tratativa ou processo para compras feitas via cartão de crédito?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução**Atualmente no modulo financeiro não existe tratativa para o processo desejado de pagamento de cartão de credito de compras realizadas pela empresa, pois no modulo é especificamente tratado o titulo.  
   
Uma sugestão seria a criação de um motivo de baixa especifico através da rotina **(FINA490)** para controlar as baixas dos títulos a pagar, e posteriormente realizar a baixa movimentando banco de um titulo que foi pago via cartão de credito nas rotina **FINA080** ou **FINA090**, contudo esta sugestão deve ser avaliada, configurada e tratada internamente.

Saiba mais: [Baixas Pagar Manual - FINA080](https://tdn.totvs.com/display/public/PROT/Baixas+Pagar+Manual+-+FINA080+-+Financeiro+-+P12)

                   [Cadastro de Motivo de Baixa - FINA490](https://tdn.totvs.com/display/public/PROT/Cadastro+de+Motivo+de+Baixa+-+FINA490)
