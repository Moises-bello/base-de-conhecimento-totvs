---
article_id: 360037713794
category: Ativo Fixo - Contabilização/Lançamento padrão
content_hash: d271ff43b42ed77f4c7791dc3ed7f67d624686e8f2566f529d811e29d671084f
fetched_at: '2026-06-28T22:41:42.310752+00:00'
product: protheus
section_id: 1500001536421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA155/ ATFA150 - Contabilização
  rotinas de ampliação lançamento padrão 821
type: support-article
updated_at: '2022-06-20T12:27:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037713794-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA155-ATFA150-Contabiliza%C3%A7%C3%A3o-rotinas-de-amplia%C3%A7%C3%A3o-lan%C3%A7amento-padr%C3%A3o-821
---

**Dúvida**Como realizar a contabilização LP821 utilizando rotinas ATFA155 e ATFA150

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Ativo Fixo - a partir da versão 12

**Solução**Utilizando a rotina de  ampliação ATFA150 o valor é gerado no campo N3\_AMPLIA1 (Vl. Amplia 1).

Já a execução da rotina de ampliação ATFA155 diferente da ATFA150 é gerado uma linha com o tipo 11 com o valor de ampliação no campo  N3\_VORIG1 (Val.Orig M1).

A configuração no lançamento padrão 821,  deve seguir a configuração de acordo com a rotina utilizada considerando para a ATFA155 os campos da tabela SN4 e para ATFA150 os campos da tabela SN3.

Exemplos de configuração de lançamento padrão na ampliação:

ATFA155: 821 - 001  
IF(SN4->N4\_TIPO=="11",SN4->N4\_VLROC1,0)

ATFA150: 821 - 002 IF(SN3->N3\_TIPO=="01",SN3->N3\_AMPLIA1,0)

**Saiba Mais**

[ATFA155 - Rotina de Ampliação de Bens](https://tdn.totvs.com/pages/releaseview.action?pageId=527393818)
