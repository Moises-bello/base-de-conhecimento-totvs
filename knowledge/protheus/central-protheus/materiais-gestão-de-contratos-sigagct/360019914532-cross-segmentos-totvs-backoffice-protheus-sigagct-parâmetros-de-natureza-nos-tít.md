---
article_id: 360019914532
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: e4f98a4237b22c20ccd6631ff1788fd762e522cc15d4e24f0b4f5844cf5712ad
fetched_at: '2026-06-28T22:37:20.102327+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Parâmetros de natureza
  nos títulos financeiros gerados pelo módulo Gestão de Contratos
type: support-article
updated_at: '2025-11-27T20:02:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019914532-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Par%C3%A2metros-de-natureza-nos-t%C3%ADtulos-financeiros-gerados-pelo-m%C3%B3dulo-Gest%C3%A3o-de-Contratos
---

**Dúvida**

Parâmetros de natureza nos títulos financeiros gerados pelo módulo Gestão de Contratos  
  
**Ambiente**  
Protheus – Gestão de Contratos – A partir da versão 12.1.17

**Solução**

A regra utilizada pelo sistema, para preenchimento da natureza nos títulos financeiros gerados pelo módulo Gestão de Contratos é a seguinte:

* Títulos provisórios (PR) referente às parcelas do Cronograma Financeiro, gerados na alteração da situação do contrato para Vigente:

O sistema utiliza a natureza informada no campo **CN9\_NATURE**, caso o campo não contenha a informação, o sistema buscará a natureza nos parâmetros: **MV\_CNNAT** (Contrato de Compra) ou **MV\_CNNATCL**(Contrato de Venda).

* Títulos gerados no encerramento da medição:

A configuração necessária para a natureza usada nas medições, o sistema utiliza a natureza informada no campo **CN9\_NATURE**, caso o campo não contenha a informação, o sistema buscará a natureza no parâmetro: **MV\_CNNATMD**.

***Saiba Mais :***

[Parâmetros de natureza nos títulos financeiros gerados pelo módulo Gestão de Contratos](http://tdn.totvs.com/pages/releaseview.action?pageId=244425645)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
