---
article_id: 7492272638871
category: Materiais - Compras (SIGACOM)
content_hash: b17f2f9f322c424e99caef84bb382bab04e0452af0bcef64e1dbfbd6f3d03d80
fetched_at: '2026-06-28T22:41:11.640322+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Error.log SELECT
  XI_EVENTID FROM SXI SXI WHERE  SXI.XI_EVENTID = '036' AND SXI.D_E_L_E_T_= ' ' on
  __EXECSQL(APLIB300.PRW) ao Cadastrar Fornecedor
type: support-article
updated_at: '2022-07-15T14:12:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7492272638871-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Error-log-SELECT-XI-EVENTID-FROM-SXI-SXI-WHERE-SXI-XI-EVENTID-036-AND-SXI-D-E-L-E-T-on-EXECSQL-APLIB300-PRW-ao-Cadastrar-Fornecedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao cadastrar um Fornecedor é apresentado o error.log SELECT XI\_EVENTID FROM SXI SXI WHERE SXI.XI\_EVENTID = '036' AND SXI.D\_E\_L\_E\_T\_= ' ' on \_\_EXECSQL(APLIB300.PRW)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**

O erro é devido à não existir no ambiente em questão a tabela SXI.

Acesse a rotina "Miscelanea -> Inscr Event Viewer" e cadastre um evento qualquer para criar a tabela SXI, e após criar a tabela realizar um novo teste.

![imagem1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7492170059671/imagem1.png)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
