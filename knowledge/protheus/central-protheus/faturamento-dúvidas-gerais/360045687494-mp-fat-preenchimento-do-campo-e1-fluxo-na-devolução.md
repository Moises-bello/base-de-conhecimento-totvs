---
article_id: 360045687494
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 76dbd57db53d725097f1b843632140c60e02de9f56f3505d8bb0a46bec16577e
fetched_at: '2026-06-28T22:38:31.329274+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Preenchimento do campo E1_FLUXO na Devolução
type: support-article
updated_at: '2021-04-28T15:53:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045687494-MP-FAT-Preenchimento-do-campo-E1-FLUXO-na-Devolu%C3%A7%C3%A3o
---

**Dúvida**

Gostaria que na notas de devolução, o campo **E1\_FLUXO** fosse preenchido como "**N"**, tem parametrização para isso?

**Ambiente**

Microsiga Protheus - todas as versões.  
  
**Solução**

A rotina **mata461** (**preparação da nota de saída**) não trata o campo  **E1\_FLUXO** como "**N**", por determinação dentro do próprio fonte, o campo já recebe a atribuição como "**S**", não havendo parametrização de mudança.  
  
Se for realmente necessário a mudança, somente por customização, mas não há ponto específico para o tratamento, no caso pode-se usar o ponto de entrada  **M460FIM**([**https://tdn.totvs.com/pages/viewpage.action?pageId=6784180**](https://tdn.totvs.com/pages/viewpage.action?pageId=6784180)), após transação para efetuar o ajuste conforme a necessidade.
