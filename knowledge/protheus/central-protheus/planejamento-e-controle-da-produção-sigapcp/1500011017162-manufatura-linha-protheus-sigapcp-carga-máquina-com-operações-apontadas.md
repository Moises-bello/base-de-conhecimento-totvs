---
article_id: 1500011017162
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 29eb3f4a3286ed10ca9cd6e6c0472e56a049b39957fe4f7124b32f631a5bbc00
fetched_at: '2026-06-28T22:42:41.026554+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Carga máquina com operações apontadas
type: support-article
updated_at: '2021-05-17T11:58:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011017162-Manufatura-Linha-Protheus-SIGAPCP-Carga-m%C3%A1quina-com-opera%C3%A7%C3%B5es-apontadas
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:05 min**  
**Dúvida**Na execução do **MATA690 - Carga Máquina**, como ocorre a alocação para aquelas operações que já foram apontadas total ou parcialmente?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Na lista de parâmetros do **MATA690** temos o parâmetro **Considera Saldo**, que tem as opções **Ordem de Produção**, **Operação** e **Saldo por Tempo.**Quando selecionada a opção **Ordem de Produção**, o **MATA690** aloca todas as operações do roteiro, inclusive aquelas que já tiveram apontamentos parciais ou totais, considerando a quantidade da **OP - Ordem de Produção**, sem levar em consideração os registros de apontamentos já realizados.  
Quando selecionada a opção **Operação**, o **MATA690** considera para cada operação a quantidade pendente de apontamento, isto é, a quantidade total da **OP** subtraída da quantidade já apontada daquela operação.  
Já quando selecionada a opção **Saldo por Tempo**, o **MATA690** verifica o tempo previsto para cada operação, e o tempo total já apontado daquela operação, alocando a diferença.
