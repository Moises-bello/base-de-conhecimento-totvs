---
article_id: 4403910458519
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 3975ff577e866d797a426a97adbea923a9a042f1e1687497113f019ea516c972
fetched_at: '2026-06-28T22:42:45.834359+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Reabertura de OP ao estornar um apontamento
type: support-article
updated_at: '2025-11-04T19:08:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403910458519-Manufatura-Linha-Protheus-SIGAPCP-Reabertura-de-OP-ao-estornar-um-apontamento
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34705361925143)***Tempo aproximado para leitura: **00:00:40 min**  
**Dúvida**Por que ao estornar um apontamento que encerrou uma **OP - Ordem de Produção** através das rotinas **MATA250 - Produção Simples**, **MATA681 - Produção Mod I** ou **MATA680 - Produção Mod II** a mesma permanece encerrada?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Essa situação ocorre quando no momento do estorno o Sistema apresenta a mensagem informando que a **OP** está encerrada e que após o estorno ela ficará com saldo a produzir. E questiona o usuário se deseja que a **OP** seja liberada para produção, se for respondido **Não**, o campo **C2\_DATRF - Data Real de Fim da OP** não é limpo, mantendo a **OP** encerrada.
