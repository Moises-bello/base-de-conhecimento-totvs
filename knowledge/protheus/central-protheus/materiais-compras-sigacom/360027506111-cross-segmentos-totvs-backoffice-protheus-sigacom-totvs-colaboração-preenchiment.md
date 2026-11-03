---
article_id: 360027506111
category: Materiais - Compras (SIGACOM)
content_hash: 1b951eae04142a03f58123f98d4cec3b93b0cf965f8ec6708ae031943b423bcd
fetched_at: '2026-06-28T22:41:25.364953+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Totvs Colaboração -
  Preenchimento Campo Data Emissao (DS_EMISSA)
type: support-article
updated_at: '2024-11-18T19:32:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027506111-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Totvs-Colabora%C3%A7%C3%A3o-Preenchimento-Campo-Data-Emissao-DS-EMISSA
---

**Dúvida**

Totvs Colaboração - Preenchimento Campo Data Emissao (DS\_EMISSA)

**Ambiente**Microsiga Protheus – Totvs Colaboração – A partir da versão 12  
  
**Solução**O campo DS\_EMISSA é preenchido com a data de emissão informada no XML da NF-e, ao importar a nota via Totvs Colaboração.

Para localizar a data de emissão dentro do XML o sistema sempre irá buscar da TAG  <dhEmi>2024-10-09T13:40:00-03:00</dhEmi>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27888714291351)

Devido a tabela SDS conter campos provenientes da tabela SF1 (Cabeçalho das NF de Entrada), herdou o conteúdo de inicializador por data base, porem será sempre alimentado pela Data de Emissão informada no XML da NF-e.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
