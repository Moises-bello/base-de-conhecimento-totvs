---
article_id: 360046173554
category: Inspeção de Entradas (SIGAQIE)
content_hash: 322f161249909c2003bcc78665de12fcd5e2cfef5274a5e571be9a2f33dc8570
fetched_at: '2026-06-28T22:42:27.037754+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Help SEMPERM na rotina QIEA010
type: support-article
updated_at: '2021-08-09T12:21:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046173554-Manufatura-Linha-Protheus-SIGAQIE-Help-SEMPERM-na-rotina-QIEA010
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:50 min**  
**Ocorrência**No módulo **SIGAQIE - Inspeção de Entradas**, ao tentar excluir uma especificação de produto na rotina **QIEA010 - Especificação de Produtos** é apresentado o *help* **SEMPERM - Usuário sem permissão para utilizar esta rotina**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Causa**O *help* **SEMPERM** é exibido na rotina **QIEA010** quando o usuário em questão não possui o acesso marcado em **1 - Excluir Produtos** no cadastro de usuários no **SIGACFG - Configurador**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acessar o **SIGACFG - Configurador**;  
2. No Menu **Usuário/Senhas/Usuários**, alterar o usuário em questão;  
3. Na aba **Restrições de Acesso/Acesso**, marcar o código de acesso **1 - Excluir Produtos**.
