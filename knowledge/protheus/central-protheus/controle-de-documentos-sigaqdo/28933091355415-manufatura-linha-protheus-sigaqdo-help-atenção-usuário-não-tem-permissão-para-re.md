---
article_id: 28933091355415
category: Controle de Documentos (SIGAQDO)
content_hash: 4322bb38c14fa0658701c659f15471f5c04a399b15cde1f1e627dec4e295161b
fetched_at: '2026-06-28T22:42:29.109265+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Help Atenção - Usuário não tem permissão
  para receber aviso
type: support-article
updated_at: '2025-01-22T16:57:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28933091355415-Manufatura-Linha-Protheus-SIGAQDO-Help-Aten%C3%A7%C3%A3o-Usu%C3%A1rio-n%C3%A3o-tem-permiss%C3%A3o-para-receber-aviso
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28933068124311) Tempo aproximado para leitura: **00:00:40 min****Ocorrência**Na rotina **QAXA010 - Usuários**, ao efetuar a transferência de departamento ocorre o ***Help* Atenção - Usuário não tem permissão para receber aviso**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
**Causa**O *help* **Atenção** ocorre em bases onde há divergência entre o departamento do usuário no cadastro da **responsabilidade do documento** com o departamento do **aviso de pendência** do usuário. Esta situação não é reproduzida em ambiente padrão atualizado, possivelmente oriunda de customizações via **Ponto de Entrada** ou manipulações via **Base de Dados**.  
  
**Solução**  
Para efetuar a transferência de departamento, realize os seguintes passos:  
1. Transferir a pendência de aviso do usuário responsável para outro usuário;  
2. Transferir o departamento do usuário responsável.
