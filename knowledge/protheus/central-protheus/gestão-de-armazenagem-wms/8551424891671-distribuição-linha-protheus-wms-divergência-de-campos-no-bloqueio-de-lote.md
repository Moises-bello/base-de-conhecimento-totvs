---
article_id: 8551424891671
category: Gestão de Armazenagem (WMS)
content_hash: 25a355f857460a89a164e9d10a4c711c06df2f81f0107bc30494fbc4de202680
fetched_at: '2026-06-28T22:45:47.927902+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Distribuição - Linha Protheus - WMS - Divergência de Campos no Bloqueio de
  Lote
type: support-article
updated_at: '2023-05-18T12:39:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8551424891671-Distribui%C3%A7%C3%A3o-Linha-Protheus-WMS-Diverg%C3%AAncia-de-Campos-no-Bloqueio-de-Lote
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Qual o procedimento para corrigir a mensagem informando divergência de tamanho nos campos **D0U\_DOCTO** e **DD\_DOC** no **WMSA560**, Bloqueio de Lote?  
  
**Ambiente**TOTVS Distribuição - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS) - Todas as versões  
  
**Solução**A mensagem de divergência é apresentada quando os campos **D0U\_DOCTO** e **DD\_DOC** estão com tamanhos diferentes.  
É necessário acessar o Sistema **SIGACFG**, consultar o **Dicionário de Dados** e verificar se os campos **D0U\_DOCTO** e **DD\_DOC** estão com **9 posições**, caso tenha divergência é necessário equalizar o tamanho dos campos nas tabelas **D0U** e **SDD**.
