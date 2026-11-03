---
article_id: 17102292867991
category: Financeiro - Comissão
content_hash: db13171134710718b1514554b4508813dcc867c008e6d4b291168f288a127daa
fetched_at: '2026-06-28T22:37:50.872281+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA070 - Cancelamento
  da baixa apresenta HELP: BXNAOCANC'
type: support-article
updated_at: '2024-09-27T12:59:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17102292867991-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA070-Cancelamento-da-baixa-apresenta-HELP-BXNAOCANC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26620922945559) Tempo aproximado para leitura: **00:05:00****min**

**Ocorrência**  
Como cancelar uma comissão que já foi paga?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**  
Este Help é apresentado porque o título de comissão gerado já foi pago.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17101987984919)  
  
**Solução**  
No **Contas a Pagar**, primeiro cancele a **baixa do título** de comissão. Após isso, você poderá **cancelar o título** também no **Contas a Receber**.

![Gravar_2024_07_10_14_36_09_92.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24794802724759)

 A comissão será, então, removida da rotina de **Manutenção de Comissão**.

**Importante**

Quando o pagamento da comissão ocorre, mesmo que o parâmetro **MV\_COMIDEV** esteja definido como **F**, uma comissão negativa será gerada, pois o pagamento foi realizado. Caso o pagamento não tivesse ocorrido, a comissão seria excluída.

**Saiba mais**

[Recalculo de Comissão - FINA440](https://tdn.totvs.com/pages/releaseview.action?pageId=312162528)

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Pontos de Entrada da rotina MATA490](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403854071447)
