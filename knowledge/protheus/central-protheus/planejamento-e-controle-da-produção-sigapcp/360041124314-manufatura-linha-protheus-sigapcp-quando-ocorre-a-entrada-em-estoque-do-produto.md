---
article_id: 360041124314
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 8526876881633292be2f289247ac047c574204d6fe69eea43966816848411735
fetched_at: '2026-06-28T22:42:45.797245+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Quando ocorre a entrada em estoque
  do produto produzido
type: support-article
updated_at: '2022-11-22T16:48:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041124314-Manufatura-Linha-Protheus-SIGAPCP-Quando-ocorre-a-entrada-em-estoque-do-produto-produzido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:00:40 min**  
**Dúvida**Nos apontamentos de produção, quando ocorre a entrada em estoque do produto produzido?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Ao utilizar as rotinas de apontamento **MATA680 - Produção Modelo I** e **MATA681- Produção Modelo II**, a entrada no estoque ocorre somente ao apontar a última operação do roteiro de operações que está informado na **OP - Ordem de Produção.**Já se utilizar a rotina **MATA250 - Produção Simples** a entrada do material no estoque ocorre a cada apontamento de produção, conforme a quantidade informada no campo **D3\_QUANT - Quantidade**.
