---
article_id: 360021633831
category: Escrita Fiscal - Impostos - ICMS
content_hash: 5446f5c86fbe25def9e852b114ac1ef19d14887b5e08bf16bc6e0a2c12556205
fetched_at: '2026-06-28T22:39:24.281515+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Aquisição de consumo
  com base de cálculo de ICMS reduzida
type: support-article
updated_at: '2021-07-20T14:29:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021633831-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Aquisi%C3%A7%C3%A3o-de-consumo-com-base-de-c%C3%A1lculo-de-ICMS-reduzida
---

**Dúvida**Como configurar a TES para nota fiscal de aquisição de consumo ou ativo com base de caclulo reduzida ?  
   
 **Ambiente**Protheus - Compras - Fiscal -  A partir da versão 11.80]  
  
   
**Solução**

Ao adquirir mercadoria para consumo ou ativo com redução de base de calculo configurar:

TES

Calcula icms ( F4\_ICM ) = sim

% red icms ( F4\_BASEICM ) % que tem a tributação do icms

L. fiscal icms ( F4\_LFICM ) = outros

Mat. consumo ( F4\_CONSUMO ) = sim ou outros

sit trib icm ( F4\_SITTRIB ) = 20

Exemplo

Valor da mercadoria = 1.000,00

Red base 51,11% ( parte tributada 48,89 )

1000,00 x 48,89 = 488,90 x 18% = 88,00

Valor contabil = 1.000,00

Base calculo = em branco

ICms = em branco

Outros = 1.000,00

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360018326491/Screenshot_1.png)
