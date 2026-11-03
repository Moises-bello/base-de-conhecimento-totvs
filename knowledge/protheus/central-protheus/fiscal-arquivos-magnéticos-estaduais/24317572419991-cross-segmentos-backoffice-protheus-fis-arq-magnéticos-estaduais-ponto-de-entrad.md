---
article_id: 24317572419991
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 5769a4320b82e9617320843fcbf1bccb865c618a9facfaece19a1d464b902fb1
fetched_at: '2026-06-28T22:42:09.180049+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Estaduais -
  Ponto de entrada FCIPROC001  para FCI.
type: support-article
updated_at: '2024-06-20T17:39:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24317572419991-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Estaduais-Ponto-de-entrada-FCIPROC001-para-FCI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24317596183191) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Qual ponto de entrada é disponibilizado para a rotina **FISA061 - FCI?**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]  
  
**Solução:**

Para essa questão, segue boletim técnico:

**<https://tdn.totvs.com/pages/releaseview.action?pageId=805990999>**

Inclusão do ponto de entrada **FCIPROC001**na rotina **FISA061** - **FCI** - **Ficha de Conteúdo de Importação**

Esse ponto de entrada tem por finalidade permitir que sejam enviadas informações referentes ao valor da parcela importada, valor das saídas e se o produto é novo ou não. 

**Aplicação**: para produtos produzidos com itens  importados

O ponto de entrada é acionado durante a **apuração da** **FCI** e o produto é processado diretamente na tabela **CFD**.
