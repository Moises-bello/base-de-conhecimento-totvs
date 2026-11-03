---
article_id: 360036458933
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: e238f81a7d895f31c07272ceee011ad52c5785e2109e598bf210b42b4b9c72c5
fetched_at: '2026-06-28T22:42:40.760987+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Aglutinar as Ordens de Produção provenientes
  de pedidos de venda
type: support-article
updated_at: '2021-10-22T12:55:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036458933-Manufatura-Linha-Protheus-SIGAPCP-Aglutinar-as-Ordens-de-Produ%C3%A7%C3%A3o-provenientes-de-pedidos-de-venda
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:50 min**  
**Dúvida**Como aglutinar as **Ordens de Produção** provenientes de **pedidos de venda**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Na rotina **MATA720 - Aglutinação de OPs** é possível parametrizar para atualizar os **pedidos de venda**, parâmetro **Atualiza Ped. Venda?**, se esse parâmetro estiver preenchido com **Sim**, ao aglutinar as **OPs - Ordens de Produção** o número da nova ordem será preenchido nos **pedidos de venda**, em substituição ao antigo.  
  
**Importante**  
O Sistema não libera o **pedido de venda** ao realizar o apontamento, pois ao realizar a aglutinação na tabela **SC2 - Ordens de Produção** não tem mais a referência dos pedidos, e o Sistema consulta o campo **C2\_Pedido - Pedido de Venda** para poder realizar essa liberação do pedido de venda.
