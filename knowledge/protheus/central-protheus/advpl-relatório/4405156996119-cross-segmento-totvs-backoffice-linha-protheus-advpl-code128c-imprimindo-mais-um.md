---
article_id: 4405156996119
category: ADVPL - Relatório
content_hash: cb13406f78c5179ca9666e938604beb400668ecf3a550c3227a2e37e79c857bd
fetched_at: '2026-06-28T22:40:22.764073+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Code128C imprimindo
  mais um dígito
type: support-article
updated_at: '2021-07-28T17:09:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405156996119-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Code128C-imprimindo-mais-um-d%C3%ADgito
---

**Dúvida**Ao utiliza a classe **FWMSPrinter** método **Code128C** esta retornando um zero a mais no final.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL - Todas as versões  
  
**Solução**O método **Code128C**trabalha com caracteres em quantidade par, como:  
**\* 123456**  
**\* 1111**  
Caso ele receba caracteres em quantidade ímpar como **\* 12345, \* 111** será acrescido um 0 (zero) a mais no código de barras, tornando assim a quantidade par.  
Fica então a critério e responsabilidade do desenvolvedor colocar um zero no começo ou no final da *string*para compensar a quantidade de caracteres quando a mesma for ímpar.  
  
**Saiba mais**[FWMsPrinter](https://tdn.totvs.com/display/PROT/FWMsPrinter)
