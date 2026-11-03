---
article_id: 360051853614
category: Inspeção de Entradas (SIGAQIE)
content_hash: 6f7b2812a5c261fb53df79304f9e5467a9fb92b6dd84f3644265b01e4bba75e3
fetched_at: '2026-06-28T22:42:26.926801+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Conceito da rotina QIEA110
type: support-article
updated_at: '2023-08-15T14:56:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051853614-Manufatura-Linha-Protheus-SIGAQIE-Conceito-da-rotina-QIEA110
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16775685430679)***Tempo aproximado para leitura: **00:01:30 min  
  
Dúvida**Qual o conceito da rotina **QIEA110 - Classes de Situações**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Todas as versões  
  
**Solução**A rotina **QIEA110 - Classes de Situações** relaciona as possíveis classificações da situação do fornecedor, perante a necessidade de inspeção da entrada. O Sistema apresenta quatro situações previamente cadastradas:

![Situa__o.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360082725994)

Essas classificações correspondem aos critérios de **skip-lote**, considerando as respectivas notas de **IQF - Índice de Qualificação do Fornecedor**, limites inferior e superior.  
O fornecedor estará **habilitado para skip-lote** quando sua pontuação atingir a classificação **A** ou **B**. Ou seja, se o fornecedor for classificado como **C** ou **D,** ele **não estará habilitado para skip-lote**.  
  
**Importante**  
A classe de situação é solicitada, obrigatoriamente, no cadastro de **Produto X Fornecedor - MATA061**.  
O critério de **skip-lote** adotado para cada classe de situação, deve obedecer aos índices de **IQF**.
