---
article_id: 360025321711
category: Controle de Documentos (SIGAQDO)
content_hash: 08d136e06a267f4c3befa195d71dfb6d2b810fed6007e21082046c9f9b36c5f4
fetched_at: '2026-06-28T22:42:29.046955+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Documentos com Inconsistência na Transferência
  entre usuários de mesma responsabilidade
type: support-article
updated_at: '2021-09-08T12:58:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025321711-Manufatura-Linha-Protheus-SIGAQDO-Documentos-com-Inconsist%C3%AAncia-na-Transfer%C3%AAncia-entre-usu%C3%A1rios-de-mesma-responsabilidade
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:05 min** **Ocorrência**Na rotina **QAXA010 - Usuários**, ao realizar o procedimento de transferência de pendências para outro usuário, é apresentada a mensagem: **Documentos com Inconsistência na Transferência entre usuários de mesma responsabilidade**.  
  
 **Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
 **Causa**Esta mensagem é apresentada quando o usuário marcado para receber a pendência já constar como responsável pela etapa do documento.   
  
 **Solução**Para concluir o processo deverá transferir a pendência para um usuário que não seja responsável pela pendência em questão. O usuário destino não pode constar na tabela **QD0** **- Responsáveis pelo Documento** para este documento ou revisão.   
  
**Importante**  
Caso estiver realizando a transferência de pendências para em seguida inativar o usuário, você precisa apenas garantir que todas as pendências do usuário em questão já estão designadas a outro usuário. Recomendamos a utilização do relatório de **Pendências - QDOR050**para listar todas as pendências do usuário em questão.
