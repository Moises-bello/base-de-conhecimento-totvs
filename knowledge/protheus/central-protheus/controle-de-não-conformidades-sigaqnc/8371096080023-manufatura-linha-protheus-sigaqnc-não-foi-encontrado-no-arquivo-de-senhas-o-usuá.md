---
article_id: 8371096080023
category: Controle de Não Conformidades (SIGAQNC)
content_hash: 6b564eee8bec83d482ad8ef0fab6d02f0006d38a211dbb6a1e53449e8bb71ca3
fetched_at: '2026-06-28T22:42:28.006672+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Não foi encontrado no arquivo de senhas o usuário com o login cadastrado
type: support-article
updated_at: '2023-09-08T18:30:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8371096080023-Manufatura-Linha-Protheus-SIGAQNC-N%C3%A3o-foi-encontrado-no-arquivo-de-senhas-o-usu%C3%A1rio-com-o-login-cadastrado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17381745868695) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao acessar o módulo **SIGAQNC - Controle de Não Conformidades** é exibida a mensagem **Não foi encontrado no arquivo de senhas o usuário com o login cadastrado**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Não Conformidades (SIGAQNC) – Versão 12  
  
**Causa**Esta mensagem ocorre em duas situações:  
1. Quando o usuário que está acessando o módulo, não está cadastrado como usuário na rotina **QAXA010 - Usuários**, registrando a tabela **QAA - Usuários** e/ou;  
2. Existe alguma inconsistência referente ao *login* do usuário na tabela **QAA**, no campo **QAA\_LOGIN - Login**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique se o usuário está cadastrado na rotina **QAXA010**;  
2. Se já estiver cadastrado, verifique:  
2.1. Se não há espaços em branco no conteúdo do campo **QAA\_LOGIN**;  
2.2. Se o conteúdo deste campo é diferente do campo **QAA\_APELID - Apelido**. Os campos **QAA\_LOGIN** e **QAA\_APELID** precisam ser iguais.
