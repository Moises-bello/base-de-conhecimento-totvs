---
article_id: 18433134371863
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 9728e8138e8b416e5841a2870bfccdb70ccd6b3577b7d7b6faf0835aecdb9f1a
fetched_at: '2026-06-28T22:42:44.496510+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem MA380SALDO
type: support-article
updated_at: '2023-10-20T18:12:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18433134371863-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-MA380SALDO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18433160007831) Tempo aproximado para leitura: **00:01:01 min****Ocorrência**Ao realizar a manutenção de empenhos no **MATA381 - Empenho Múltiplo** o usuário recebe a mensagem **MA380SALDO - O lote selecionado não possui saldo suficiente para esse empenho**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Essa mensagem é apresentada quando não há saldo suficiente do lote informando para atender esse empenho ou quando existe algum registro para esse produto e armazém com o campo **B8\_LOTECTL - Lote em branco**.

**Solução**Verifique se o lote foi informado na tela, se foi informado, verifique o saldo disponível desse lote e armazém.  
Caso o lote não tenha sido informado, verifique na tabela **SB8 - Saldos por Lote**, se para esse produto e armazém existe um registro com o campo **B8\_LOTECTL** em branco.
