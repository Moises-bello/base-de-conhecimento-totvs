---
article_id: 360019132251
category: Escrita Fiscal - Impostos - ICMS
content_hash: 015501899b84e6e7f70c5dfd1b0c56b9925fc1e3eea57f9cb44a511a0718dc68
fetched_at: '2026-06-28T22:39:24.214886+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como tratar origens
  (B1_ORIGEM) diferentes para um mesmo produto
type: support-article
updated_at: '2024-09-12T17:17:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019132251-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-tratar-origens-B1-ORIGEM-diferentes-para-um-mesmo-produto
---

**Dúvida**Como tratar origens (B1\_ORIGEM) diferentes para um mesmo produto?  
  
**Ambiente**Protheus - Faturamento - Compras - A partir  da versão 11.80   
  
**Solução**

A solução disponível no padrão do Protheus, é considerar a origem da mercadoria segundo o que consta no **Cadastro de Produtos**, no campo B1\_ORIGEM, se existirem origens variadas para seus produtos.

O campo **B1\_ORIGEM** é utilizado para a gravação do campo **Sit.Tribut. (D1\_CLASFIS** - Nota de entrada; **D2\_CLASFIS** - Documento de Saída; **C6\_CLASFIS** - Pedido de Venda). Se o campo for alterado manualmente a rotina **MATXFIS** irá recalcular a alíquota de ICMS e os arquivos magnéticos que exigem movimentação por nota pegam as informações dos campos acima citados.
