---
article_id: 1500008369162
category: Faturamento - Orçamentos
content_hash: 4f0e9d8df4a49624ab5489a87f037fe6cac1cb1df5254e4b7b3b42e48ec7f030
fetched_at: '2026-06-28T22:38:24.982485+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT -Conceito de
  uso do campo CK_ITEM
type: support-article
updated_at: '2022-08-29T17:44:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008369162-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Conceito-de-uso-do-campo-CK-ITEM
---

**Dúvida**

O Campo CK\_ITEM do orçamento de vendas (Tabela SCK), após o item 99, o sistema incremente LETRAS, ficando assim 9A, 9B, 9C, etc. Tem como ficar em sequencial de formato numérico e  tamanho de mais de 2 caracteres?

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGAFAT – todas as versões

**Solução**

O campo **CK\_ITEM** se relaciona  diretamente com o campo **C6\_ITEM** do **pedido de vendas (MATA410)**, ele envia a informação de item de **orçamento (MATA415**) para o pedido de vendas após a efetivação de orçamento.

Como a configuração padrão do sistema para o campo **C6\_ITEM** é de 2 caracteres, não permitindo alteração, o item de orçamento segue o mesmo modelo para evitar inconsistências.

Tanto **CK\_ITEM** como **C6\_ITEM** são campos carácteres, desta forma, os campos com essa tipagem são alfanuméricos para poder permitir mais possibilidades de inclusão de linhas e esse tratamento  é efetuado diretamente em fonte de rotina.
