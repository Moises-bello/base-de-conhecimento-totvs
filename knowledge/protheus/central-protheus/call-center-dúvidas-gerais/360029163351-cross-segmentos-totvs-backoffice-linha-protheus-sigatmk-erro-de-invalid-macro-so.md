---
article_id: 360029163351
category: Call Center - Dúvidas Gerais
content_hash: d1077044eac311d53a236f5dc7fcaa8861546e861db26b1283b1f89c6fa6ed21
fetched_at: '2026-06-28T22:41:26.868648+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice -(Linha Protheus-)SIGATMK-Erro de invalid
  macro source ao incluir um atendimento TMK
type: support-article
updated_at: '2022-06-17T18:14:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029163351-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Erro-de-invalid-macro-source-ao-incluir-um-atendimento-TMK
---

**Ocorrência**

Ao incluir um atendimento Call Center (**TMKA271**), ocorre o erro:

**invalid macro source (SSYacc0105e: Error token failed, no valid token) :{|a,b,c,d| FWInitCpo(a,b,c),lRet:=((Vazio().Or.Pertence("123")) .And. (1=Nota Fiscal;2=Remito;3=Entrega Futura)),FWCloseCpo(a,b,c,lRet),lRet } on FWBUILDFEATURE(PROTHEUSFUNCTIONMVC.PRX) 23/10/2018 18:06:52 line : 5352**

**Ambiente**

Cross Segmentos-TOTVS Backoffice -(Linha Protheus-)SIGATMK -  a partir da versão 11.  
  
**Causa**

O erro ocorre por que o **X3\_VLDUSER** do campo **UA\_DOCGER** está com um conteúdo indevido, preenchido com a informação 1=Nota Fiscal;2=Remito;3=Entrega Futura, no dicionário padrão do sistema, o campo está sem informações, em branco.

**Solução**

Para correção do problema, retire a validação**(1=Nota Fiscal;2=Remito;3=Entrega Futura)** que encontra-se no **X3\_VLDUSER**(Validação de usuário no Configurador),deixando em branco.

![UA_DOCGER.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360030251152/UA_DOCGER.gif)
