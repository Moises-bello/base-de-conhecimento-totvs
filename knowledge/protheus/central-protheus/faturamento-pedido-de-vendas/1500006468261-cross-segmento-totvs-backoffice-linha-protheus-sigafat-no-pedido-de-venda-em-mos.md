---
article_id: 1500006468261
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 08ff3ff112fad01176ae23570d60cc7d7f90598e1624e593eed3b21013f22e1b
fetched_at: '2026-06-28T22:38:38.573409+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - No Pedido de
  Venda em "Mostrar Detalhes" não esta apresentando o CNPJ do Cliente
type: support-article
updated_at: '2023-05-16T14:38:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006468261-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-No-Pedido-de-Venda-em-Mostrar-Detalhes-n%C3%A3o-esta-apresentando-o-CNPJ-do-Cliente
---

**Dúvida**No Pedido de Venda em "Mostrar Detalhes" não esta sendo apresentando o dado de CNPJ do Cliente.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

O campo **C5\_GCCINT** não está associado ao cadastro do cliente (**SA1**), este campo é para informar o CPF/CNPJ do intermediador de Serviços, tratado pela **NT2020.006**, o campo não possui gatilho de preenchimento com o campo **A1\_CGC**, ele deve ser preenchido manualmente para que possa ser apresentado na opção **"Mostrar Detalhes"** do pedido de venda **(MATA410)**

![cnpj.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008650481/cnpj.gif)
