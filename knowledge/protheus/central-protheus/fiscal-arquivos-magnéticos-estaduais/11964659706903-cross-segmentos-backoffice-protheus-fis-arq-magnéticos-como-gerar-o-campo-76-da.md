---
article_id: 11964659706903
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: fc4ae72be94789cd77afe9ff0a4d706855621e3aa6288bd8a19d21b1351ae039
fetched_at: '2026-06-28T22:42:09.127277+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  o campo 76 da DAPI?
type: support-article
updated_at: '2023-01-27T12:24:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11964659706903-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-campo-76-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar o campo **76 - Base de cálculo substituição tributária** da DAPI?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

O **campo 76 - Base de cálculo substituição tributária** é  gerado com base nos valores totais das operações do período lançadas no livro **Registro de Saídas** nas seguintes condições:

1. O campo **CFOP (D2\_CF)** iniciado do documento fiscal comece em **5**;  
2. No cadastro da **TES** o campo **Solid. Obs (F4\_OBSSOL)**esteja preenchido com **SIM;**

3. O sistema recebe as informações do campo **Ret. ICMS (D2\_BRICMS).**
