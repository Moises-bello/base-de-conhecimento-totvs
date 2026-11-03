---
article_id: 360026469531
category: Controle de Documentos (SIGAQDO)
content_hash: 96c50d7decf1265235c36e37c25a1f783c799b5e4f14237c3de04f1be6d71e77
fetched_at: '2026-06-28T22:42:29.960139+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Usuário da próxima pendência inativo
type: support-article
updated_at: '2021-10-08T13:31:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026469531-Manufatura-Linha-Protheus-SIGAQDO-Usu%C3%A1rio-da-pr%C3%B3xima-pend%C3%AAncia-inativo
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)* Tempo aproximado para leitura: **00:01:10 min****Ocorrência**Ao realizar a baixa de uma pendência no módulo **SIGAQDO - Controle de Documentos** é apresentada a mensagem **Não será possível finalizar, pois o Aprovador, Homologador ou Revisor está inativo. Favor entrar em contato com o responsável pelo cadastro de usuários.**  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**Esta mensagem é apresentada porque o responsável pela próxima pendência está **inativo** e não existe outro usuário com o mesmo departamento e função para realizar a baixa da pendência.   
  
**Solução**É necessário alterar o usuário responsável pela próxima etapa do processo de revisão do documento. O usuário que está com a pendência atual, deve acessar a opção **Responsáveis** existente no **QDOA050 - Cadastro de Documentos**, deletar o usuário inativo e incluir um novo usuário.  
  
**Importante**Caso o Protheus não permitir realizar esta alteração, acesse a rotina **QDOA020 - Tipos de Documentos**, botão **Outras Ações** > **Niv Resp**. A coluna **Altera Documento** deverá estar igual a **Sim** para a etapa do usuário que está com a pendência no momento. Desta forma o usuário poderá deletar o responsável atual e cadastrar um novo.
