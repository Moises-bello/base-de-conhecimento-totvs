---
article_id: 9863362940183
category: Comércio Exterior - Easy - Financing
content_hash: f20feedfcca940d24956299e79859d66ccb2dc867938dc0cf4cbd7040de60488
fetched_at: '2026-06-28T22:39:53.032985+00:00'
product: protheus
section_id: 1500001538101
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEFF - Qual condição o
  campo Data do Estorno, é preenchido para o evento 100?
type: support-article
updated_at: '2022-10-31T12:38:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9863362940183-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEFF-Qual-condi%C3%A7%C3%A3o-o-campo-Data-do-Estorno-%C3%A9-preenchido-para-o-evento-100
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Qual condição o campo Data do Estorno, é preenchido para o evento 100?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Financing Control* – Todas versões.

**Solução**No momento da inclusão de um contrato de financiamento **SIGAEFF** do tipo **ACC/ACE**, independente das data de crédito e início de juros, é criado o evento **"100 ACC Contrato"** correspondente ao valor do contrato, este evento é a captação do valor do empréstimo, e terá o seu valor atualizado em "Reais" atualizados assim que for preenchido o campo com data de início de juros.  
Ao optar pela liquidação deste contrato  este por ser encerrado ou valor captado, ser transferido para outro contrato de financiando, ao confirmar a liquidação será preenchido campo EF1\_DT\_ENC "Dt. Encerra" e serão criados os eventos,  "**180 Encerramento Contrato ACC",  "501 V.C. ACC", "520 Prov. Juros ACC" e "670 Liq. Juros Forc"**. Se optar por não cancelar liquidar o contrato este permanecerá aberto e com saldo para que sejam vinculadas as *Invoices*, para o evento "**100 ACC Contrato"**, **o campo EF3\_DT\_EST  "Data Estorno"** não será preenchido.
