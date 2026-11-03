---
article_id: 4411606682391
category: TAF - REINF
content_hash: 3ee6b97501118361bb77a185c82c6af052faf922a49239ed81f36352e74ae079
fetched_at: '2026-06-28T22:41:34.703044+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Layout T013 -  Ident
  Proces ou Ato Conce ( T9Q_NUMPRO ) não existe na base de dados e  Chave Cod. Suspensao
  ( T9Q_IDSUSP )
type: support-article
updated_at: '2023-03-31T17:14:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411606682391-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Layout-T013-Ident-Proces-ou-Ato-Conce-T9Q-NUMPRO-n%C3%A3o-existe-na-base-de-dados-e-Chave-Cod-Suspensao-T9Q-IDSUSP
---

**Dúvida**

Ao integrar Nota Fiscal com Processo referenciado ocorre a inconsistência abaixo:

Ident Proces ou Ato Conce ( T9Q\_NUMPRO ) não existe na base de dados e Chave Cod. Suspensao ( T9Q\_IDSUSP )  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TAF - a partir da versão 12.  
  
**Solução**

O erro de integração ocorre por que é apresentado uma duplicidade no layout T001AO.

Verificar no cadastro de Processo referenciado (MATA967) o campo CCF\_INDSUS se está com o mesmo conteúdo para as 2 linhas.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411606529175/mceclip0.png)

Este conteúdo deve ter um identificador único para que seja enviado ao TAF de forma correta.

Corrigindo o erro de Duplicidade no layout T001AO, e com a integração do layout T001AB//T001AO com sucesso, o layout T013 não apresentará erro.
