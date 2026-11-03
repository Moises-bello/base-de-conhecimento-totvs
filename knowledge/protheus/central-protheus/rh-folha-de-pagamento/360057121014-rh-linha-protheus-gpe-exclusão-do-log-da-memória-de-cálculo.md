---
article_id: 360057121014
category: RH - Folha de Pagamento
content_hash: b34d9c046e455d8014c24108ba9be1029a18d7b240976b9f84654ea578aa9901
fetched_at: '2026-06-28T22:44:14.949282+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Exclusão do log da memória de cálculo
type: support-article
updated_at: '2025-08-13T15:01:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057121014-RH-Linha-Protheus-GPE-Exclus%C3%A3o-do-log-da-mem%C3%B3ria-de-c%C3%A1lculo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26265021837335) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Exclusão do log da memória de cálculo.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoas - Todas as versões  
  
**Solução**

A fim de não onerar demasiadamente o banco de dados, foi incluída a funcionalidade de deleção automática dos logs durante o fechamento do período do roteiro.

Assim, o sistema irá manter apenas **3** períodos de log e seu histórico: 2 fechados + Período Atual.

Esse controle é feito pela chave FILIAL + PROCESSO + PERIODO + NR PAGAMENTO + ROTEIRO, de forma mensal.

Exemplo:

Processo 00001, Roteiro FERIAS, Período 10/2017 - fechado

Processo 00001, Roteiro FERIAS, Período 11/2017 - fechado

Processo 00001, Roteiro FERIAS, Período 12/2017 - aberto

Ao realizar o **fechamento**do período de **Férias** de **12/2017 ,**então teremos:

O sistema irá **deletar** **fisicamente** os registros do roteiro Férias de 10/2017 para o processo 00001.

**Mantendo** no banco de dados apenas: 11/2017 e 12/2017, mais os registros gerados em 01/2018.

**Saber Mais:**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
