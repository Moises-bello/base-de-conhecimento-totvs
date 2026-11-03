---
article_id: 360047913534
category: RH - Folha de Pagamento
content_hash: 78f40c81f2277c5733b1b08d26a444c2c222f3fa29044d8911b27c3c45d0574e
fetched_at: '2026-06-28T22:44:14.877015+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - De onde o sistema busca os dias para cálculo de
  DSR de hora extra, adicional noturno e outros DSRs
type: support-article
updated_at: '2025-08-22T19:56:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047913534-RH-Linha-Protheus-GPE-De-onde-o-sistema-busca-os-dias-para-c%C3%A1lculo-de-DSR-de-hora-extra-adicional-noturno-e-outros-DSRs
---

#### time.png Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**De onde o sistema busca os dias para cálculo de DSR de hora extra, adicional noturno e outras verbas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**O sistema busca os dias úteis e DSR para cálculo de DSR hora extra, adicional noturno e afins do cadastro de Períodos, aba Cadastro de Calendário, conforme print abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070560394)  
  
Quando o parâmetro **MV\_TPCALEN** **esta com 1**, o sistema monta o calendário analítico, e os dias úteis e DSR somente poderão ser alterados se alterado conforme abaixo, o mesmo serve para feriados, que serão considerados na contagem de DSR somente se alterados conforme abaixo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071682433)  
  
Quando parâmetro **MV\_TPCALEN esta com 2**, o sistema monta o calendário de forma sintética, desta forma é possível alterar os dias úteis e DSR diretamente nos campos abaixo:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070561174)

**Saiba Mais**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
