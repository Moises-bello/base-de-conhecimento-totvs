---
article_id: 10565300666775
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: c63b91599062777fbe2173b26a466aa6565d78be29c516b376cbfe61b5e38d17
fetched_at: '2026-06-28T22:42:44.465007+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem Estorno OP
type: support-article
updated_at: '2022-11-29T19:44:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10565300666775-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-Estorno-OP
---

Tempo aproximado para leitura: **00:00:45 min  
  
Ocorrência**No módulo **SIGAPCP - Planejamento e Controle da Produção**, ao estornar a produção através da rotina **MATA250** **- Produção Simples** ocorre a mensagem **A OP XXXXXXXXXXX está encerrada, após o estorno deste apontamento a OP ficará com saldo p/ produzir. Deseja reabrir a Ordem de Produção?** para todos os níveis. **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**  
Quando ocorre a **produção automática** e as **OPs** estão **encerradas**, ao estornar a produção ocorre a mensagem para todos os níveis.  
  
**Solução**  
Para não apresentar a mensagem para todos os níveis ao estornar a produção, altere o parâmetro **MV\_ESTPROP** - **Indica se a validação do estoque disponível será proporcional ou não**, para **.F.**
