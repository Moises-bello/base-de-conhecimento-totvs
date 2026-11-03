---
article_id: 5896605185815
category: Controle de Não Conformidades (SIGAQNC)
content_hash: ec1fc93b7c3875a840fdfb360f57b6fd05d1af92b7d86f67ce1d59864b22b124
fetched_at: '2026-06-28T22:42:27.876832+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - A FNC não poderá ser encerrada em status
  (Registrada / Em Análise)
type: support-article
updated_at: '2022-05-05T20:00:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5896605185815-Manufatura-Linha-Protheus-SIGAQNC-A-FNC-n%C3%A3o-poder%C3%A1-ser-encerrada-em-status-Registrada-Em-An%C3%A1lise
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:35 min****Ocorrência**Na rotina **QNCA040 - Cadastro de Não Conformidades** ao tentar registrar ou alterar uma **FNC - Ficha de Não Conformidade** ocorre a mensagem **A FNC não poderá ser encerrada em status (Registrada / Em Análise)**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Causa**A mensagem ocorre quando no campo **Situação** é selecionada a opção **1 - Registrada** ou **2 - Em Análise** e o campo **DT.Con.Real** está preenchido.  
O preenchimento do campo **DT.Con.Real** apenas é habilitado quando no campo **Situação** é selecionada a opção **3 - Procede**, **4 - Não Procede** ou **5 - Cancelada**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. O campo **DT.Con.Real** não deve ser preenchido se a **Situação** selecionada for **1 - Registrada** ou **2 - Em Análise**.
