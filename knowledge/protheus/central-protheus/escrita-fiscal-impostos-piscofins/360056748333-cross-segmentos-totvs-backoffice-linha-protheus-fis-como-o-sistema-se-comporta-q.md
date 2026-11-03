---
article_id: 360056748333
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: b55800239e257feeb56d2e3675f546be1bb13bd8a7a12754dae40f1efe973d61
fetched_at: '2026-06-28T22:39:36.926425+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como o sistema se
  comporta quando o PCC calculado fica abaixo de R$10,00?
type: support-article
updated_at: '2021-06-29T17:31:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056748333-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-o-sistema-se-comporta-quando-o-PCC-calculado-fica-abaixo-de-R-10-00
---

**Dúvida**  
Campos relacionados quando o PCC calculado é igual ou menor que R$10,00.  
  
**Ambiente**  
Protheus– Compras – A partir da versão 11.80.  
  
**Solução**

Cálculo abaixo de dez reais:

Campos E2\_PRETPIS/PRETCOF/PRETCSL = campos populados = 1 (valor calculado e armazenado)

Campos E2\_PIS/E2\_COF/E2\_CSLL = não preenchidos, pois neste momento não haverá retenção

Cálculo acima de dez reais:

Campos E2\_PRETPIS/PRETCOF/PRETCSL = campos não preenchidos, pois os impostos serão pagos nesta nota (acima de dez ou pelo fator da cumulatividade)

Campos E2\_PIS/E2\_COF/E2\_CSLL = confirmação dos impostos que serão gerados no financeiro para retenção (tipo TX).
