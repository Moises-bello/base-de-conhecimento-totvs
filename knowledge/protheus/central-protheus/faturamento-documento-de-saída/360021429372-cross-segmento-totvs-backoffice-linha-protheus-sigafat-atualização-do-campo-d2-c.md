---
article_id: 360021429372
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: a4183e0f829925a54e5fb36c8a49618937a2019b7d2769f8afe887a155c8c04b
fetched_at: '2026-06-28T22:38:43.852605+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Atualização
  do campo D2_CUSTO1 ao utilizar TES que atualiza estoque
type: support-article
updated_at: '2023-05-22T16:57:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021429372-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Atualiza%C3%A7%C3%A3o-do-campo-D2-CUSTO1-ao-utilizar-TES-que-atualiza-estoque
---

**Dúvida**

Ao utilizar uma TES que atualiza estoque (F4\_ESTOQUE = S), a rotina de geração de notas fiscais,  MATA461, atualização dos acumulados dos itens da nota, função MAAVALSD2.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**Caso o cliente deseje atualizar o campo D2\_CUSTO1 poderá utilizar os pontos de entrada M460CUST, M460GCUS, MA330D2 e M330CD2 para realizar customizações no processo.  
  
Durante a execução da rotina MATA460 / MATA461  
  
<https://tdn.totvs.com/display/public/PROT/M460CUST+-+Tratamento+de+custo>

<http://tdn.totvs.com/display/public/PROT/M460GCUS+-+Tratamento+de+custo>  
  
Durante a execução da rotina MATA330  
  
<http://tdn.totvs.com/display/public/PROT/MA330D2>

<http://tdn.totvs.com/pages/releaseview.action?pageId=6087587> 

**Saiba Mais**Para conhecer mais sobre esse assunto, acesse o(s) *link*(s) abaixo:  
  
<http://tdn.totvs.com/pages/releaseview.action?pageId=317313777>
