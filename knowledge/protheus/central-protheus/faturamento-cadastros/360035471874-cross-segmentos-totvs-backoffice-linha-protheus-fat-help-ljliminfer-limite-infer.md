---
article_id: 360035471874
category: Faturamento - Cadastros
content_hash: 8cf62997214d8dc4fea6de18b3ffdd4fe5b8c68b53e2837dbe87854e37f49a93
fetched_at: '2026-06-28T22:38:35.493445+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - FAT - HELP LJLIMINFER
  Limite inferior e superior na condição de pagamento
type: support-article
updated_at: '2022-05-18T12:44:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035471874-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-FAT-HELP-LJLIMINFER-Limite-inferior-e-superior-na-condi%C3%A7%C3%A3o-de-pagamento
---

**Dúvida**Na condição de pagamento pode ser estipulado o valor mínimo e valor máximo para utilizar uma determinada condição de  pagamento no pedido de venda (**MATA410**)?

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - todas as versões.  
  
**Solução**Na rotina condição de pagamento (**MATA360**) informe o valor mínimo através do campo **E4\_INFER** e valor máximo  **E4\_SUPER**. Estes campos estipulam o valor limite que está condição de pagamento

pode ser utilizada no pedido de venda.

![](https://tdn.totvs.com/download/attachments/268578622/image2016-10-26%2011%3A44%3A45.png?version=1&modificationDate=1477497833000&api=v2)

Após estipular os limites na condição, no pedido de venda caso o valor não esteja entre o range do valor menor e maior apresenta a mensagem:

* **LJLIMINFER** - O valor total da venda não atingiu o Limite inferior desta condição de pagamento. (Mensagem apresentada quando o valor do pedido de venda é inferior ao valor mínimo);
* **LJLIMNSUPER** - O valor total da venda não atingiu o Limite superior desta condição de pagamento. ( Mensagem apresentada quando o valor limite é ultrapassado).

**Solução**: Utilize outra condição ou diminua o valor total da venda.

**Observação**: Sem a condição de pagamento, não haverá a validação de valores min/máx.

**Saiba mais:**   **[FAT0155\_Limite\_inferior\_e\_superior\_na\_condição\_de\_pagamento](https://tdn.totvs.com/x/Pi8CE)**

**[MP - FAT - Condições de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017468312-MP-FAT-Condi%C3%A7%C3%B5es-de-Pagamento)**

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Nota sobre formas de pagamento para a NT2020.006](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407076251287-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Nota-sobre-formas-de-pagamento-para-a-NT2020-006)**
