---
article_id: 360025647814
category: Escrita Fiscal - Impostos - ICMS
content_hash: ba97ab176819bc0ba4c81771ec1fdba0fb990f28dae9ca5e9ba381f73606295f
fetched_at: '2026-06-28T22:39:26.000794+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Rejeição 693 - Alíquota
  de ICMS superior a definida para a operação interestadual - Venda Interestadual
  Cons Final - Não Contribuinte
type: support-article
updated_at: '2026-04-23T12:56:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025647814-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Rejei%C3%A7%C3%A3o-693-Al%C3%ADquota-de-ICMS-superior-a-definida-para-a-opera%C3%A7%C3%A3o-interestadual-Venda-Interestadual-Cons-Final-N%C3%A3o-Contribuinte
---

**Dúvida**

Ao transmitir documento fiscal é apresentado a rejeição "693 - Alíquota de ICMS superior a definida para a operação interestadual"

Onde é definido no Protheus o valor da alíquota de ICMS em operações interestaduais de vendas para consumidor final?

**Ambiente**

Protheus - Livro Fiscais - A partir da versão 11.80  
  
**Solução**Verificar o cadastro do cliente:  
  
A1\_Contrib = Não ( 2 ), logo deve ser realizado as configurações abaixo:  
  
No pedido de vendas = Consumidor Final  
  
TES  
  
Calcula icms = Sim  
Calc dif icms = Sim  
Calc difal = Sim  
CST = 20  
Material Consumo = Sim  
  
Dessa forma será calculado 7% ou 12%, referente a alíquota de venda para o estado de destino.   
  
Quando se realiza venda a um cliente não contribuinte do ICMS, deve ser calculado DIFAL da EC/87 para não haver erro na emissão do documento fiscal.
