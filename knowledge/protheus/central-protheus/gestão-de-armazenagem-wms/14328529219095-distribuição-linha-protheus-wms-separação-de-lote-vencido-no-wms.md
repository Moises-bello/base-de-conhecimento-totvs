---
article_id: 14328529219095
category: Gestão de Armazenagem (WMS)
content_hash: 0814b7b0cf7323bb1f256744a3e12600c30c084b8912537efa779583e4af2528
fetched_at: '2026-06-28T22:45:47.965250+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Distribuição - Linha Protheus - WMS - Separação de lote vencido no WMS
type: support-article
updated_at: '2024-06-20T16:33:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14328529219095-Distribui%C3%A7%C3%A3o-Linha-Protheus-WMS-Separa%C3%A7%C3%A3o-de-lote-vencido-no-WMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como separar produto ***WMS*** com lote vencido e parâmetro **MV\_LOTVENC**=**N**?  
  
**Ambiente**TOTVS Distribuição - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS) - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
1. O produto deve estar com **bloqueio** de **lote** e **endereço** no **WMSA560**;  
2. Para incluir no pedido, no **MATA410**, é necessário a **liberação** deste bloqueio no **WMSA560**;  
3. Durante a inclusão do **produto** no pedido, informar o **lote** que está liberado e o **endereço** do mesmo;  
4. Salvar o pedido e ir diretamente para o monitor de serviços, **WMSA332**, este processo **não gera serviço a ser executado no WMSA150**;  
5. Finalizar o processo de separação e o produto estará apto a ser faturado.
