---
article_id: 27570528237719
category: Gestão de Transportes (TMS)
content_hash: 0e3fbb19cd374b476a9894b2f6da07a663f60e650860fcad3140cd8814b315da
fetched_at: '2026-06-28T22:45:27.233730+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ajuste tamanho do campo DL8_ID
type: support-article
updated_at: '2024-11-05T14:45:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27570528237719-Log%C3%ADstica-Linha-Protheus-TMS-Ajuste-tamanho-do-campo-DL8-ID
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27570467831319) Tempo aproximado para leitura: **00:01:20 min****Ocorrência**Erros na integração do Protheus com o Coleta Entrega relacionados a unidade.  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Causa**No coleta entrega, caso a unidade possua um código de mais de 4 caracteres, excede o tamanho do campo **DN8\_ID - Id SAAS**, gerando erros na integração do Protheus com o Coleta Entrega. Esse erro pode ocorrer para as integrações com o Coleta Entrega a partir do **Protheus Faturamento**, **Protheus TMS** e **Protheus OMS**, pois essas utilizam a tabela **DN8 - Filiais Externas** na integração.   
  
**Solução**O produto liberou uma atualização de dicionário 014657 para atualizar o tamanho do campo **DN8\_ID - Id SAAS** para 10 caracteres, para que permita vincular o código da unidade do Coleta Entrega corretamente.   
  
Vale reforçar que o layout das integrações será revisado para acatar o tamanho do campo **DN8\_ID - Id SAAS**, mas caso tenha problemas na gravação do histórico da integração na tabela **DN5 - Histórico de Integrações**, ajuste o layout manualmente para acatar o tamanho do campo **DN8\_ID - Id SAAS** e grave o histórico novamente.   
  
**Anexo**
