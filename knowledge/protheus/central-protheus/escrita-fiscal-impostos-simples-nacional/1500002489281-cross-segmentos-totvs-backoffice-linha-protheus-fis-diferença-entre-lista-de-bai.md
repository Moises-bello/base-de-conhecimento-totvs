---
article_id: 1500002489281
category: Escrita Fiscal - Impostos - Simples Nacional
content_hash: 17d1264058075c58639d874737fa9f9f52cf73cbb2cb673e019f2c546e66fbb1
fetched_at: '2026-06-28T22:39:37.590175+00:00'
product: protheus
section_id: 1500001538461
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Diferença entre lista
  de baixas e apuração do Simples Nacional em regime de caixa
type: support-article
updated_at: '2021-07-01T13:17:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002489281-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Diferen%C3%A7a-entre-lista-de-baixas-e-apura%C3%A7%C3%A3o-do-Simples-Nacional-em-regime-de-caixa
---

**Dúvida**Na apuração do Simples Nacional em regime de Caixa, ocorre diferença entre a base de cálculo e a lista de baixas no Financeiro.  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Na apuração do Simples em regime de Caixa , é necessário atentar-se a um detalhe que pode ser preponderante para diferenças de valor na apuração  
No regime de Caixa será considerado o período de recebimento das receitas, respectivamente, independentemente do momento em que foram reconhecidas. Porém é necessário atentar-se que a rotina de Apuração do Simples Nacional (**FISA153**) não considera alguns tipos (**E5\_TIPO**) de títulos para compor a base cálculo, como TX (Taxas), AB - abatimentos e também os exemplos a seguir:  
CF-, CS-, FC-, FE-, FU-, I2-, IM-, IN-, IR-, IS, PI-, FC-,FE-, NCC, PR

Mais detalhes sobre as variáveis com os tipos de título  
<https://tdn.totvs.com/pages/releaseview.action?pageId=184781323>
