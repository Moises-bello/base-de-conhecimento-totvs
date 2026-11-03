---
article_id: 6675316597527
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 7b435edb921002b348cf641048302984cbf6803794ed6137a3fd3b57236de1d3
fetched_at: '2026-06-28T22:42:44.526720+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem O MRP está em execução pelo
  usuário XXXX no ticket XXXX
type: support-article
updated_at: '2024-02-07T13:17:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6675316597527-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-O-MRP-est%C3%A1-em-execu%C3%A7%C3%A3o-pelo-usu%C3%A1rio-XXXX-no-ticket-XXXX
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:45 min  
  
Ocorrência**No módulo **SIGAPCP - Planejamento e Controle da Produção** é apresentado a mensagem **O MRP está em execução pelo usuário XXXX no ticket XXXX**, ao executar a rotina **PCPA712 - MRP memória**. **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**  
O **MRP - Material Requiriment Planning** já está em utilização por outro usuário.  
  
**Solução**  
É necessário que o **usuário** que fez a execução do **ticket** apresentado na mensagem, acesse a rotina **PCPA712** e faça a **liberação**.  
Caso não apresente o **usuário** na mensagem, através da tabela **HW3 - Processamentos do MRP** é possível identificar o usuário que fez a **execução** do **ticket**.
