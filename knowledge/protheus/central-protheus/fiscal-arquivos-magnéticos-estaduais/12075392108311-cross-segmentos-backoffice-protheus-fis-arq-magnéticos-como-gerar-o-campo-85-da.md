---
article_id: 12075392108311
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 666374c873912e0ecd7b0a8fc5821a26d2564b1ead56285b0716fabe26cafbf8
fetched_at: '2026-06-28T22:42:09.140910+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  o campo 85 da DAPI?
type: support-article
updated_at: '2023-01-31T20:33:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12075392108311-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-campo-85-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar o campo **85 -Base de Cálculo Substituição Tributária** da **DAPI**?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

O **campo 85 - Base de Cálculo Substituição Tributária** é  gerado com base nos valores totais das operações do período lançadas no livro **Registro de Entradas** nas seguintes condições:

1. No cadastro da TES o campo **Solid. Obs (F4\_OBSSOL)** esteja preenchido com **SIM**

2. O sistema recebe informações do campo **Ret. ICMS (D1\_BRICMS).**
