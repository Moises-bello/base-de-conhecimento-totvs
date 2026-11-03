---
article_id: 360024575534
category: Escrita Fiscal - Error.log
content_hash: 8b9a3642fc84274d7e457226653f99751b39c8e524fb15b932b829d8110b67c3
fetched_at: '2026-06-28T22:39:32.907862+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: 'MP - FIS - Data width error - Field: CD2_PREDBC Value: 100.000000 on XFISATUSF3(IMPXFIS.PRW)'
type: support-article
updated_at: '2022-12-23T12:54:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024575534-MP-FIS-Data-width-error-Field-CD2-PREDBC-Value-100-000000-on-XFISATUSF3-IMPXFIS-PRW
---

**Dúvida**Data width error - Field: CD2\_PREDBC Value: 100.000000 on XFISATUSF3(IMPXFIS.PRW)  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
Para solução do error.log referenciando o campo CD2\_PREDBC, será necessário verificar todos os campos que envolvem redução:

* F4\_BASEICM

* F4\_BSICMST

* F7\_BASEICM

* F7\_BSICMST

O tamanho destes campos devem ser o mesmo do CD2\_PREDBC e vice versa. Sendo assim, compare no módulo de Configurador o tamanho destes campos, e caso haja divergência será necessário que seja feito o ajuste.
