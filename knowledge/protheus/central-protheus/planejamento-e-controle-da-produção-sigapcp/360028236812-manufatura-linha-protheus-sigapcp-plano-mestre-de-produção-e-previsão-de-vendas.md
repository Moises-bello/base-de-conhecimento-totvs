---
article_id: 360028236812
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: df9b265a51d6798781cdb647d493267841ec53f9912b2724f7b58f536e9db90a
fetched_at: '2026-06-28T22:42:45.578352+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Plano mestre de produção e Previsão
  de vendas no MRP
type: support-article
updated_at: '2026-04-17T19:40:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028236812-Manufatura-Linha-Protheus-SIGAPCP-Plano-mestre-de-produ%C3%A7%C3%A3o-e-Previs%C3%A3o-de-vendas-no-MRP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18790601371287)*** Tempo aproximado para leitura**: 00:00:56 min**  
  
**Dúvida**  
Qual o comportamento do **PMP - Plano mestre de produção** e **PV - Previsão de vendas** no **PCPA712 - MRP Memória**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
O Sistema considera da seguinte forma esses documentos no momento da geração de **SC's - Solicitações de Compra** e **OP's - Ordens de Produção**:  
  
**Previsão de venda**

* A quantidade da **PV** será somada em **Saída;**
* Serão abertas **SC's** e **OP's** caso necessário.

**Plano mestre da produção**

* A quantidade do **PMP** será somada em **Entrada**;
* Para os itens descritos no **PMP** sempre serão geradas **OP's** ou **SC's**, independente da posição do estoque.
