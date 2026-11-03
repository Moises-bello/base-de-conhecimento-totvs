---
article_id: 13117548771991
category: Controle de Documentos (SIGAQDO)
content_hash: f29b472a024920c7c9e9a3a21bf0f9cec7205a4270c9cb0e376b967b87088cad
fetched_at: '2026-06-28T22:42:29.942660+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Todos usuários cadastrados recebem
  pendência de baixa
type: support-article
updated_at: '2023-03-16T12:26:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13117548771991-Manufatura-Linha-Protheus-SIGAQDO-Todos-usu%C3%A1rios-cadastrados-recebem-pend%C3%AAncia-de-baixa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:30 min** **Dúvida**No **SIGAQDO - Controle de Documentos**, como habilitar para que todos os usuários responsáveis cadastrados na rotina **QDOA050 - Cadastro de Documentos** recebam a pendência de baixa?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**Na rotina **QDOA020 - Tipos de Documento**, indo em **Outras Ações/Nív. Resp** é cadastrado o **nível** e o **número mínimo** de usuário responsável por este nível. Se o campo **Baixa Pend** estiver como **Sim**, a quantidade cadastrada no campo **Nr Mínimo** será respeitada e na rotina **QDOA050** a quantidade de usuários que exceder o número mínimo não receberá pendência de baixa. Se o campo **Baixa Pend** estiver com o conteúdo igual a **Não**, todos os usuários cadastrados para este nível receberão pendências.
