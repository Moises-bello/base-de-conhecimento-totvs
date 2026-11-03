---
article_id: 28334062077591
category: Meu RH - Pagamento
content_hash: 6c94736ef615aa014da3287a61b8d3e7ff9bff3821582ccb1a20ae66d3c53411
fetched_at: '2026-06-28T22:47:33.857523+00:00'
product: rm
section_id: 1500000835221
source: central-rm
title: 'RH - RM - Meu RH - Erro ao acessar envelope de pagamento: objeto deve ser
  do tipo DateTime'
type: support-article
updated_at: '2024-12-09T14:11:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28334062077591-RH-RM-Meu-RH-Erro-ao-acessar-envelope-de-pagamento-objeto-deve-ser-do-tipo-DateTime
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28334062042263) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Quando acessar a tela de envelope de pagamento no Meu RH, é retornada a mensagem : **Objeto deve ser do tipo DateTime.**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**Esse incidente ocorre pois, na ficha financeira do colaborador no mesmo mês e período que está sendo acessado no Meu RH, existe algum evento que esteja com a data de pagamento não informada.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse  Ficha Financeira do Funcionário que está com erro ao abrir o envelope de pagamento no Meu RH, no exemplo abaixo o erro é apresentado no Período 1 do mês 10.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28334052251671)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28334062046871)  
  
2. Preencha a data de pagamento do evento que está com o campo em branco, nesse caso foi o evento de código 0003.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28334062049303)  
  
3. Acesse o envelope novamente pelo Meu RH e o erro deixará de ser apresentado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28334052264983)
