---
article_id: 16461272927127
category: Inspeção de Processos (SIGAQIP)
content_hash: 1fd5bd9321dcaefaf89c5f07a23cba3be61f560d921022e04eb44333d1e9da7f
fetched_at: '2026-06-28T22:42:25.797520+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Help SEMPERM na rotina QIPA010
type: support-article
updated_at: '2023-08-01T20:35:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16461272927127-Manufatura-Linha-Protheus-SIGAQIP-Help-SEMPERM-na-rotina-QIPA010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16461317915415) Tempo aproximado para leitura: **00:00:35 min****Ocorrência**No módulo **SIGAQIP - Inspeção de Processos**, ao tentar excluir uma especificação de produto na rotina **QIPA010 - Especificação de Produtos** é apresentado o **help SEMPERM - Usuário sem permissão para utilizar esta rotina**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Causa**O *help* **SEMPERM** é exibido na rotina **QIPA010** quando o usuário em questão não possui o acesso marcado em **1 - Excluir Produtos** no cadastro de usuários no **SIGACFG - Configurador**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acessar o **SIGACFG - Configurador**;  
2. No Menu **Usuário/Senhas/Usuários**, alterar o usuário em questão;  
3. Na aba **Restrições de Acesso/Acesso**, marcar o código de acesso **1 - Excluir Produtos**.
