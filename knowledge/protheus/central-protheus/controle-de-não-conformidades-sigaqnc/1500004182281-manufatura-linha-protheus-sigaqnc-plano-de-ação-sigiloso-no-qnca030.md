---
article_id: 1500004182281
category: Controle de Não Conformidades (SIGAQNC)
content_hash: 0786e63595dd34938efa9071af68282e3509640b85a6625da0e2e5ea65b44f6c
fetched_at: '2026-06-28T22:42:28.020601+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Plano de Ação Sigiloso no QNCA030
type: support-article
updated_at: '2021-05-20T10:51:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004182281-Manufatura-Linha-Protheus-SIGAQNC-Plano-de-A%C3%A7%C3%A3o-Sigiloso-no-QNCA030
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:10 min**  
**Ocorrência**Ao alterar o plano de ação na rotina **QNCA030 - Cadastro de Plano de Ação** é exibida a mensagem **Plano de Ação Sigiloso. Terão acessos aos dados XXX, YYY, ZZZ tem acesso aos dados**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Causa**A mensagem é exibida quando o plano está com o campo **QI3\_SIGILO - Sigilo?** Igual à **1-Sim**.   
  
**Solução**Somente o usuário responsável pelo plano e os usuários responsáveis por cada etapa, poderão alterar este plano de ação.  
Para identificar qual é o usuário responsável pelo plano, verifique qual é a matrícula que consta no campo **QI3\_MAT - Mat. Usr Resp** da rotina **QNCA030**.  
E para identificar quais os usuários responsáveis por cada etapa deste plano, consulte o plano na rotina **QNCA030** e em **Outras Ações/Ação/Etap**, verifique qual é a matrícula que consta no campo **QI5\_MAT - Mat Usr Resp** de cada etapa.  
  
**Saiba mais**  
Além disso, também é possível definir outros usuários responsáveis por alteração em plano de ação sigiloso, por meio da utilização do **PE - Ponto de Entrada** [QNC40SIG - Define se a FNC deve continuar como sigilosa](https://tdn.totvs.com/display/public/PROT/QNC40SIG+-+Define+se+a+FNC+deve+continuar+como+sigilosa).
