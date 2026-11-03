---
article_id: 360059060074
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 026af3276f35e743b294a72ddf2916324777455a3190937be13826bc16c1e560
fetched_at: '2026-06-28T22:39:31.044312+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Impostos não deduzidos
  no pedido de venda ou no contas a receber, como resolver?
type: support-article
updated_at: '2025-11-28T15:39:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059060074-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Impostos-n%C3%A3o-deduzidos-no-pedido-de-venda-ou-no-contas-a-receber-como-resolver
---

**Duvida:**

Após lançar o pedido de venda e integrar a nota fiscal no financeiro os impostos não são deduzidos do título principal, esse conceito está correto?  
  
**Ambiente:**

Protheus – Faturamento – A partir da versão 11.80.

**Solução**

Por conceito, o sistema funciona desta forma na saída, pois não é possível prever se o Tomador fará o recolhimento do impostos. Com isso, a dedução ocorre somente após a baixa do título principal.

Vejamos:

No **Pedido de Venda (MATA410)**, o imposto não será abatido do valor do título. Ele irá gerar um próprio título de abatimento no Contas a Receber com a denominação do imposto seguido do símbolo “-“. Exemplo: "IR-". O valor será compensado somente na baixa do título principal.

Dedução na aba duplicatas e no valor do título, somente no documento de entrada, pois nas entradas os impostos são retidos da fonte pagadora do tomador de serviço, no caso o Contas a Pagar.

Ao incluir as informações da nota no Pedido de Venda e consultar a planilha financeira, o valor do imposto será demonstrado na aba "Nota Fiscal", porém na aba duplicatas o valor não será deduzido do montante do título:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18059552551063)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18059592846359)

* No Contas a Receber (FINA740) o imposto gera um título de abatimento. No caso exemplificado, "IRF-":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18059556055703)

* A dedução do valor do imposto do total da NF ocorrerá somente após a baixa do título principal:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18059610686615)
