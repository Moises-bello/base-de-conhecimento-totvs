---
article_id: 8102671038359
category: Inspeção de Processos (SIGAQIP)
content_hash: 95928162656cb7e49b504b4bd3ddc042c1eaa523752c382b221c8d7e67b979c7
fetched_at: '2026-06-28T22:42:25.800418+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Impressão Certificado de Qualidade
type: support-article
updated_at: '2022-08-12T18:12:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8102671038359-Manufatura-Linha-Protheus-SIGAQIP-Impress%C3%A3o-Certificado-de-Qualidade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:35 min** **Dúvida**Na rotina **QIPR050 - Impressão de Certificado de Qualidade** como imprimir o **Certificado de Qualidade** sem informar o **Laudo Geral** da necessidade de **inspeção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Todas as versões  
  
**Solução**  
Para imprimir o **Certificado de Qualidade** sem informar o **Laudo Geral** da necessidade de **inspeção**, o parâmetro **MV\_QIMPRCQ - Imprime Certificado de Qualidade sem Laudo Geral** deverá ter o conteúdo igual a **S - Sim**.   
Estando o conteúdo deste parâmetro igual a **N - Não**, haverá exigibilidade de Laudo Geral para que a impressão seja permitida, ocorrendo o alerta **Identificada inconsistência, favor verificar (Ordem de Produção + Lote + Num. Série + Produto + Revisão).**  
O **Laudo Geral** é cadastrado na necessidade de inspeção na rotina **QIPA215 - Resultados.**
