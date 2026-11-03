---
article_id: 360025813734
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 34616a10e8ec67e72a980b75fd79acf8c9bf2677ef2338e7e4ef882fef9a57f8
fetched_at: '2026-06-28T22:42:47.044949+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Tabela SGJ
type: support-article
updated_at: '2021-10-05T11:16:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025813734-Manufatura-Linha-Protheus-SIGAPCP-Tabela-SGJ
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:50 min****Dúvida**Para que serve a tabela **SGJ**  **– Amarração Pedido de Venda x Ordem de Produção**?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Para informar se essa tabela é utilizada, é necessário informar **T** no parâmetro **MV\_PVCOMOP - Ativa a gravação na tabela SGJ - Amarração Pedido de Venda x Ordem de Produção**.  
Ela é usada internamente pelo Sistema para controlar e gravar os registros de amarração do pedido de venda com as ordens de produção, quando a **OP - Ordem de Produção** é aberta por meio do **MATA650 - Ordem de produção > Outras Ações > Vendas**.  
  
**Importante**  
Somente os pedidos de venda gerados após a ativação do parâmetro, serão controlados pela tabela **SGJ.**
