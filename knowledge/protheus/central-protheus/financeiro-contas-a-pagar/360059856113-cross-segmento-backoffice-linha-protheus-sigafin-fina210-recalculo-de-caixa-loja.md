---
article_id: 360059856113
category: Financeiro - Contas a Pagar
content_hash: ebe2633b7acd84249c5031050ee8220a44eff4697917b5c00baf8c8f62a7be6c
fetched_at: '2026-06-28T22:38:08.287333+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA210 - Recalculo
  de caixa loja, com transferência que não atualiza o saldo bancário '
type: support-article
updated_at: '2024-06-03T20:27:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059856113-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA210-Recalculo-de-caixa-loja-com-transfer%C3%AAncia-que-n%C3%A3o-atualiza-o-saldo-banc%C3%A1rio
---

**Ocorrência**Após realizar o **recalculo de saldos bancários** na rotina **FINA210**, na rotina **saldos bancários** **FINA030** não está considerando as transferência do tipo "CH" com um caixa de loja (cadastrados na tabela 23 da SX5)  
  
**Ambiente**Cross Segmento - BackOffice Linha Protheus – Financeiro – FINA210 - A partir da versão 11  
  
**Causa**Esse valor não será considerado no saldo bancário, pois este será considerado como um movimento de sangria, que é tratado pelo modulo de loja. Isto quando o caixa não for simultaneamente financeiro.

**Solução**Para que os caixas de loja sejam considerados também como financeiro, pode-se ativar o parâmetro **MV\_CXLJFIN** =  **T**  
Descrição do parâmetro: Define se os caixas do loja atuarão também como caixas Financeiros.  
  
**Saiba mais:**   
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN – FINA210 – Como executar corretamente a rotina de recalculo de saldos bancário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018852211)
