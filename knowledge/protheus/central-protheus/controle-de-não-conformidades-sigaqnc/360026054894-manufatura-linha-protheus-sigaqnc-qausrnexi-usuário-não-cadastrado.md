---
article_id: 360026054894
category: Controle de Não Conformidades (SIGAQNC)
content_hash: 389e5794a3175b0f571059facd2c7cf5629936556d36f081f8860c9dd871cf30
fetched_at: '2026-06-28T22:42:28.035449+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - QAUSRNEXI - Usuário não cadastrado
type: support-article
updated_at: '2021-09-08T12:58:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026054894-Manufatura-Linha-Protheus-SIGAQNC-QAUSRNEXI-Usu%C3%A1rio-n%C3%A3o-cadastrado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**Na rotina **QNCA040 - Ficha de Ocorrência e de Não Conformidade**, ao tentar informar um usuário responsável, é apresentada a mensagem **QAUSRNEXI - Usuário não cadastrado**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Causa**A mensagem **QAUSRNEXI** ocorre quando existem dados incorretos nos campos referente a **Filial da Matrícula do Usuário -** **QUB\_FILMAT** ou **Código do Responsável -** **QUB\_AUDLIDER.** Estas informações precisam estar equivalentes à filial e matrícula do usuário existentes na tabela **QAA - Usuários**.   
  
**Solução**Geralmente ocorre divergência quando a tabela **QAA** não está em modo exclusivo. A tabela **QAA** sempre deve estar em modo **exclusivo**, nunca compartilhada. Caso a tabela **QAA** já estiver em modo **exclusivo**, verificar se os campos de cada linha abaixo estão com o mesmo tamanho e conteúdo.

* **QAA\_FILIAL = QUB\_FILMAT**
* **QAA\_MAT = QUB\_AUDLIDER**
