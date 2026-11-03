---
article_id: 360041762913
category: Call Center - Telecobrança
content_hash: 612334698474d620c18892b668f31adba70b846b6c32aeeee632b2f83643fba9
fetched_at: '2026-06-28T22:41:28.746241+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK-Campo Observação
  do Histórico de Cobrança não carrega as informações.
type: support-article
updated_at: '2022-06-22T17:43:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041762913-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Campo-Observa%C3%A7%C3%A3o-do-Hist%C3%B3rico-de-Cobran%C3%A7a-n%C3%A3o-carrega-as-informa%C3%A7%C3%B5es
---

**Dúvida**

Campo de Observação do Histórico de cobrança não consta as informações que foram preenchido no campo: ACF\_OBS.  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- A partir da versão 12.1.17

**Solução**

Quando o usuário realiza a Consulta do Histórico de Cobrança por meio da funcionalidade da Posição do Cliente utilizando a opção de Seleção de Filiais ou não, as informações não são apresentadas no campo: Observação, conforme os dados do campo: ACF\_OBS. 

E para correção é necessário aplicar os patchs das rotinas: TMKC020 e FINC010, que estão disponíveis no link abaixo:

Saiba mais: <https://tdn.totvs.com/pages/viewpage.action?pageId=528915371>
