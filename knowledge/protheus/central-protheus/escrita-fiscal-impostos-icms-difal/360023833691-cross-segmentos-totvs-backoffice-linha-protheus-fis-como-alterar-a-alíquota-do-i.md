---
article_id: 360023833691
category: Escrita Fiscal - Impostos - ICMS - Difal
content_hash: b27202a6041a512e80858b2ae9379ca57624bc534d4752b92cd4c07d8842157c
fetched_at: '2026-06-28T22:39:19.266074+00:00'
product: protheus
section_id: 1500001549902
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como alterar a alíquota
  do ICMS ST ou Difal /EC87
type: support-article
updated_at: '2021-09-23T20:14:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023833691-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-alterar-a-al%C3%ADquota-do-ICMS-ST-ou-Difal-EC87
---

**Dúvida**

Como alterar a alíquota do ICMS ST ou Difal/EC87  
   
 **Ambiente**

Protheus - Compras - Faturamento - A partir da versão 11.80  
  
**Solução**

Para alterar a alíquota do icms st ou Difal ec/87 temos duas opções:

1) Criar na exceção fiscal

* **Al.ICMS Dest.:** É a alíquota do ICMS Retido ( ICMS ST ou DIfal /EC87)

2) Alterar o parâmetro

       MV\_ESTICM : para o estado desejado

        exemplo

        SP18

Dessa forma será alterada a alíquota para os próximos pedidos ou entrada de notas fiscais.
