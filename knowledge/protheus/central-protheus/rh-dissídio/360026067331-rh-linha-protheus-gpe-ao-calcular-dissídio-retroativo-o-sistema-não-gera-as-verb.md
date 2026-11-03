---
article_id: 360026067331
category: RH - Dissídio
content_hash: 18c34cbb3ec3b3cf4cf1ee812773df06cc84a716de773c6cfc699b5225d07546
fetched_at: '2026-06-28T22:43:43.180623+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Ao calcular dissídio retroativo, o sistema não
  gera as verbas de férias para o dissídio
type: support-article
updated_at: '2025-08-21T12:57:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026067331-RH-Linha-Protheus-GPE-Ao-calcular-diss%C3%ADdio-retroativo-o-sistema-n%C3%A3o-gera-as-verbas-de-f%C3%A9rias-para-o-diss%C3%ADdio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34341612528919) Tempo aproximado para leitura: 00:00:30 min**

**Ocorrência**Ao calcular dissídio retroativo de um funcionário que teve férias, sistema não gera as verbas de férias no cálculo do dissidio.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 11.80  
  
**Causa**O cálculo das verbas de férias dentro do dissídio retroativo é realizado no fonte GPEXCAL3 na função fCDifFerias, esta função é chamada pelo roteiro S\_CADIFFER dentro do roteiro de cálculo da folha de pagamento. Para que o cálculo ocorra, o roteiro S\_CADIFFER não pode estar desabilitado no roteiro principal da folha.  
  
**Solução**Caso as verbas de férias não estejam sendo calculadas no dissídio, verificar se o roteiro S\_CADIFFER está habilitado.

**Saiba Mais:**  
[Página Centralizadora do Dissídio (GPEM690)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
