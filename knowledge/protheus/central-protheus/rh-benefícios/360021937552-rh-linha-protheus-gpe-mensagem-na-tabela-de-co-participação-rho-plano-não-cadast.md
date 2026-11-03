---
article_id: 360021937552
category: RH - Benefícios
content_hash: dc6351c52cfc3fd25e16e80b33ba3e021ec16533313f9ccfcf9cefe75d1e2531
fetched_at: '2026-06-28T22:44:04.704378+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Mensagem na tabela de co-participação RHO "Plano
  não cadastrado para o usuário"
type: support-article
updated_at: '2025-09-04T19:50:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021937552-RH-Linha-Protheus-GPE-Mensagem-na-tabela-de-co-participa%C3%A7%C3%A3o-RHO-Plano-n%C3%A3o-cadastrado-para-o-usu%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32417709157527) Tempo aproximado para leitura: **00:01:00 min****Dúvida**O que verificar quando gera a mensagem "Plano não cadastrado para o usuário"?  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Na rotina **Coparticipação/Reembolso** em **Atualizações> Benefícios> Coparticipação/Reembolso (GPEA003),** deverá verificar se o campo **RHO\_CODIGO(Sequencia)** está preenchido, este campo não vem automático pelo sistema, no momento da inclusão temos que informar dando F3.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32417709172759)

**Observação:** Esse campo **Sequencia** só será preenchido caso no campo **Origem** seja determinado Dependente/Agregado. 

**Saiba mais:**  
[RH - Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597251-RH-Benef%C3%ADcios)
