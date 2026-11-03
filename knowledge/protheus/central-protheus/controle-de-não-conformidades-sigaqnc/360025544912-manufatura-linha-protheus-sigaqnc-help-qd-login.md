---
article_id: 360025544912
category: Controle de Não Conformidades (SIGAQNC)
content_hash: 1cdfa2eeabab4d74bb15aeaac2d7efe697e044c3c143275877c3ef251b178507
fetched_at: '2026-06-28T22:42:27.965251+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Help QD_LOGIN
type: support-article
updated_at: '2022-10-07T13:53:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025544912-Manufatura-Linha-Protheus-SIGAQNC-Help-QD-LOGIN
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Ao acessar uma rotina qualquer dos módulos **SIGAQDO - Controle de Documentos** ou **SIGAQNC -****Controle de Não Conformidades**, é apresentada a mensagem: **QD\_LOGIN. Problema: O usuário atual não possui um login cadastrado igual ao apelido do configurador.**   
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) – Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Causa**  
A mensagem **QD\_LOGIN** ocorre quando o usuário em questão não possui cadastro na rotina de **Usuários - QNCA070** ou **QAXA010**. Isto é, além do cadastro de usuário do **SIGACFG - Configurador**, o usuário em questão precisa ter seu login vinculado à um cadastro de usuário na rotina de **Usuários**.   
  
**Solução**Para solucionar este *help*, verifique as instruções abaixo:  
1. Verifique se o *login* do usuário já está cadastrado nas rotinas **QNCA070** ou **QAXA010**. Se não estiver, deve ser cadastrado;  
2. Caso o usuário já estiver cadastrado e mesmo assim a mensagem persistir, verifique na tabela **QAA - Usuários** se existem dois usuários apontando para o mesmo *login*. Esta verificação poderá ser realizada filtrando pelo campo **QAA\_LOGIN - Login Usuário**. Caso existirem dois usuários com o mesmo *login*, é necessário manter **apenas um usuário** para evitar inconsistência nas informações;  
3. Indicamos que os campos **QAA\_LOGIN** e **QAA\_APELID - Apelido** sejam iguais (não obrigatório);  
4. O campo **QAA\_EMAIL - E-mail** deve estar preenchido.  
  
**Importante**  
Esta mensagem também pode ocorrer em outros módulos pertencentes ao **Protheus Qualidade**.
