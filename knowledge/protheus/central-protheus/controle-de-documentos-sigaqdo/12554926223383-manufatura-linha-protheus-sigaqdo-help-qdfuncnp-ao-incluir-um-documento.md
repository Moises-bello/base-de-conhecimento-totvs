---
article_id: 12554926223383
category: Controle de Documentos (SIGAQDO)
content_hash: 5306f1eed53fad8a3817455b217011cce2e147a0e247fa4cb80917aee1556008
fetched_at: '2026-06-28T22:42:29.134496+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Help QDFUNCNP ao incluir um documento
type: support-article
updated_at: '2023-02-20T18:27:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12554926223383-Manufatura-Linha-Protheus-SIGAQDO-Help-QDFUNCNP-ao-incluir-um-documento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:05 min****Ocorrência**Na rotina **QDOA050** **- Cadastro de Documentos**, ao incluir documento e informar os responsáveis é apresentado *help* **QDFUNCNP - Funcionário não tem permissão para ser responsável**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**O *help* **QDFUNCNP** ocorre em duas situações:

1. Quando um ou mais usuários responsáveis pelo documento não estão ativos;
2. Quando um ou mais responsáveis não são do mesmo departamento e cargo definidos para o tipo de documento.

**Solução**Para solucionar, execute os passos a seguir:

1. É necessário verificar se o campo **Status Usr.** está como **1-Ativo** e o campo **Data Fim** em branco na rotina **QAXA010 - Usuários;**
2. Verificar se na rotina **QDOA020 - Tipos de Documentos** para o tipo de documento em questão, em **Outras Ações/Respons** se o departamento e cargo definidos para cada nível de responsabilidade no campos **Cod Dep** e **Cargo** são os mesmos do usuário selecionado de acordo com os campos **Código Depto** e **Cod. Função** da rotina **QAXA010**.
