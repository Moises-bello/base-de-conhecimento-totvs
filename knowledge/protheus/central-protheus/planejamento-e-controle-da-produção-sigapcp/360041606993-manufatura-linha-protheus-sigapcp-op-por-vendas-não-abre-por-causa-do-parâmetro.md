---
article_id: 360041606993
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: a64d41dfa93e0e017b93a20402840bcda11df19d45fd0fd5de4ade9127e933c1
fetched_at: '2026-06-28T22:42:44.688249+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - OP por vendas não abre por causa do
  parâmetro Considera Qtd Liberada P.V
type: support-article
updated_at: '2021-05-26T10:53:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041606993-Manufatura-Linha-Protheus-SIGAPCP-OP-por-vendas-n%C3%A3o-abre-por-causa-do-par%C3%A2metro-Considera-Qtd-Liberada-P-V
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:30 min**  
**Dúvida** Por que não gera **OP -** **Ordem de produção** por **PV - Pedido de venda** quando o parâmetro **Considera Qtd Liberada P.V** está ativo?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Quando o parâmetro **Considera Qtd Liberada P.V** está igual a **Sim** o Sistema avalia a tabela **SC9 - Pedidos Liberados** para abrir a **OP**. Se o parâmetro estiver igual a **Não** é avaliado apenas o **PV** para a geração da **OP**.
