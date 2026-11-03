---
article_id: 360026741492
category: Materiais - Compras (SIGACOM)
content_hash: 911fa7af5be52273200c18981f6ba162f9604ce676afba0550d8daf99acbf519
fetched_at: '2026-06-28T22:41:22.079728+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Pedido de compras -
  vínculo com solicitação de compras não leva Valor unitário
type: support-article
updated_at: '2022-05-18T21:08:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026741492-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Pedido-de-compras-v%C3%ADnculo-com-solicita%C3%A7%C3%A3o-de-compras-n%C3%A3o-leva-Valor-unit%C3%A1rio
---

**Dúvida**

Ao vincular a solicitação de compras a um pedido, o campo Valor Unitário (C1\_VUNIT), não é levado para a tabela SC7.

**Ambiente**Microsiga Protheus – Compras – A partir da versão 11.80  
  
**Solução**

Comportamento padrão sistêmico, onde, ao 'vincular' a solicitação de compras no pedido de compras, somente levará os dados referentes a produto e quantidade. Para realizar este tratamento a totvs disponibiliza os pontos de entradas abaixo:

MT120C1D - Acrescenta elementos no array dos dados

<http://tdn.totvs.com/display/public/PROT/MT120C1D+-+Acrescenta+elementos+no+array+dos+dados>

MT120C1C - Acrescenta os títulos das colunas acrescidas

<http://tdn.totvs.com/pages/viewpage.action?pageId=6085468>

A120F4CP - Substituição de Função de Carga

<http://tdn.totvs.com/pages/viewpage.action?pageId=6085264>

Saiba Mais :

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
