---
article_id: 1500004184761
category: Controle de Não Conformidades (SIGAQNC)
content_hash: 2570128952068303bfe4777ca6839d5dd18e11805aaa33abc015f4def9657fa3
fetched_at: '2026-06-28T22:42:27.950869+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - FNC Sigilosa no QNCA040
type: support-article
updated_at: '2021-05-12T20:59:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004184761-Manufatura-Linha-Protheus-SIGAQNC-FNC-Sigilosa-no-QNCA040
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**Ao alterar ou visualizar a **FNC - Ficha de Não-Conformidade** na rotina **QNCA040 - Cadastro de Ocorrências/Não-Conformidades** é exibida a mensagem **Ficha de Ocorrências/Não-conformidades sigilosa. Somente o usuário digitador (XXX) e/ou responsável (YYY) terão acesso aos dados**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) – Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Causa**A mensagem é exibida ao alterar ou visualizar a **FNC** na rotina **QNCA040** quando a **FNC** está com o campo **QI2\_SIGILO - Sigilo?** Igual à **1-Sim**.   
  
**Solução**Somente o usuário responsável ou digitador desta **FNC** que poderão visualizar ou alterar este registro.  
Para identificar qual é o usuário responsável pela **FNC**, verifique qual é a matrícula que consta no campo **QI2\_MATRES - Cod. Usr Resp** da rotina **QNCA040**.  
E para identificar qual o usuário que incluiu esta **FNC**, verifique qual é a matrícula que consta no campo **QI2\_MAT - Mat Usr Resp**.  
  
**Saiba mais**  
Além disso, também é possível definir outros usuários possam manipular uma **FNC** sigilosa, por meio da utilização do **PE - Ponto de Entrada** [QNC40SIG - Define se a FNC deve continuar como sigilosa](https://tdn.totvs.com/display/public/PROT/QNC40SIG+-+Define+se+a+FNC+deve+continuar+como+sigilosa).
