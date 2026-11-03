---
article_id: 1500002710662
category: Financeiro - Contas a Receber
content_hash: f4c195720b9ced08d8026dd03ac89f75dad01347e00983b4f47a37b4b9f6a766
fetched_at: '2026-06-28T22:38:15.074820+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: MP - SIGAFIN - FINA460 - Gerar liquidação com natureza diferente do título
  pai  que calcula impostos na emissão
type: support-article
updated_at: '2021-04-28T15:16:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002710662-MP-SIGAFIN-FINA460-Gerar-liquida%C3%A7%C3%A3o-com-natureza-diferente-do-t%C3%ADtulo-pai-que-calcula-impostos-na-emiss%C3%A3o
---

**Dúvida**Como gerar liquidação com natureza diferente do título pai que calcula impostos na emissão?

**Ambiente**Microsiga Protheus – Financeiro – FINA460 – A partir da versão 12.1.17  
  
**Solução**Ao realizar uma liquidação com natureza que gere impostos na emissão e que seja diferente da natureza do título pai, o parâmetro MV\_VL460NT deve estar preenchido com o conteúdo 2 sem aspas, caso exista aspas (""), o sistema não irá gerar os impostos.  
  
EXEMPLO:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103514653/mceclip0.png)
