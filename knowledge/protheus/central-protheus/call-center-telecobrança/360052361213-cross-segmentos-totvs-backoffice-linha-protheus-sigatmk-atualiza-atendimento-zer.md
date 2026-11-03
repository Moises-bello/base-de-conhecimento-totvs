---
article_id: 360052361213
category: Call Center - Telecobrança
content_hash: a74aedd9709bd457e776737ebf428947134e077b5cecac3edacf6d705085ce04
fetched_at: '2026-06-28T22:41:28.639645+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- Atualiza Atendimento
  - Zera Valores do Juros
type: support-article
updated_at: '2022-06-22T17:26:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052361213-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Atualiza-Atendimento-Zera-Valores-do-Juros
---

**Dúvida**

Ao confirmar a negociação e marcar o botão "**Atualiza Atendimento**" ao retornar para a tela de negociação os juros são zerados.

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK-Todas as Versões.

**Solução**

Quando o campo **Atualiza o Atendimento**, estiver selecionado, irá indicar que os títulos marcados serão **prorrogados para a data de pagamento informada**. Caso a data de pagamento ultrapasse ao número de dias estipulado para prorrogação do título, a simulação poderá até ser calculada, mas os dados não serão carregados nos itens de atendimento. E também, caso a data de pagamento informada seja maior que a data em que está sendo efetuada a simulação, os juros serão recalculados e com isso zerados, pois as datas de "**Vencimento**" e "**Venc. Real**" serão alteradas para a nova data que foi informada, e com isso o título não estará mais vencido.

Documento com detalhes em : **<https://tdn.totvs.com/x/gR8QGg>**
