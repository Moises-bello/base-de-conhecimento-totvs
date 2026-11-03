---
article_id: 1500008650402
category: RH - Rescisão
content_hash: b31d3cd83fe2f5b7add60cdafb9b86c60e86085ca926962f7574459b8fb2a555
fetched_at: '2026-06-28T22:43:53.642972+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Por que o cálculo de rescisão mesmo não tendo desconto
  de empréstimo consignado emite mensagem de desconto de empréstimo consignado
type: support-article
updated_at: '2025-08-20T20:27:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008650402-RH-Linha-Protheus-GPE-Por-que-o-c%C3%A1lculo-de-rescis%C3%A3o-mesmo-n%C3%A3o-tendo-desconto-de-empr%C3%A9stimo-consignado-emite-mensagem-de-desconto-de-empr%C3%A9stimo-consignado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18970294536599)**Tempo aproximado para leitura: **01:30 min****Dúvida**Por que o cálculo de rescisão mesmo não tendo desconto de empréstimo consignado emite o erro: Atenção o funcionário possui empréstimo(s) que serão liquidados parcialmente ou NÃO serão liquidados pois o saldo devedor dos mesmos ultrapassa o valor de 30% sobre o liquido da Rescisão. Verifique os Lançamentos Futuros.:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013222101)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**O erro é emitido porque no cálculo da rescisão consta alguma verba com o campo Emp. Cons. Sim.

Este campo só deve constar com Sim para a verba de desconto de empréstimo consignado.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013229901)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012868502)

**Verba Desconto Empréstimo Consignado.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18970294544279)**

**Saiba mais:**

[RH - Linha Protheus - GPE - Valor liquido rescisão calculado diferente do liquido em TRCT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18850302368663-RH-Linha-Protheus-GPE-Valor-liquido-rescis%C3%A3o-calculado-diferente-do-liquido-em-TRCT?source=search)

[RH - Linha Protheus - GPE - Como descontar empréstimo consignado na rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026281133-RH-Linha-Protheus-GPE-Como-descontar-empr%C3%A9stimo-consignado-na-rescis%C3%A3o?source=search)
