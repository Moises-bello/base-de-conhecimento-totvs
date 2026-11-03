---
article_id: 360026128373
category: Controle de Documentos (SIGAQDO)
content_hash: 800d0fca8a47852d8b2aa28a1001f6c922b668c6ccad1be3a6b0984b35fe107f
fetched_at: '2026-06-28T22:42:29.131192+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Help QDFUNCNP ao gerar revisão de um
  documento
type: support-article
updated_at: '2023-02-20T18:24:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026128373-Manufatura-Linha-Protheus-SIGAQDO-Help-QDFUNCNP-ao-gerar-revis%C3%A3o-de-um-documento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:15 min**  
**Ocorrência**Na rotina **QDOA050** **- Cadastro de Documentos**, ao incluir uma revisão do documento e salvar a tela de responsáveis ou finalizar o documento, é apresentada a mensagem: **QDFUNCNP - Funcionário não tem permissão para ser responsável**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**A mensagem **QDFUNCNP** ocorre em duas situações:

1. Quando um ou mais usuários responsáveis pelo documento foram transferidos de cargo ou departamento e após isto, deixaram de possuir a permissão para baixa da pendência.
2. Quando o responsável não está parametrizado para acumular revisão.

**Solução**Para solucionar, execute os passos a seguir:

1. É necessário transferir as pendências do usuário que não possui a permissão para um novo usuário responsável.
2. Verificar se na rotina **QDOA020 - Tipos de Documentos** para o tipo de documento em questão, em **Outras Ações/Respon**s se o campo **Acum. Revisão** está marcado como **Sim**.

**Saiba mais**Em caso de dúvidas a respeito do processo de transferência de pendências, consulte o artigo  
[Manufatura - Linha Protheus - SIGAQDO - Transferência de pendências para um novo usuário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021357911-MP-QUA-Transfer%C3%AAncia-de-pend%C3%AAncias-para-um-novo-usu%C3%A1rio)
