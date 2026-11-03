---
article_id: 1500000523162
category: Controle de Documentos (SIGAQDO)
content_hash: 01e5cce36d80787b08e0b86b8baed1ca1b1e8c594347c5be3f41908d534a2afa
fetched_at: '2026-06-28T22:42:29.155239+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Help QDOA080NUS
type: support-article
updated_at: '2021-05-24T17:48:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000523162-Manufatura-Linha-Protheus-SIGAQDO-Help-QDOA080NUS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:51 min**  
**Ocorrência**No módulo **SIGAQDO - Controle de Documentos**, ao tentar incluir um **treinando** na rotina **QDOA080 - Treinamento** é apresentado *help* **QDOA080NUS - Não existe usuário cadastrado neste departamento/cargo**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**Esse incidente ocorre porque não é permitido incluir um **usuário inativo** ou que não tenha um **código de função** válido vinculado.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

* Acesse a rotina **QAXA010 -** **Cadastro de usuários**;
* Valide no campo **Status Usr.** se o usuário está ativo;
* E no campo **Cod. Função** se existe um **código de função** válido vinculado ao usuário.
