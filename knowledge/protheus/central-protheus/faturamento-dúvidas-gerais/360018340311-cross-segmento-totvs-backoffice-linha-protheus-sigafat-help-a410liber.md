---
article_id: 360018340311
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 6255ed6f7236e1191afe3d3a9b0dd7b26f5f1bd8d29ba7a0b4aa8c1c347d3595
fetched_at: '2026-06-28T22:38:28.581882+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help A410LIBER
type: support-article
updated_at: '2022-02-22T11:23:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018340311-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-A410LIBER
---

**Dúvida**

Ao tentar excluir um Pedido de Vendas - **MATA410 -** exibe o Help **A410LIBER**: Este pedido possui iten(s) Liberado(s), logo, torne-se necessário o Estorno desses na opção de Prep. de N.Fiscais para obter êxito na exclusão do pedido.  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 11.80.  
  
**Solução**

Indica que este Pedido já foi submetido à LIBERAÇÃO (total ou parcialmente) e se encontra apto a faturar (está liberado na tabela **SC9** de liberações).

É necessário estornar a liberação realizada e então poderá excluir o Pedido.

Para estornar, acesse Atualizações > Faturamento > Documento de Saída (Rotina **MATA460A**) e localize no browse o Pedido de Vendas, o qual se encontra apto a faturar;

Selecione o Pedido em questão e acesse Ações relacionadas > **"Estor.Docs"** para efetuar o estorno da Liberação.

**Saiba Mais**: **[HELP A410LIBER ao tentar Excluir um Pedido de Vendas](https://tdn.totvs.com/x/YHQxE)**
