---
article_id: 360051554174
category: RH - Rescisão
content_hash: c218aace9a9f6bc1a8561555f1c96980f0177a28140b143251c98d54af72409c
fetched_at: '2026-06-28T22:43:51.011826+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - Como separar na rescisão para funcionário horista o saldo
  de salário em horas normais e DSR
type: support-article
updated_at: '2022-08-29T17:07:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051554174-RH-Linha-Protheus-Como-separar-na-rescis%C3%A3o-para-funcion%C3%A1rio-horista-o-saldo-de-sal%C3%A1rio-em-horas-normais-e-DSR
---

**Dúvida**Como separar na rescisão para funcionário categoria horista saldo de salário em horas normais e DSR?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as versões.  
  
**Solução**Para apresentar composição do saldo de salário rescisão horista em horas normais e DSR, atualize o mnemônico P\_LDSRSALD para .T.

**Exemplo**

**Mnemônico**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081531554/mceclip1.png)

**Rescisão**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081531754/mceclip2.png)  
  
Com esta configuração, as horas normais serão apresentadas no id 0048 e o DSR no id 1399.
