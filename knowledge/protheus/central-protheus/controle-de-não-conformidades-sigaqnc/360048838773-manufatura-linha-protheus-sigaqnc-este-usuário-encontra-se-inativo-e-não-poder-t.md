---
article_id: 360048838773
category: Controle de Não Conformidades (SIGAQNC)
content_hash: 430ef499ee81fc460958a461dbe9602cc7f114db19833ad35d604494d06bdfda
fetched_at: '2026-06-28T22:42:27.937891+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Este usuário encontra-se inativo e
  não poder ter acesso aos Sistemas de qualidade. Seu login será bloqueado para evitar
  problemas de inconsistência na base de dados
type: support-article
updated_at: '2021-12-09T20:30:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048838773-Manufatura-Linha-Protheus-SIGAQNC-Este-usu%C3%A1rio-encontra-se-inativo-e-n%C3%A3o-poder-ter-acesso-aos-Sistemas-de-qualidade-Seu-login-ser%C3%A1-bloqueado-para-evitar-problemas-de-inconsist%C3%AAncia-na-base-de-dados
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:15 min**  
**Ocorrência**Ao tentar acesso ao módulo **24 - Controle de Documentos** ou **36 - Controle de Não Conformidades** é exibida a mensagem **Este usuário encontra-se inativo e não poder ter acesso aos Sistemas de qualidade. Seu login será bloqueado para evitar problemas de inconsistência na base de dados**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) – Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Causa**Esta mensagem ocorre quando o usuário em questão não possui cadastro na rotina **QNCA070 - Usuários** ou **QAXA010 -** **Usuários**. Isto é, além do cadastro de usuário do **SIGACFG - Configurador**, o usuário em questão precisa ter seu *login* vinculado à um cadastro de usuário na rotina de **Usuários**.  
  
**Solução**Para solucionar esta mensagem é necessário incluir um usuário nas rotinas **QNCA070** ou **QAXA010** vinculado ao *login* do usuário.  
  
**Importante**  
Caso o usuário já estiver cadastrado e mesmo assim a mensagem persistir, verifique na tabela **QAA - Usuários** se existem dois usuários apontando para o mesmo *login*. Esta verificação poderá ser realizada filtrando pelo campo **QAA\_LOGIN - Login Usr**. Caso existirem dois usuários com o mesmo *login*, é necessário manter **apenas um usuário** para evitar inconsistência nas informações.
