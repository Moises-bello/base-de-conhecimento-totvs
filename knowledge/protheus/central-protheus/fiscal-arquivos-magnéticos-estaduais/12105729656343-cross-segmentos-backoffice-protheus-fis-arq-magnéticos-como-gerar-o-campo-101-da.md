---
article_id: 12105729656343
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 0e13f89f9174a3f060ddc95fb50f2ae538b60c075df245955b00b6e330443923
fetched_at: '2026-06-28T22:42:09.120434+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  o campo 101 da DAPI?
type: support-article
updated_at: '2023-02-02T13:17:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12105729656343-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-campo-101-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar o campo **101 Substituição tributária** da **DAPI**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]  
  
**Solução**

O campo **101 Substituição tributária** é  gerado com base nos valores totais das operações do período lançadas no livro **Registro de Entradas**nas seguintes condições:

1. No cadastro da **TES** o campo**Solid. Obs (F4\_OBSSOL)** esteja preenchido com **SIM**

2. O sistema recebe informações do campo **ICMS Solid. (D1\_ICMSRET).**
