---
article_id: 360049414854
category: Call Center - Dúvidas Gerais
content_hash: 7bbb570f54cf4f77d992672460ba33becb042277e982b821d339545197cc55f3
fetched_at: '2026-06-28T22:41:26.822931+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK- Botão Atualiza Atendimento
type: support-article
updated_at: '2022-06-17T16:33:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049414854-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Bot%C3%A3o-Atualiza-Atendimento
---

**Dúvida**

Sistema não permite marcar o Botão Atualiza Atendimento Simulação de Valores Telecobrança.

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK - Todas as versões.

**Solução**

Quando o campo Atualiza o Atendimento, estiver selecionado, irá indicar que os títulos marcados serão prorrogados para a data de pagamento informada.

Caso a data de pagamento ultrapasse ao número de dias estipulado para prorrogação do título, a simulação poderá até ser calculada, mas os dados não serão carregados no Acols (Itens de Atendimento).

Para Atualizar o atendimento o campo **K2\_DIAPROR** ( Quantidade máxima de dias que o título poderá ter a data de vencimento prorrogada, deve estar preenchido no cadastro de Regra de Negociação.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075209933/mceclip0.png)

Maiores detalhes em :[**https://tdn.totvs.com/pages/releaseview.action?pageId=239037537**](https://tdn.totvs.com/pages/releaseview.action?pageId=239037537)
