---
article_id: 20400960229271
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: d1835c6c1063470fc60a53fd79bfa09c519d31eb712639e0c48b7f43ace41ac0
fetched_at: '2026-06-28T22:42:43.336369+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Geração de Solicitação de Compras na
  Ordem de Produção por Vendas
type: support-article
updated_at: '2024-01-08T13:39:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20400960229271-Manufatura-Linha-Protheus-SIGAPCP-Gera%C3%A7%C3%A3o-de-Solicita%C3%A7%C3%A3o-de-Compras-na-Ordem-de-Produ%C3%A7%C3%A3o-por-Vendas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20400996102039) Tempo aproximado para leitura: **00:00:38 min** **Dúvida**Por que o Sistema gera uma **OP - Ordem de Produção** para um item que tem estrutura vencida, mesmo com o parâmetro **Produto Sem Estrutura Gera?** com o conteúdo **Solic. de Compra**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Neste processo o Sistema verifica se o item possui estrutura cadastrada no **PCPA200 - Cadastro de Estruturas**, mas não avalia se algum componente é empenhado. Então, tendo estrutura cadastrada é gerada a **OP**.
