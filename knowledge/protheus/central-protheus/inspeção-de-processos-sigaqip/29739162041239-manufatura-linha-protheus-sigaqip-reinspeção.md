---
article_id: 29739162041239
category: Inspeção de Processos (SIGAQIP)
content_hash: 1b0ea07d5fe83cd3dc28c9ee67f0de5c34eaed7ef9a9c8a29a53e8df999e29b7
fetched_at: '2026-06-28T22:42:25.936637+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Reinspeção
type: support-article
updated_at: '2025-02-04T20:40:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29739162041239-Manufatura-Linha-Protheus-SIGAQIP-Reinspe%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29739162014103) Tempo aproximado para leitura: **00:00:50 min** **Dúvida**No módulo **SIGAQIP - Inspeção de Processos**, existe um processo de **reinspeção**?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Todas as versões  
  
**Solução**O módulo **SIGAQIP** não possui um processo específico de reinspeção, ou seja, não há geração de novo registro na rotina **QIPA215 - Resultados**. No entanto, caso seja necessário **reinspecionar** um produto, independentemente do motivo, ele deve ser transferido para o armazém da qualidade, geralmente o armazém 98, por meio da rotina **MATA261 -****Transferência Múltiplas**.  
Após essa movimentação, um novo registro será gerado na rotina **MATA175 - Estoque**, permitindo que a gestão do produto ocorra **apenas via controle de estoque**.
