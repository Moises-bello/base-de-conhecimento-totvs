---
article_id: 1500004940861
category: Faturamento - Integrações
content_hash: ecd7853f8412cb17f60485085e890969e5f868630f7d2a7f5c8ec79b4bbdc226
fetched_at: '2026-06-28T22:38:26.462179+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - SIGAFAT - Centro de Custo na
  Nota Fiscal de Saída com Integração EAI
type: support-article
updated_at: '2023-07-20T18:36:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004940861-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Centro-de-Custo-na-Nota-Fiscal-de-Sa%C3%ADda-com-Integra%C3%A7%C3%A3o-EAI
---

**Dúvida**

Na integração via Mensagem única não está gravando o rateio no Pedido de Venda no campo **C6\_CC**.

**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

A TAG responsável para a gravação do centro de custo na integração é a **CostCenterInternalId ( <CostCenterInternalId>68|20903014204401</CostCenterInternalId>),** o valor composto nesta tag é gravado no campo   **AGG\_CC (C. CUSTO Rateio)** e não **C6\_CC**.

Outro campo que é utilizado neste processo também é o C6\_RATEIO, se houver rateio na integração o seu conteúdo deve ser 1.

A alternativa para que seja gravado o conteúdo no campo **C6\_CC (C. CUSTO)** é utilizar o  **Ponto de Entrada MT410EAI.**

**Saiba mais:**

<https://tdn.totvs.com/x/D4TYCg>

Documentação sobre a funcionalidade do rateio no Backoffice Protheus Faturamento:

**[FAT0117\_Centro\_de\_Custo\_no\_Documento\_de\_Saída](https://tdn.totvs.com/pages/releaseview.action?pageId=244936415)**
