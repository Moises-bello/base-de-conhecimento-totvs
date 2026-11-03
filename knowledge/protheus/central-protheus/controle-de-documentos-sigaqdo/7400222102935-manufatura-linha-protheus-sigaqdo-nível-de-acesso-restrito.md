---
article_id: 7400222102935
category: Controle de Documentos (SIGAQDO)
content_hash: 6a4d58c7ccc263b54f2c47efd00ef4feebf53a8d611d39f6dc71d164a53d5ed6
fetched_at: '2026-06-28T22:42:29.204648+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Nível de acesso restrito
type: support-article
updated_at: '2022-07-12T19:48:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7400222102935-Manufatura-Linha-Protheus-SIGAQDO-N%C3%ADvel-de-acesso-restrito
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**No módulo **SIGAQDO - Controle de Documentos**, ao realizar a manutenção de distribuição por meio da rotina **QDOA120 - Manutenção de Distribuição** é exibida a mensagem **Nível de acesso restrito**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**Esta mensagem é exibida quando acessadas as opções **Distribuir por Destinatário**, **Inativar por Destinatário**, **Ativar por Destinatário**, **Distribuir por Documento**, **Inativar por Documento**, **Ativar por Documento** e **Localizadores** quando o usuário em questão não possui permissão para baixar solicitações.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o **SIGACFG - Configurador**;  
2. No *menu* **Usuário/Senhas/Usuários**, consulte o usuário em questão e clique em **Alterar**;  
3. Na aba **Restrições de Acesso** acesse a aba **Acessos** e marque o código de acesso **92 - Baixa de Solicitações**.
