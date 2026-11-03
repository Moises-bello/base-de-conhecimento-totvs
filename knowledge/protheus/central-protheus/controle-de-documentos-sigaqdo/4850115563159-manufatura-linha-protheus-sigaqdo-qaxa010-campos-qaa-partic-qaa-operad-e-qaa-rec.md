---
article_id: 4850115563159
category: Controle de Documentos (SIGAQDO)
content_hash: ea8f2f8f5ec64f573f9a893b2078056acf6deb4dde3edba42f89eaec3f968af3
fetched_at: '2026-06-28T22:42:29.261472+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - QAXA010 - Campos QAA_PARTIC, QAA_OPERAD
  e QAA_RECUR
type: support-article
updated_at: '2022-03-18T16:43:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4850115563159-Manufatura-Linha-Protheus-SIGAQDO-QAXA010-Campos-QAA-PARTIC-QAA-OPERAD-e-QAA-RECUR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:10 min** **Dúvida**Em qual rotina é realizado o cadastro dos campos **QAA\_PARTIC - Código de Participantes**, **QAA\_OPERAD - Código do Operador** e **QAA\_RECUR - Código do Recurso** utilizado no **QAXA010 - Cadastro de Usuários**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**Os campos **QAA\_PARTIC**, **QAA\_OPERAD** e **QAA\_RECUR** somente devem ser preenchidos caso o módulo **SIGAQDO - Controle de Documentos** esteja integrado com os módulos citados abaixo, referente cada campo:

* O campo **QAA\_PARTIC** faz referência ao módulo de **SIGAAPD - Arquitetura Organizacional** e é cadastrado por meio da rotina **APDA020 - Participantes** e gravado na tabela **RD0 - Pessoas/Participantes**;
* O campo **QAA\_OPERAD** deve ser preenchido nos casos de integração com o módulo de **SIGATMK - Call Center**. Os operadores são cadastrados na rotina **TMKA090 - Operadores** e gravados na tabela **SU7 - Operadores**.
* E o campo **QAA\_RECUR** pertence ao módulo de **SIGAPMS - Gestão de Projetos**. É cadastrado através da rotina **PMSA050 - Recursos de Projetos** e gravado na tabela **AE8 - Recursos de Projetos**.
