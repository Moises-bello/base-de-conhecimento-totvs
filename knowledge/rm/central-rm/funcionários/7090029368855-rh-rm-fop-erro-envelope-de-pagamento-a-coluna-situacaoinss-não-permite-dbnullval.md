---
article_id: 7090029368855
category: Funcionários
content_hash: e9dace17a4c299ff407af2b47a62ce21328829451cadc4423c0eaf501e886734
fetched_at: '2026-06-28T22:47:03.292895+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: 'RH - RM - FOP - ERRO Envelope de Pagamento: A coluna ''SITUACAOINSS'' não
  permite DBNull.Value'
type: support-article
updated_at: '2025-03-12T11:01:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7090029368855-RH-RM-FOP-ERRO-Envelope-de-Pagamento-A-coluna-SITUACAOINSS-n%C3%A3o-permite-DBNull-Value
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como realizar a correção do erro A coluna 'SITUACAOINSS' não permite DBNull.Value.?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7089868461207/mceclip0.png)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para realizar a correção do erro apresentado ao tentar abrir o envelope do funcionário, realize o seguinte processo:  
  
Dentro do cadastro do funcionário, na aba **Parâmetros**, a opção **calcula INSS** deverá estar **marcada**, conforme print abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7089910768919/mceclip2.png)

Caso esteja desabilitada, marque a opção e recalcule o envelope do funcionário. Feito isso, o erro deixará de ocorrer.
