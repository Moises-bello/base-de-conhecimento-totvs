---
article_id: 360045477734
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: f7e9ff6cbedcff7b234493d8b5495a8b6c5b547986cfdf98c386ea5966d72435
fetched_at: '2026-06-28T22:38:43.879818+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - HELP: A410TEEST'
type: support-article
updated_at: '2025-10-17T20:55:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045477734-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-HELP-A410TEEST
---

**Dúvida**Ao incluir um **pedido de venda** (**MATA410**) com produto que controla **rastreabilidade**, informando o lote no pedido e utilizando um **TES (MATA080)** que **não movimenta estoque**, ocorre o help:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360064538013/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  - Faturamento- Todas as versões.  
  
**Solução**Com relação ao  HELP **A410TEEST**, não é um erro e sim um conceito do  padrão do sistema, se o TES não movimenta estoque, não deve informar o número do lote no Pedido, caso deixe o campo em branco o sistema permitirá a gravação e não movimentará o estoque.

Se está  informando o lote no pedido, está indicando ao sistema que deseja movimentar o saldo de estoque do produto e para isso é necessário que o **TES** utilizado movimente estoque.  
  
Poe conceito sistêmico e para que não haja problema de integridade entre as tabelas de movimentações e  saldo (**SB2** e **SD3**),  lote (**SB8**) e endereçamento (**SBF**), é fundamental realizar a movimentação do estoque quando utilizar Lote no pedido de vendas.  
  
Este procedimento é conceito e padrão do sistema.
