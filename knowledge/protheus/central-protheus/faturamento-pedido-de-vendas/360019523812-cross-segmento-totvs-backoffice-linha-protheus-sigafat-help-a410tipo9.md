---
article_id: 360019523812
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 7843b6fc7245ce0d5c797a367f9410a7898e97a5c389bfda7290478b6a31e054
fetched_at: '2026-06-28T22:38:38.676509+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- Help A410TIPO9 '
type: support-article
updated_at: '2024-12-18T12:31:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019523812-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-A410TIPO9
---

**Dúvida**

Help A410TIPO9 .

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

A mensagem **A410TIPO9** é demonstrada ao utilizar a **Condição de Pagamento Tipo 9**, quando a soma dos **valores das parcelas** não bate com o**Valor do Pedido**.

O **Valor do Pedido de Venda** é composto pela soma do **Valor Total dos Itens**e das despesas acessórias (**Frete, Seguro, Despesa e Frete Autônomo**).

**Observação**: Os campos de **Indenização (C5\_DESCONT**, para indenização em valor, e **C5\_PDESCAB**, para indenização em porcentagem)**não são considerados** na formação do **Valor do Pedido,**pois trata-se de um valor que será considerado somente à partir da emissão do documento de saída.

**Observação:** Caso tenha realizado a criação de novos campos de parcela na **SC5. Ex.: C5\_PARC5, C5\_PARC6, C5\_PARC7 e C5\_DATA5, C5\_DATA6 E C5\_DATA7**, verifique se foi realizada a alteração do parâmetro **MV\_NUMPARC (número de parcelas)**pois para aumentar o número de campos de parcelas é necessário alterar o parâmetro para essa quantidade de parcelas.

Caso esteja utilizando outro tipo de condição e apresente a mensagem, verifique se os campos de parcelas estão preenchidos no pedido de venda, caso sim retire para validar o tipo utilizado no pedido de venda.

**Saiba Mais**

Para avaliação dos exemplos de uso, acesse a FAQ no TDN:**[FAT0274 Mensagem A410TIPO9 - Condição de Pagamento do Tipo 9 x Indenização](http://tdn.totvs.com/pages/viewpage.action?pageId=407112501)**
