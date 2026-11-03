---
article_id: 1500012899501
category: Controle de Documentos (SIGAQDO)
content_hash: 59ec8b749033bfde4d331701a1ce853135f69b1c7f39f62019354ff31403ee11
fetched_at: '2026-06-28T22:42:29.034941+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Documentos com Inconsistência na Transferência
  devido ao cadastro, Responsáveis no Tipo de Documento
type: support-article
updated_at: '2021-06-02T14:49:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012899501-Manufatura-Linha-Protheus-SIGAQDO-Documentos-com-Inconsist%C3%AAncia-na-Transfer%C3%AAncia-devido-ao-cadastro-Respons%C3%A1veis-no-Tipo-de-Documento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min**  
**Ocorrência**Na rotina **QAXA010 - Usuários**, ao realizar o procedimento de transferência de pendências para outro usuário, é apresentada a mensagem: **Documentos com Inconsistência na Transferência devido ao cadastro, Responsáveis no Tipo de Documento**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**Esta mensagem em duas situações diferentes:

1. Na transferência das pendências de documentos entre usuários: é exibida quando o usuário destino possui um departamento e/ou cargo/função diferente do usuário de origem;
2. Na transferência de departamento do mesmo usuário: é exibida quando no cadastro dos responsáveis do tipo de documento, não existe o relacionamento do departamento novo com o cargo atual.

**Solução**1. Para solucionar essa ocorrência na transferência das pendências entre usuários, realize os seguintes passos:

* Acesse a rotina **QAXA010** e consulte o usuário de origem, ou seja, o usuário na qual a pendência será transferida, e verifique qual é o departamento do campo **Codigo Depto** e qual a função no campo **Cod. Função**;
* Realize a mesma consulta para o usuário destino, ou seja, o usuário que irá receber a pendência do documento, e verifique se o departamento e função são os mesmos indicados nos campos **Codigo Depto** e **Cod. Função** do usuário de origem;

A pendência somente ser transferida para usuários do mesmo departamento e função/cargo.  
  
2. E para solucionar esta ocorrência na transferência de departamento, realize os seguintes passos:

* Acesse a rotina **QAXA010** e consulte o usuário no qual será transferido de departamento e verifique qual é a função no campo **Cod. Função**;
* Acesse a rotina **QDOA020 - Tipos de Documentos** e em **Outras Ações/Respons** verifique se existe o relacionamento do **departamento novo**, no qual será transferido, com o **cargo atual**, cargo verificado no item anterior. Caso não exista este relacionamento, deverá ser efetuado este cadastro para que seja possível realizar a transferência com sucesso.
