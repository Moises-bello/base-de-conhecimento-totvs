---
article_id: 360048947793
category: Controle de Não Conformidades (SIGAQNC)
content_hash: d14138bc24998909f5c0bfe14ff5d1ce065a0468e58e62d33e25bb94837f4c02
fetched_at: '2026-06-28T22:42:27.987976+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Help QNCNPENDE exibido na rotina QNCA050
type: support-article
updated_at: '2021-05-19T10:42:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048947793-Manufatura-Linha-Protheus-SIGAQNC-Help-QNCNPENDE-exibido-na-rotina-QNCA050
---

***![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**No módulo **SIGAQNC - Controle de Não Conformidades**, ao acessar a rotina **QNCA050 - Pendências** é exibido o *help* **QNCNPENDE - Não existe(m) pendência(s) para você**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) – Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Causa**O *help* **QNCNPENDE** ocorre quando o usuário em questão não possui pendências. Isto é, não existem registros pendente nas tabelas **QI2 - Não Conformidades**, **QI3 - Cadastro de Plano de Ações** e **QI5 - Ação Corretiva x Ações** para este usuário.  
  
**Solução**Para solucionar essa ocorrência, siga as instruções abaixo:

1. Filtre nas tabelas mencionadas acima pelo código de usuário, utilizando os campos **QI2\_MATRES - Cod Usr Resp**, **QI3\_MAT- Mat Usr Resp** e **QI5\_MAT - Mat Usr Resp** em que o *help* é exibido e verifique se existe algum registro pendente;
2. Verifique se o campo **QI2\_CONREA - Dt. Con. Real** está em branco. Se estiver preenchido, indica que a **FNC - Ficha de Não Conformidade** está concluída e portanto, não existe pendência.
