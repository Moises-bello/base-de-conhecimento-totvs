---
article_id: 12105918494487
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: a2604fee4d622bb9c14cc4813c9286e6717d51d72a55b39f9cb52a8cd0de2e3d
fetched_at: '2026-06-28T22:42:09.124120+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  o campo 102 da DAPI?
type: support-article
updated_at: '2023-02-02T13:21:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12105918494487-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-campo-102-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar o campo **102 Substituição tributária (Saídas)** da **DAPI**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

O campo **102 Substituição tributária (Saídas)** é gerado com base nos valores totais das operações do período lançadas no livro **Registro de Saídas** nas seguintes condições:

1. O campo **CFOP (D2\_CF)** iniciado por **5**;

2. No cadastro da **TES** o campo**Solid. Obs (F4\_OBSSOL)** esteja preenchido com **SIM**

3. O sistema recebe informações do campo **ICMS Solid. (D2\_ICMSRET).**
