---
article_id: 4411511737111
category: RH - Provisão
content_hash: 06b97fd89b1072d0046138aee774d829a1a7ce3e55b8fa123b6156dee9f1ebe5
fetched_at: '2026-06-28T22:43:55.910200+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - GP070FIM - Finalização do processamento de cálculo
  da provisão
type: support-article
updated_at: '2025-10-24T12:39:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411511737111-RH-Linha-Protheus-GPE-GP070FIM-Finaliza%C3%A7%C3%A3o-do-processamento-de-c%C3%A1lculo-da-provis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32998197344023) Tempo aproximado para leitura: **00****:02:00 min** **Dúvida**Utilização Ponto de entrada GP070FIM.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução****01) Visão Geral**

O Ponto de entrada GP070FIM é acionado na finalização do processamento do cálculo da provisão, após todo o processamento e gravação na tabela SRT.

**Programa Fonte**GPEM070.PRX

**Sintaxe**

GP070FIM - Finalização do processamento de cálculo da provisão ( [ ] )

**02. Exemplo de Utilização:**

#INCLUDE 'RWMAKE.CH'             //TESTE PONTO ENTRADA GP070FIM  
USER FUNCTION GP070FIM()  
Local cTitulo:= "Teste Ponto de Entrada GP070FIM"  
Local cMat := SRA->RA\_MAT  
Aviso(cTitulo, cMat + " " + 'Clique OK para continuar... Ponto de Entrada GP070FIM', { "Ok" },, )  
Return

**Saiba Mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)

<https://tdn.totvs.com/pages/viewpage.action?pageId=642633399>
