---
article_id: 7395876153751
category: Controle de Documentos (SIGAQDO)
content_hash: a25a93e14b1877fcdd450e69c8f1f0cd5669462fac3862ea0b49cc4df0f3066c
fetched_at: '2026-06-28T22:42:29.071782+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Existe solicitação de Alteração para
  este Documento
type: support-article
updated_at: '2022-07-12T20:58:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7395876153751-Manufatura-Linha-Protheus-SIGAQDO-Existe-solicita%C3%A7%C3%A3o-de-Altera%C3%A7%C3%A3o-para-este-Documento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:10 min****Ocorrência**No módulo **SIGAQDO - Controle de Documentos**, ao tentar realizar a transferência de departamento por meio da rotina **QAXA010 - Cadastro de Usuários** é apresentada a mensagem **O usuário informado para receber o aviso de (Existe solicitação de Alteração para este Documento) no documento xxxx, NÃO está indicado como permissão Gerar Revisão no cadastro!**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**Esta mensagem é apresentada quando o usuário não está com permissão para gerar revisão definida para o nível de responsabilidade no cadastro do tipo de documento.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Para o documento indicado na mensagem, verifique qual é o nível de responsabilidade deste usuário por meio da opção **Responsáveis** na rotina **QDOA050 - Documentos**;  
2. Consulte na rotina **QDOA020 - Tipo de Documento**, o tipo de documento utilizado neste documento, e em **Outras Ações/Niv Respons**, verifique se para o nível de responsabilidade deste usuário o campo **Gera Revisão** está como **Sim**.
