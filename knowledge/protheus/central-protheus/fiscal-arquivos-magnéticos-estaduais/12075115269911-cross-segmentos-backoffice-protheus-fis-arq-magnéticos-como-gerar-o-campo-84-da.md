---
article_id: 12075115269911
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: fb8d044e912c02342b4b2501b2b11e2a723393f45e26402f355a79642d37e747
fetched_at: '2026-06-28T22:42:09.137454+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  o campo 84 da DAPI?
type: support-article
updated_at: '2023-01-31T20:28:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12075115269911-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-campo-84-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida** Como gerar o campo **84 - Valor Retido** da **DAPI**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

O **84 - Valor Retido** é  gerado com base nos valores totais das operações do período lançadas no livro **Registro de Saídas** nas seguintes condições:

1. O campo **CFOP (D2\_CF)** for iniciado por **6**;

2. No cadastro da TES o campo**Solid. Obs (F4\_OBSSOL)** esteja preenchido com **SIM**

3. O sistema recebe informações do campo **ICMS Solid. (D2\_ICMSRET).**
