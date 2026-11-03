---
article_id: 360028861332
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 0881782635c1a47a6bec373416f80056cbca291635e3fa0a494f3ae24e534882
fetched_at: '2026-06-28T22:42:42.118484+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Considerar a informação do campo Perda
  no apontamento de produção
type: support-article
updated_at: '2022-02-01T19:36:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028861332-Manufatura-Linha-Protheus-SIGAPCP-Considerar-a-informa%C3%A7%C3%A3o-do-campo-Perda-no-apontamento-de-produ%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:45 min****Dúvida**Como fazer com que o Sistema considere a informação do campo **Perda** das rotinas de apontamento de produção?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Para que essa informação seja considerada e atualize os dados da **OP - Ordem de Produção**, assim como faça a requisição do material empenhado, o parâmetro **MV\_PERDINF - Identifica se a quantidade de perda informada nos apontamentos de produção será tratada de forma informativa ou se compõe o saldo da OP** deve ter o conteúdo **.F.**.  
  
Referente a requisição do material, além do parâmetro **MV\_PERDINF**, o parâmetro **MV\_REQAUT** **- Verifica se o sistema deve ou não gerar requisições automáticas (baseado no empenho) na produção** deve ter o conteúdo **A**.
