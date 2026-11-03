---
article_id: 115015486348
category: Contabilidade Gerencial - Plano de Contas
content_hash: 4bae6a6b034f5985a0168d7d4ddcccb35b6e27a0cf51c24e6ed19b3351141e13
fetched_at: '2026-06-28T22:40:33.300030+00:00'
product: protheus
section_id: 1500001549022
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA020 - Plano de
  contas: Error.log - Erro invalid macro source (SSYacc0105e: Error token failed,
  no valid token) no Plano de contas'
type: support-article
updated_at: '2024-04-22T12:46:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015486348-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA020-Plano-de-contas-Error-log-Erro-invalid-macro-source-SSYacc0105e-Error-token-failed-no-valid-token-no-Plano-de-contas
---

**Ocorrência**Ao realizar a inclusão/alteração/exclusão de uma conta contábil é exibido o seguinte erro:

**invalid macro source (SSYacc0105e: Error token failed, no valid token) :{|a,b,c| FWInitCpo(a,b,c),lRet:=(INCLUI .and. If(FunName()=="CTBA160",.T.,.F.)",.F.,.T.)),FWCloseCpo(a,b,c,lRet,.T.),lRet } on FWBUILDFEATURE(PROTHEUSFUNCTIONMVC.PRX) 05/10/2017 18:39:41 line : 5199**

**Ambiente:**  
Protheus – Contabilidade Gerencial – A partir da versão 12.1.17  
  
**Causa:**Erro ocorre, pois o "modo de edição" X3\_WHEN do campo CTS\_ORDEM esta com conteúdo:

INCLUI .and. If(FunName()=="CTBA160",.T.,.F.)",.F.,.T.)  
  
**Solução:**

Para correção desta ocorrência deve ajustar o conteúdo do campo X3\_WHEN referente ao campo CTS\_ORDEM através do módulo configurador com a informação:

INCLUI .and. If(FunName() $ "CTBA160|CTBA161",.T.,.F.)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22922262300439)
