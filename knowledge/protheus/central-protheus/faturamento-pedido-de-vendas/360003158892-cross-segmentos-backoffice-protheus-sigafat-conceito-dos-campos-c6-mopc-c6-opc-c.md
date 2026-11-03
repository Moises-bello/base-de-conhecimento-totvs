---
article_id: 360003158892
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 8a58e4315ab16a5f186dd1ca7d3934633bb859d38aa098b2da60ecff23a73fff
fetched_at: '2026-06-28T22:38:39.612685+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT -  Conceito dos campos C6_MOPC,
  C6_OPC, CK_MOPC e CK_OPC
type: support-article
updated_at: '2025-11-21T20:25:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003158892-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Conceito-dos-campos-C6-MOPC-C6-OPC-CK-MOPC-e-CK-OPC
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36420177595415) Tempo aproximado para leitura: **00:02:00 min****

**Dúvida**

Como funciona o preenchimento dos campos **\_OPC** e **\_MOPC** ao incluir itens com opcionais no Pedido e Orçamento de Venda?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

**Solução**

Quando um produto possui opcionais cadastrados em sua estrutura, ao inserir este produto no Pedido de Venda por exemplo, o sistema solicita a seleção dos opcionais e grava essas escolhas nos campos:

* **C6\_OPC** - Registro resumido do **grupo/item (GA\_GROPC/GA\_OPC)** selecionado:

Armazena os grupos/itens de opcionais selecionados.  
Se vários componentes na estrutura utilizarem o mesmo grupo e item, o conteúdo será idêntico/repetido, pois o sistema entende que pertencem ao mesmo grupo de opcionais

* **C6\_MOPC** - Registro detalhado da **estrutura + opcional**, codificado:

Armazena a relação completa da estrutura com o opcional associado.  
O conteúdo aparece como caracteres especiais pois é codificado, para permitir gravação de estrutura com opcionais maiores, evitando gerar estouro de campo.

**Observação:** O conceito, a lógica e a forma de gravação desses campos são definidos pelo SIGAPCP.

Em caso de dúvidas sobre montagem de estrutura, grupos, itens ou comportamento do opcional, orientamos que sejam avaliadas com o módulo Protheus Manufatura.

**Saiba mais:**

[Cross Segmentos - Backoffice Protheus - SIGAFAT - Uso de Opcionais no Faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016126271-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Uso-de-Opcionais-no-Faturamento?source=search)

[Grupo de Opcionais - Conceito e Gravação dos Campos \_OPC e \_MOPC](https://tdn.totvs.com/x/siWVMw)
