---
article_id: 360051732433
category: Escrita Fiscal - CIAP
content_hash: b5d7194ddcc837211dec8becee6738ca1cd7e1d20e6b002d217395e06fad8fa0
fetched_at: '2026-06-28T22:39:33.728052+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - A905TUDOK - Inclusão
  manual de ativo na rotina MATA905 - Manutenção do CIAP
type: support-article
updated_at: '2021-07-29T12:29:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051732433-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-A905TUDOK-Inclus%C3%A3o-manual-de-ativo-na-rotina-MATA905-Manuten%C3%A7%C3%A3o-do-CIAP
---

**Dúvida**

Ao tentar incluir um ativo de forma manual na rotina de Manutenção do CIAP - MATA905, é apresentado a mensagem abaixo:

A905TUDOK

Há inconsistência nos dados referentes ao CIAP, verifique o valor do crédito ou se o crédito já foi utilizado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079223814/mceclip0.png)  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**A mensagem é apresentada quando o campo Item NFE (F9\_ITEMNFE) é preenchido manualmente na rotina de Manutenção CIAP (MATA905).

Esse campo não poderá ser preenchido quando a inclusão do item ocorre através da rotina MATA905 pois esse código será integrado quando o item é incluído através do documento de entrada.

Nesse caso, solicito que efetue a inclusão do item novamente através da rotina MATA905 porém desconsidere o preenchimento do campo Item NFE (F9\_ITEMNFE).
