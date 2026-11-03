---
article_id: 5543680657431
category: Controle de Documentos (SIGAQDO)
content_hash: aab63422bd6f2697b41067036fa224ee7750147cbde1fb753cf97b2f7742f2ab
fetched_at: '2026-06-28T22:42:29.148348+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Help QDO50NARSP
type: support-article
updated_at: '2022-04-19T17:38:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5543680657431-Manufatura-Linha-Protheus-SIGAQDO-Help-QDO50NARSP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:30 min****Ocorrência**Na rotina **QDOA050 - Cadastro de Documentos** ao tentar alterar o responsável pelo documento é apresentado o *help* **QDO50NARSP - Nao podera ser alterado os responsaveis das etapas anteriores ou igual a etapa atual**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões.  
  
**Causa**Esse incidente ocorre porque o usuário **não tem permissão de alterar** os usuários responsáveis ou está tentando alterar o responsável por uma etapa já baixada ou pela etapa atual.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acessar a rotina **QDOA020 - Tipos de Documentos** e ir em **Ações Relacionadas > Niv. Resp** e confirmar se o campo **Altera Doc** está com o conteúdo igual a **Sim**.
