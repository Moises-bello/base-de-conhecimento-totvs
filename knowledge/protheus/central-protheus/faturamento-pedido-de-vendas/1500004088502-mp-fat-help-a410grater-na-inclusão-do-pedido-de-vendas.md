---
article_id: 1500004088502
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 185b4f3a2850640bc2577a77f9c6e754b4e4964b9f1194e21e2a98e820ac6ad9
fetched_at: '2026-06-28T22:38:41.232946+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: MP - FAT - HELP A410GRATER na inclusão do Pedido de Vendas
type: support-article
updated_at: '2021-04-28T15:49:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004088502-MP-FAT-HELP-A410GRATER-na-inclus%C3%A3o-do-Pedido-de-Vendas
---

**Ocorrência**

Ao incluir um Pedido de Vendas (**MATA410**) o sistema está apresentando o Help **A410GRATER**.  
  
**Ambiente**Microsiga Protheus – Faturamento – A partir da versão 11.80  
  
**Causa**O sistema possui uma validação que verifica se o Produto que está informando no pedido possui grade (C6\_GRADE) e se o TES utilizado possui controle de Poder de Terceiros (F4\_PODER3 = R ou D).  
Caso ele identifique que essas duas configurações existem, informa o Help A410GRATER indicando que a grade não está disponível para poder de terceiros.  
  
**Solução**

Para solucionar essa ocorrência, realize uma das duas ações abaixo:  
1. Utilize um produto que não possua Grade;  
2. Utilize um TES que possua o campo "Poder Tec." (**F4\_PODER3**) como "N - Não Controla".
