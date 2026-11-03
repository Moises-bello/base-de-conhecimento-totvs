---
article_id: 360021439192
category: Escrita Fiscal - Impostos - ICMS
content_hash: 9cb93597c3dc81c6e2fba1006cc72e6bf44f20cd5258b869d656028ff72e2283
fetched_at: '2026-06-28T22:39:24.245183+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Sistema exibe a linha
  do ICMS complementar (DIFAL) com o valor zerado na planilha do pedido de venda
type: support-article
updated_at: '2024-09-23T20:42:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021439192-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Sistema-exibe-a-linha-do-ICMS-complementar-DIFAL-com-o-valor-zerado-na-planilha-do-pedido-de-venda
---

**Dúvida**Por qual motivo o sistema está exibindo a linha do ICMS complementar (DIFAL) com o valor zerado na planilha do pedido de venda?  
  
**Ambiente**Protheus – Livros Fiscais– A partir da versão 12.1.16  
  
**Solução**De acordo com a emenda constitucional 87/2015 a partir de 2019 todo o valor do diferencial de alíquota passou a ser recolhido para o estado de destino. Desse modo a linha do ICMS complementar que representa os valores da origem ficarão zeradas.

O sistema atende essa regra através do parâmetro MV\_PPDIFAL.

MV\_PPDIFAL = {{2016,40,60},{2017,60,40},{2018,80,20},{2019,100,0},{2020,100,0},{2021,100,0},{2022,100,0},{2023,100,0},{2024,100,0}}
