---
article_id: 4402252829975
category: Controle de Documentos (SIGAQDO)
content_hash: 86e434f8327ee8a5eae2cc97a639b7998472a3116efd20251eecaf61025a6347
fetched_at: '2026-06-28T22:42:29.183051+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Help QX50NQDOC
type: support-article
updated_at: '2021-06-07T16:54:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402252829975-Manufatura-Linha-Protheus-SIGAQDO-Help-QX50NQDOC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:40 min**  
**Ocorrência**Na rotina de **Questionários - QAXA050** ao tentar alterar um questionário ocorre o *help* **QX50NQDOC - Usuário não tem permissão para Visualizar / Incluir / Alterar / Excluir questionário para o Documento Relacionado**.  
**Ambiente**Totvs Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**O *help* **QX50NQDOC** é apresentado quando o usuário que realiza a operação não possui permissão ou não tem vínculo com o **Documento Relacionado**.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Na rotina **Cadastros de Documentos - QDOA050**, em **Responsáveis**, verifique se o usuário em questão está relacionado como responsável pelo documento;  
2. Caso o usuário esteja relacionado ao documento na rotina **QDOA050** e ainda assim ocorrer o *help*,  acesse a rotina **QDOA020 - Tipos de Documentos** e valide em **Outras Ações/Nív. Resp** se a etapa do usuário tem permissão de alterar o documento igual a **sim**.
