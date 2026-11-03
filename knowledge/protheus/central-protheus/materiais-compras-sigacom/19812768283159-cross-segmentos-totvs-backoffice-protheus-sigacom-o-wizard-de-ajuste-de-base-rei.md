---
article_id: 19812768283159
category: Materiais - Compras (SIGACOM)
content_hash: 7e91b7f3d5ef01bd706d24931053c95008459b86f9c4de9f97cb3846acfedd47
fetched_at: '2026-06-28T22:41:22.005412+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - O Wizard de ajuste
  de base Reinf não gera DHR e FKW para títulos sem saldo?
type: support-article
updated_at: '2023-12-13T17:27:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19812768283159-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-O-Wizard-de-ajuste-de-base-Reinf-n%C3%A3o-gera-DHR-e-FKW-para-t%C3%ADtulos-sem-saldo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19812756875287) Tempo aproximado para leitura: **03:00:00 min****Ocorrência**Executei o Wizard de ajuste de base Reinf , não preencheu a natureza de rendimento e também não gerou DHR e FKW para notas com título sem saldo. Porque isso ocorreu?  
**Ambiente**Protheus – Compras – A partir da versão 12.1.33  
  
**Causa**

Realmente isso não será possível. O wizard não irá preencher natureza de rendimento , nem gerar DHR e FKW em notas cujo saldo do título esteja zerado, pois o wizard efetua as validações abaixo para que as informações sejam gravadas na DHR e na FKW.  
  
\* Se há natureza de Rendimentos no Cadastro do Produto (F2Q\_NATREN)

\* Se o campo E2\_SALDO > 0

\* Se os campos abaixo estão preenchidos com valores   
- SD1->D1\_BASEIRR > 0   
- SD1->D1\_BASEPIS > 0   
- SD1->D1\_BASECOF > 0   
- SD1->D1\_BASECSL > 0

**Solução**Caso essas verificações sejam negativas, o wizard realmente não irá gravar DHR nem FKW. Nesses casos, o lançamento deve ser realizado manualmente no TAF.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [Wizard de configuração de ajuste de base Reinf](https://tdn.totvs.com/pages/releaseview.action?pageId=802753445)
* [Ajuste - Vínculo da Natureza de Rendimento para títulos lançados antes da vigência do EFD-Reinf Bloco 40](https://tdn.totvs.com/pages/releaseview.action?pageId=786554814)
