---
article_id: 360028019711
category: Materiais - Compras (SIGACOM)
content_hash: f4c7129043b51a0729dc05864254d4a52ecd9bdaf6a4278a4e38d31b58917304
fetched_at: '2026-06-28T22:41:22.123990+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ponto de entrada para
  validação do registro na solicitação de compras
type: support-article
updated_at: '2022-05-18T21:11:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028019711-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ponto-de-entrada-para-valida%C3%A7%C3%A3o-do-registro-na-solicita%C3%A7%C3%A3o-de-compras
---

**Dúvida**Ponto de entrada para validação do **registro** na solicitação de compras  
  
**Ambiente**Protheus - SIGACOM - A partir da versão 12.1.17  
  
**Solução**

O ponto de entrada **MT110VLD** está localizado na **Solicitação de Compras.**

Este **ponto de entrada** é responsável em validar o registro posicionado da Solicitação de Compras antes de executar as operações de inclusão, alteração, exclusão e cópia.

Se retornar .T., deve executar as operações de inclusão, alteração, exclusão e cópia ou .F. para interromper o processo.

Veja um exemplo através do link: [MT110VLD - Valida o registro na Solicitação de Compras](http://tdn.totvs.com/pages/releaseview.action?pageId=6085449)

***Saiba Mais :***

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
