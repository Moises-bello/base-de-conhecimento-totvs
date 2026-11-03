---
article_id: 7081330752023
category: Financeiro - Contas a Pagar
content_hash: f64a9482269dee0eb5a22c7d064890d4d487df3402d6227eddc2638cf9954342
fetched_at: '2026-06-28T22:38:09.575983+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Fina080 - Gerar imposto
  (PCC) total na baixa da 1ª parcela '
type: support-article
updated_at: '2023-01-25T21:20:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7081330752023-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Fina080-Gerar-imposto-PCC-total-na-baixa-da-1%C2%AA-parcela
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05 min** **Dúvida**E possível Fina080 - Gerar imposto total na baixa da 1ª parcela ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Somente para títulos de origem do modulo COMPRAS, é possível em titulo de retenção de PCC, ser retido na 1º parcela.  
Para que isso deve-se seguir os parâmetros  conforme documentação abaixo  
MV\_RATPIS: Rateio do imposto na entrada - T. (Default) para ratear os impostos OU .F. para NÃO ratear.   
MV\_RATCOF: Rateio do imposto na entrada - .T. (Default) para ratear os impostos OU .F. para NÃO ratear.   
MV\_RATCSLL: Rateio do imposto na entrada - .T. (Default) para ratear os impostos OU .F. para NÃO ratear.  
  
**Saiba mais**

Não esta disponível no modulo Financeiro independente MV\_BX10925 = 1 ou 2 (BAIXA OU EMISSÃO),  
[Retenção de PIS COFINS CSLL](https://tdn.totvs.com/pages/releaseview.action?pageId=6076816)
