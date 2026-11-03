---
article_id: 360043713394
category: Controle de Documentos (SIGAQDO)
content_hash: 56def56fe81c2b6f8dd8b16fb609dec475abe8516245579fe03f629a0c767b06
fetched_at: '2026-06-28T22:42:29.124554+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Help QD050NGRV
type: support-article
updated_at: '2024-02-15T18:04:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043713394-Manufatura-Linha-Protheus-SIGAQDO-Help-QD050NGRV
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**No módulo **SIGAQDO - Controle de Documentos**, ao tentar gerar a revisão de um documento na rotina **QDOA050 - Cadastro de Documentos** em **Outras Ações/Gera Revisão** é apresentado *help* **QD050NGRV - Não gera revisão de documentos com status diferente de Leitura**, **Modificação em Andamento** ou esteja **Obsoleto**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**Esse incidente ocorre porque não é permitido gerar revisão de documento com status diferente de **Leitura**, **Modificação em andamento** ou **Obsoleto**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Na rotina **QDOA050** consultar este documento e em **Outras Ações/Detalhes**, verificar qual é o usuário que está com a pendência de distribuição;  
2. Acessar a rotina **QDOA110 - Distribuição de Documentos** com este usuário, e realizar a distribuição deste documento;  
3. Retornar para a rotina **QDOA050** e em **Outras Ações/Gera Revisão**, gerar a revisão deste documento.
