---
article_id: 360018892192
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: 942e9a3f964363cf6a9e303b55c580208febea5039f53fa77823deba5e732b6b
fetched_at: '2026-06-28T22:41:43.274098+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA060- Como funciona
  o campo N3_DINDEPR
type: support-article
updated_at: '2024-10-21T20:14:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018892192-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA060-Como-funciona-o-campo-N3-DINDEPR
---

**Dúvida**Como funciona o campo N3\_DINDEPR?  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Ativo Fixo – A partir da versão 11.80  
  
  
**Solução**

A configuração na data de início da depreciação se faz no parâmetro [MV\_TIPDEPR](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/sigaatf_t.htm) e o sistema oferece três formas distintas de cálculo:

\* Se for informado 0, para iniciar o calculo da depreciação, serão utilizados os dias proporcionais entre o campo Data inicio da depreciação e a data-base do sistema (dDataBase);

\* Se for informado 1, para iniciar o calculo da depreciação, serão utilizado o mês cheio (30 dias), considerando o mes do campo Data inicio de depreciação (N3\_DINDEPR);

\* Se for informado 2, para iniciar o calculo da depreciação, será utilizado o primeiro dia do mês subsequente á data da aquisição do bem.

Se o preenchimento deste parâmetro se fizer com a opção 2, e ainda considerando que a inclusão se efetua no mesmo mês do último cálculo da depreciação ou em data posterior, o sistema ,automaticamente, traz o conteúdo do campo Data de Início de Depreciação (SN3 - N3\_DINDEPR) como sendo o primeiro dia do mês subseqüente ao da aquisição do bem.

Na inclusão de um ativo, o Sistema não permite a inclusão de um bem com a data anterior ao parâmetro [MV\_ULTDEPR](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/sigaatf_u.htm).

Saiba mais: [Data de inicio de depreciação - Campo N3\_DINDEPR](https://tdn.totvs.com/pages/releaseview.action?pageId=560637378)

<https://tdn.totvs.com/pages/viewpage.action?pageId=306851592>

<https://tdn.totvs.com/pages/releaseview.action?pageId=312159681>

--
