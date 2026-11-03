---
article_id: 360049979034
category: Controle de Documentos (SIGAQDO)
content_hash: e5b77e118b9e88aefd720d2a6fc82d591e94f9ad0a1f126ecf2ee07b05d3ed4b
fetched_at: '2026-06-28T22:42:29.187094+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Help SEMPERM na rotina QDOA052
type: support-article
updated_at: '2021-05-25T13:24:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049979034-Manufatura-Linha-Protheus-SIGAQDO-Help-SEMPERM-na-rotina-QDOA052
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min****Ocorrência**No módulo **SIGAQDO - Controle de Documentos**, ao tentar inserir uma solicitação na rotina **QDOA052 - Cadastro de Solicitações** é apresentado o *help* **SEMPERM - Usuário sem permissão para utilizar esta rotina**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**O *help* **SEMPERM** é exibido na rotina **QDOA052** quando o cadastro do usuário na rotina **QAXA010 - Cadastro de Usuários** o campo **QAA\_APELID** está divergente do campo **QAA\_LOGIN** e/ou a opção **Acesso 92 - Baixa solicitações** não está habilita em**SIGACFG - Configurador**no menu **Usuário/Senhas/Usuários.**  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse a rotina **QAXA010 - Cadastro de Usuários**;  
2. Valide se o nome o reduzido do usuário no campo **QAA\_APELID - Nome Reduzido** está igual ao campo **QAA\_LOGIN - Login do Usuário**;  
3. Confirme no **SIGACFG - Configurador** no menu **Usuário/Senhas/Usuários** se em **Restrições de Acesso** a opção **Acesso 92 - Baixa solicitações** está habilitada.
