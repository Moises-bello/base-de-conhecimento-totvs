---
article_id: 11965306272151
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 1f6d31f90d7a35c7f5d7f270c9187d769079206e19a3baf05e7ee3efde7340e0
fetched_at: '2026-06-28T22:42:09.133502+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  o campo 83 da DAPI?
type: support-article
updated_at: '2023-01-27T12:32:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11965306272151-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-campo-83-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida** Como gerar o campo **83 - Base de Cálculo Substituição Tributária**  da **DAPI**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

O **campo 83 - Base de Cálculo Substituição Tributária** é  gerado com base nos valores totais das operações do período lançadas no livro **Registro de Saídas** nas seguintes condições:

1. O campo **CFOP (D2\_CF) é** iniciado por **5**;

2. No cadastro da **TES** o campo**Solid. Obs (F4\_OBSSOL**) esteja preenchido com **SIM.**

3. O sistema recebe as informações do campo **ICMS Solid. (D2\_ICMSRET).**
