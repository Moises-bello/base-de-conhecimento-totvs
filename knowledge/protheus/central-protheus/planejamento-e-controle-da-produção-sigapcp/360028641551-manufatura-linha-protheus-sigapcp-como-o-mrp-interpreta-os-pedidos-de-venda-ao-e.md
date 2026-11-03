---
article_id: 360028641551
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: cb66ce3110ba21127ca20a11fba064fd20fbe6e097d96a80d45a9bd2227818cd
fetched_at: '2026-06-28T22:42:42.028859+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - Como o MRP interpreta os pedidos de
  venda ao executar pela previsão de vendas '
type: support-article
updated_at: '2021-09-14T13:27:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028641551-Manufatura-Linha-Protheus-SIGAPCP-Como-o-MRP-interpreta-os-pedidos-de-venda-ao-executar-pela-previs%C3%A3o-de-vendas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura**: 00:00:50 min**  
**Dúvida**Levando em consideração que existem pedidos de venda em carteira, como o Sistema trabalha com essa informação ao executar o **MATA712 - MRP** com base na previsão de vendas?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**No **MATA712** temos os parâmetros **Pedidos de venda colocados?** e **Pedidos de venda já faturados?**. Esses dois parâmetros trabalham em conjunto, o primeiro faz a leitura dos valores que estão pendentes para entrega e o segundo das quantidades que já foram entregues, subtraindo ou não as quantidades da previsão de venda, conforme parametrizado.
