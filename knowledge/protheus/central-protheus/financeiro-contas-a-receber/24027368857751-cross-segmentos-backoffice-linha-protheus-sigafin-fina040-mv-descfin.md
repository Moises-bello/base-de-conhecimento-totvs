---
article_id: 24027368857751
category: Financeiro - Contas a Receber
content_hash: 7ead10d2831c7f0d5b9726ddbc112276a2a29fa3c1d6983d00625df58da481ca
fetched_at: '2026-06-28T22:38:13.944405+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA040 - MV_DESCFIN
type: support-article
updated_at: '2024-06-10T14:41:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24027368857751-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA040-MV-DESCFIN
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24027368829207) Tempo aproximado para leitura: **01:00 min** **Dúvida**Qual é a funcionalidade do parâmetro **MV\_DESCFIN**?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução**O parâmetro **MV\_DESCFIN** apenas considera o desconto financeiro aplicado no título no campo **"Desc Financ"** será considerado no valor total do percentual de desconto informado ou proporcional ao valor pago, ou seja:  
  
Uma parcela possui um valor de **R$ 1000,00** com desconto de **10%** :  
  
**MV\_DESCFIN = P**  
O % desconto, será liberado proporcionalmente ao valor pago da parcela, ou seja:   
  
Total do título R$ 1000  
Baixa parcial de R$ 500  
% de desconto será R$ 50  
  
  
**MV\_DESCFIN = l**  
O desconto poderá ser concedido integralmente ao pago na parcela.  
  
Total do título R$ 1000  
Baixa parcial de R$ 500  
% de desconto poderá se de até R$ 100,00
