---
article_id: 11965035246999
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 947ad669761e779c85092f309e960b519c04bf947c4b048eaf25c5c954cbc33f
fetched_at: '2026-06-28T22:42:09.130312+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  o campo 77 da DAPI?
type: support-article
updated_at: '2023-01-27T12:28:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11965035246999-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-campo-77-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar o campo **77 - Valor Retido** da DAPI?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

O **campo 77 - Valor Retido** é  gerado com base nos valores totais das operações do período lançadas no livro **Registro de Saídas** nas seguintes condições:

1. O campo **CFOP (D2\_CF)** é iniciado por **5**;

2. No cadastro da **TES** o campo**Solid. Obs (F4\_OBSSO**L) esteja preenchido com **SIM**

3. O sistema recebe as informações do campo **ICMS Solid. (D2\_ICMSRET).**
