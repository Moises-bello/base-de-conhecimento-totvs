---
article_id: 360044239494
category: Materiais - Compras (SIGACOM)
content_hash: 4ff569a5b9b47ead3d55b4a6d4579a927474818a692dffd3c5e96116650857af
fetched_at: '2026-06-28T22:41:20.235846+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Na rotina Análise
  de Cotação (MATA161) ocorre o erro: type mismatch on compare on A161PROP(MATA161.PRW)'
type: support-article
updated_at: '2022-05-18T21:05:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044239494-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Na-rotina-An%C3%A1lise-de-Cota%C3%A7%C3%A3o-MATA161-ocorre-o-erro-type-mismatch-on-compare-on-A161PROP-MATA161-PRW
---

**Ocorrência**

Na rotina Análise de Cotação (MATA161) ocorre o erro: type mismatch on compare on A161PROP(MATA161.PRW)  
  
**Ambiente**

Protheus – Financeiro – A partir da versão 12  
  
**Causa**

Esse incidente normalmente ocorre, pois o pergunte **MTA161** (SX1) da ordem 1 está diferente do tipo **carácter** (**X1\_TIPO**).

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

Ajuste o tipo do pergunte **MTA161** da ordem 1 para carácter

**Documentações complementares:**

* [Perguntas (CFGX031 - SIGACFG)](https://tdn.totvs.com/pages/releaseview.action?pageId=306855563)
* [SX1 - Perguntas do usuário](https://tdn.totvs.com/pages/viewpage.action?pageId=22479548)
* [MP-FAT-Grupo de Perguntas da Exclusão da Nota](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028706012-MP-FAT-Grupo-de-Perguntas-da-Exclus%C3%A3o-da-Nota?source=search)
