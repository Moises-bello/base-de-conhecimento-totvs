---
article_id: 360024357552
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 71d57cb324dc7a6115ca84f2d9aaa054c8a6b4b32eb47b0cba99d639d563b993
fetched_at: '2026-06-28T22:38:40.995062+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Tratamento de juros no módulo
  Faturamento
type: support-article
updated_at: '2025-01-27T17:05:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024357552-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Tratamento-de-juros-no-m%C3%B3dulo-Faturamento
---

**Dúvida**

Como funciona o juros no modulo faturamento?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

**Solução**

A taxa de juros a ser aplicada nos títulos do conta  receber é feita pelo parâmetro **MV\_TXPER** **.**

O  sistema registra o percentual no campo **E1\_PORCJUR** e faz conversão no campo **E1\_VALJUR**, que é o valor a ser cobrado por dia de atraso ao título.

O módulo Faturamento não utiliza conceito de Multa, apenas de juros de acordo com a configuração informada acima.

Para o correto funcionamento e configuração do Parâmetro **MV\_TXPER** o conteúdo numérico deve ser separado por ponto (.) e não por vírgula(,).

*Exemplo*:

**MV\_TXPER** = 1.50 (um ponto cinquenta, que equivale a 1,50%)

O campo **E1\_PORCJUR** é gravado no momento da emissão do titulo no contas a receber. Caso o percentual do parâmetro  **MV\_TXPER** seja alterado o novo valor irá ser aplicado somente para os novos próximos títulos.

**Saiba Mais**:

**[FAT0097 - Comportamento Juros no Modulo Faturamento](https://tdn.totvs.com/x/jxFdDg)**
