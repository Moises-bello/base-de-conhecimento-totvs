---
article_id: 360035386393
category: Faturamento - Cenários de Venda
content_hash: 864d1a4077f5a4497c90e95dfc343ab5e5bcb1cda898ffe3079c5b312bb43fad
fetched_at: '2026-06-28T22:38:33.935603+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Funcionamento
  do campo "Tipo de preço (DA1_TIPPRE)"
type: support-article
updated_at: '2024-02-01T22:03:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035386393-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Funcionamento-do-campo-Tipo-de-pre%C3%A7o-DA1-TIPPRE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21051080340631)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

Do que se trata o campo **"Tipo de preço (DA1\_TIPPRE)"**, na rotina de tabela de preço de venda (**OMSA010**)?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - a partir da release 12.1.23

**Solução**

O campo "Tipo de preço (**DA1\_TIPPRE)"** trata-se de uma melhoria criada pela equipe de desenvolvimento de Varejo (Módulo SIGALOJA), que tem como objetivo de enviar os tipos de preços "Tipo de preço (DA1\_TIPPRE)" com as opções:

* **1** = Preço Venda
* **2** = Venda Consumidor
* **3** = Atacado
* **4** = Varejo
* **5** = Promoção, via mensagem única. (**PriceListHeaderItem**)

OBSERVAÇÃO: Esse campos não é considerado e usado nos processos do módulo Faturamento (SIGAFAT).

**Saiba mais:**

**[DVARLOJ1-918 DT - PriceListHeaderItem - Tabela de Preço - versão 2.001](https://tdn.totvs.com/pages/viewpage.action?pageId=342306210)**
