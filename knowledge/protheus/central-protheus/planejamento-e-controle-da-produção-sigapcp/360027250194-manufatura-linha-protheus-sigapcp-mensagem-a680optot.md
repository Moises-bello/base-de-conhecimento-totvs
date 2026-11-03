---
article_id: 360027250194
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 8e24574cf10e5ebb8d8ca1f9b7c9716f7fcfc002ffb35791ff43a4dbf9e03b77
fetched_at: '2026-06-28T22:42:43.621886+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem A680OPTOT
type: support-article
updated_at: '2024-06-19T20:30:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027250194-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-A680OPTOT
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24128095375127)***Tempo aproximado para leitura: **00:00:55 min**  
**Ocorrência**Ao tentar realizar um apontamento de produção por meio da rotina **MATA680 - Apontamento Modelo I** ou **MATA681 - Apontamento Modelo II** o usuário recebe a mensagem **A680OPTOT - Capacidade da Operação desta OP já está totalizada**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**A **OP - Ordem de Produção** já foi finalizada e o campo **C2\_DATRF** - **Dt Real Fim**está preenchido, ou a operação que está sendo apontada já foi finalizada, isto é, existe um registro para essa **OP** e operação com o campo **H6\_PT** **- Parc. Total** com conteúdo **T**.  
  
**Solução**Verifique se a **OP** e operação que o usuário deseja apontar estão corretas, ou verifique os apontamentos já realizados para essa **OP** ou **OP** e operação, se for necessário realizar o novo apontamento é necessário estornar o apontamento que encerrou a operação e/ou **OP**.
