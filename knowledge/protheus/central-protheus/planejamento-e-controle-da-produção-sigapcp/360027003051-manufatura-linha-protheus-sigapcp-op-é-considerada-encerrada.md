---
article_id: 360027003051
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 31b5463903e44e42ddefcfee54332d5486b48434f3831b97e94b632bf83e7fc3
fetched_at: '2026-06-28T22:42:44.684795+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - OP é considerada encerrada
type: support-article
updated_at: '2024-03-01T18:30:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027003051-Manufatura-Linha-Protheus-SIGAPCP-OP-%C3%A9-considerada-encerrada
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)* Tempo aproximado para leitura: **00:00:30 min****Dúvida**Quando uma **OP - Ordem de produção** é considerada encerrada?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Uma **OP** é considerada encerrada quando atende a todos os critérios abaixo:

1. Ser do tipo firme, de acordo com o conteúdo do campo **C2\_TPOP - Tipo OP** que deve ter o conteúdo **F**;
2. Ter o campo **C2\_DATRF - Dt Real Fim** preenchido;
3. A quantidade entregue ser maior ou igual a quantidade prevista pela **OP**, para esta validação o Sistema verifica se o conteúdo do campo **C2\_QUJE - Qtd Produzid** é maior ou igual **C2\_QUANT - Quantidade.**
