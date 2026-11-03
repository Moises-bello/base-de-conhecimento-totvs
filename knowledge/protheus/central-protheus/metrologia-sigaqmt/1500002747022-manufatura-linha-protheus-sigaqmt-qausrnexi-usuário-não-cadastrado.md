---
article_id: 1500002747022
category: Metrologia (SIGAQMT)
content_hash: c61446f98ecc9b21d8387e3abbeddb0f0947fa0edeb8bbdf15e6817821398952
fetched_at: '2026-06-28T22:42:24.834736+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - QAUSRNEXI - Usuário não cadastrado
type: support-article
updated_at: '2021-07-26T18:22:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002747022-Manufatura-Linha-Protheus-SIGAQMT-QAUSRNEXI-Usu%C3%A1rio-n%C3%A3o-cadastrado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:55 min**  
**Ocorrência**  
Na rotina **QMTA010 - Instrumentos**, ao tentar informar um usuário responsável, é apresentada a mensagem **QAUSRNEXI - Usuário não cadastrado**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Todas as versões  
  
**Causa**A mensagem **QAUSRNEXI** ocorre quando existem dados incorretos nos campos referente a **Filial Resp -****QM2\_FILRES** ou **Responsável -****QM2\_RESP**. Estas informações precisam estar equivalentes à filial e matrícula do usuário existentes na tabela **QAA - Usuários**.   
  
**Solução**Geralmente ocorre divergência quando a tabela **QAA** não está em modo exclusivo. A tabela **QAA** sempre deve estar em modo **exclusivo**, nunca **compartilhada**. Caso a tabela **QAA** já estiver em modo **exclusivo**, verificar se os campos de cada linha abaixo estão com o mesmo tamanho e conteúdo.

* **QAA\_FILIAL = QM2\_FILRES**
* **QAA\_MAT = QM2\_RESP**
