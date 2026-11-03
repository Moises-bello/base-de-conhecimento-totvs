---
article_id: 19930988054295
category: PMS - Integrações
content_hash: e5fd6db7a1358a710adf7d727b670f3393ace18853d32ee6fa88dc330670c722
fetched_at: '2026-06-28T22:37:16.750213+00:00'
product: protheus
section_id: 1500001550742
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Amarração de projetos na
  rotina de pedido de compras (MATA121)
type: support-article
updated_at: '2024-03-11T16:13:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19930988054295-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Amarra%C3%A7%C3%A3o-de-projetos-na-rotina-de-pedido-de-compras-MATA121
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19930996897943) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como funciona a amarração de projetos no pedido de compras?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - Protheus 12 e superiores  
 **Solução**

É possível amarrar o projeto ao pedido de compras. Essa ação preenche a tabela AJ7 com o número do pedido de compras no campo "AJ7\_NUMPC".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19930988045975)

Nesse momento, também é possível gerar empenho ao projeto para que os produtos do pedido de compra fiquem iguais aos da tarefa do projeto (opcional).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19930988044951)

**OBSERVAÇÃO:** Quando há vínculo da solicitação de compras ao projeto, a tabela "AJ7" não é preenchida, pois a origem que não deve ser alterada é na solicitação de compras, na tabela "AFG":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19930996903447)
