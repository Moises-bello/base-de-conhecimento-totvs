---
article_id: 12555092736279
category: Controle de Documentos (SIGAQDO)
content_hash: 9c198b7d572e0a2fd833133d2a6223371544b1c206c46b702cd9c9bc97d98522
fetched_at: '2026-06-28T22:42:29.137792+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Help QDFUNCNP ao transferir a pendência
  de um usuário
type: support-article
updated_at: '2023-05-02T18:37:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12555092736279-Manufatura-Linha-Protheus-SIGAQDO-Help-QDFUNCNP-ao-transferir-a-pend%C3%AAncia-de-um-usu%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:45 min****Ocorrência**Na rotina **QAXA010 - Usuários**, ao tentar transferir uma pendência de um usuário por meio da opção **Outras Ações/Transferir** é apresentado *help* **QDFUNCNP - Funcionário não tem permissão para ser responsável**.]  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**Este *help* ocorre quando o usuário que está realizando a ação, não possui permissão para transferir pendências.  
  
**Solução**Para solucionar essa ocorrência, verifique no **SIGACFG - Configurador** no **Menu Usuários/Senhas/Usuários**, se o usuário que está realizando esta ação possui a permissão **102 - Transfere Pendências** marcada aba **Restrições de Acesso/Acessos**.
