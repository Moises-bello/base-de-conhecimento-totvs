---
article_id: 8365857231255
category: Comércio Exterior - Easy Export Control - Pedido - Export
content_hash: 06c8d2b6dd5814183086debaf3631843b512636ee896a522f848b192193da1b4
fetched_at: '2026-06-28T22:36:58.984070+00:00'
product: protheus
section_id: 1500001538181
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Atenção: Este
  Adiantamento Não Pode Ser Alterado'
type: support-article
updated_at: '2022-08-23T13:56:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8365857231255-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Aten%C3%A7%C3%A3o-Este-Adiantamento-N%C3%A3o-Pode-Ser-Alterado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao efetuar a alteração do adiantamento no pedido de exportação e o sistema apresenta uma mensagem: 

"Atenção - Este adiantamento não pode ser alterado. Detalhes: Este adiantamento já está vinculado a fechamento(s) de cambio,para alterar o mesmo favor desvincular o adiantamento no(s) fechamento(s) de cambio correspondente(s)." Como faço para seguir com o processo sem que esta mensagem seja exibida?

![ADIANTAMENTO_N_O_PODE_SER_ALTERADO.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/8365258529047/ADIANTAMENTO_N_O_PODE_SER_ALTERADO.PNG)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**

Para que não seja exibido a mensagem "Este adiantamento não pode ser alterado" no pedido de exportação será necessário estonar a associação feita no cambio de exportação. Acesse a rotina de cambio (**EECAF200**):

1) Selecione o processo .

2) Menu Outras Ações ->Associar.

3) Exclua o adiantamento criado.

Efetuado este procedimento será possível fazer a alteração do adiantamento no Pedido de exportação.
