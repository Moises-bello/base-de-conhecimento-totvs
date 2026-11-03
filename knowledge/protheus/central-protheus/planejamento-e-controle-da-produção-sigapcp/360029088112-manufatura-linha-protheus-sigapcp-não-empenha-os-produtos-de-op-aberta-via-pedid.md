---
article_id: 360029088112
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: df50529c698e50d95cc9baefe29cc2e60a8a6df0d9d8258367c5b08b0a688622
fetched_at: '2026-06-28T22:42:44.576685+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Não empenha os produtos de OP aberta
  via pedido de venda quando a estrutura é cadastrada após a abertura do pedido
type: support-article
updated_at: '2021-10-19T16:59:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029088112-Manufatura-Linha-Protheus-SIGAPCP-N%C3%A3o-empenha-os-produtos-de-OP-aberta-via-pedido-de-venda-quando-a-estrutura-%C3%A9-cadastrada-ap%C3%B3s-a-abertura-do-pedido
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:01:00 min****Dúvida**Por que não são empenhados os produtos de **OP****- Ordem de Produção** aberta via **Pedido de Venda** quando a estrutura é cadastrada após a abertura do pedido?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Para que o Sistema leia a estrutura que foi alterada/modificada após a abertura do pedido é necessário que o conteúdo do parâmetro **MV\_SELEOPC** **- Indica se sistema utiliza seleção de Opcionais na abertura de OPs, SCs, Prev. Vendas, Plano Mestre de Produção, etc** esteja igual a **N**.  
Caso o parâmetro esteja ativo, o Sistema irá salvar no pedido a estrutura daquele momento, então ao criar ou modificar uma estrutura não serão lidas essas novas alterações.
