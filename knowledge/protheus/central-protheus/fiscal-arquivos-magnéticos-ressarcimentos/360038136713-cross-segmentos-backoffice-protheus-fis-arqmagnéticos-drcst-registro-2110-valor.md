---
article_id: 360038136713
category: Fiscal Arquivos Magnéticos - Ressarcimentos
content_hash: 2399a870c8cc04ebbf4fb9cf7e19aa788e312b218054be54398650a2e913066b
fetched_at: '2026-06-28T22:42:12.706991+00:00'
product: protheus
section_id: 1500001546642
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DRCST - Registro
  2110: Valor divergente entre o informado e o calculado.'
type: support-article
updated_at: '2022-08-18T17:58:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038136713-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DRCST-Registro-2110-Valor-divergente-entre-o-informado-e-o-calculado
---

**Ocorrência**Ao validar o arquivo da DRCST está ocorrendo o seguinte erro de validação:

Registro 2110: Valor divergente entre o informado e o calculado.  
Campo: VL\_ICMS\_IND\_S\_OE  
Valor informado: 19,72, Valor calculado: 19,74

Ou

Registro 2110: Valor divergente entre o informado e o calculado.  
Campo: VL\_ICMS\_ST\_IND\_S\_OE  
Valor informado: 33,26, Valor calculado: 33,24  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80.  
 **Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Conforme o Boletim Técnico da rotina, para corrigir os erros de arredondamento, é necessário aplicar o dicionário diferencial acumulado do Fiscal.  
  
Dicionário diferencial acumulado:   
<https://suporte.totvs.com/portal/p/10098/download#detail/765125>    
  
Boletim Técnico:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=484701377>
