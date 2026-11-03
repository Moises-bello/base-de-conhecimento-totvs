---
article_id: 4411032786839
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 87dc89c88feaf62eeecdec02253c0a4ca0da6771e8fe2b0f8243204871c39ed7
fetched_at: '2026-06-28T22:38:43.888446+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Múltiplas naturezas
  no pedido de venda '
type: support-article
updated_at: '2022-08-17T20:48:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411032786839-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-M%C3%BAltiplas-naturezas-no-pedido-de-venda
---

**Dúvida**

É possível utilizar múltiplas naturezas no pedido de venda?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

Por padrão do sistema não há como incluir múltiplas naturezas do pedido de venda.

A natureza tratada no Protheus fica no campo **A1\_NATUREZ** ou no campo **C5\_NATUREZ**, e essa informação será validada de acordo com a configuração do Parâmetro **MV\_1DUPNAT** que por padrão vem como SA1->**A1\_NATUREZ**.

Saiba mais : **<https://tdn.totvs.com/x/h_ruDQ>**

**Observação: O cadastro de naturezas é efetuado na tabela SED - Cadastros de natureza e posteriormente deve ser associado ao campo definido no mv\_1dupnat para que que seja emitida nas notas fiscais de saída.**
