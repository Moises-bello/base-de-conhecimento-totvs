---
article_id: 40671178750615
category: Financeiro - Contabilização
content_hash: 3251bd6990e8624d7b8b51a486c3b8f8c1461013852e09e68f3000e99b741c58
fetched_at: '2026-06-28T22:38:05.198824+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Não gera
  variação cambial para títulos provisórios
type: support-article
updated_at: '2026-05-22T17:44:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40671178750615-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Financeiro-N%C3%A3o-gera-varia%C3%A7%C3%A3o-cambial-para-t%C3%ADtulos-provis%C3%B3rios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40671235631895) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Por que o sistema não gera variação cambial para títulos provisórios?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Os títulos provisórios funcionam apenas como uma estimativa para a composição do fluxo de caixa, não representando, neste momento, uma obrigação financeira ou fiscal efetivamente consolidada.

Como o título provisório ainda não caracteriza o fato contábil definitivo, uma vez que a invoice final ou a NF ainda não foi processada e aprovada para pagamento, o sistema não o considera apto para reavaliações cambiais ou para a geração de movimentos bancários e de variação (tabela SE5).

Dessa forma, o comportamento padrão do sistema determina que a rotina de variação cambial somente será aplicada sobre obrigações ou direitos que estejam devidamente efetivados e consolidados no ambiente.
