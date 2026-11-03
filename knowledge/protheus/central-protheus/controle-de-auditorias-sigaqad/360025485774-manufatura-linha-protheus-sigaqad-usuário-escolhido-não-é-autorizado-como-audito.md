---
article_id: 360025485774
category: Controle de Auditorias (SIGAQAD)
content_hash: cfdc32bcca13b9d7d4943337f44234f5b8d358c46d5af96624e5a05cefcfa86c
fetched_at: '2026-06-28T22:42:30.902956+00:00'
product: protheus
section_id: 360005876634
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQAD - Usuário escolhido não é autorizado
  como Auditor
type: support-article
updated_at: '2021-08-16T14:07:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025485774-Manufatura-Linha-Protheus-SIGAQAD-Usu%C3%A1rio-escolhido-n%C3%A3o-%C3%A9-autorizado-como-Auditor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**Ao informar um usuário como auditor na rotina **Agenda de Auditorias - QADA150**, é apresentada a mensagem **Usuário escolhido não é autorizado como Auditor**.   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Auditorias (SIGAQAD) - Todas as versões  
  
**Causa**Esta mensagem é apresentada quando o usuário em questão não foi marcado como auditor no **Cadastro de Usuários e Auditores - QIEA050**.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse a rotina **Usuários e Auditores**;  
2. Selecione o usuário que precisa ser selecionado como auditor e clique em **Alterar**;  
3. Marque o campo **Auditor - QAA\_AUDIT** como **1 - Sim** e clique em **Salvar**.
