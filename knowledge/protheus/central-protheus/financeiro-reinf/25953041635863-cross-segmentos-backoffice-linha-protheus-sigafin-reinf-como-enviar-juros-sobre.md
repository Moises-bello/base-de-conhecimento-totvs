---
article_id: 25953041635863
category: Financeiro - Reinf
content_hash: 9684ea96d0f43a5098173b896523113a1df50a3b346627b16589197d53196e05
fetched_at: '2026-06-28T22:37:51.780090+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - Como enviar
  Juros Sobre Capital Próprio (JSCP) para o Reinf
type: support-article
updated_at: '2024-10-09T14:23:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25953041635863-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-Como-enviar-Juros-Sobre-Capital-Pr%C3%B3prio-JSCP-para-o-Reinf
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25953041606167) Tempo aproximado para leitura: **05:00:00 min****Dúvida**Como enviar Juros Sobre Capital Próprio (JSCP) para Reinf ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas versões  
  
  
**Solução**

Os juros sobre capital próprio devem ser escriturados na **EFD-Reinf**, através do evento **R-4010 (beneficiário pessoa física)** ou **R-4020 (beneficiário pessoa jurídica)**, com a **Natureza de rendimentos** ***12016 - Juros sobre Capital Próprio***.

Caso o beneficiário seja não identificado, o contribuinte deverá escriturar o pagamento ou crédito através do evento **R-4040** e utilizar a **Natureza de Rendimentos** ***12052 - Juros sobre Capital Próprios cujos beneficiários não estejam identificados o momento do registro Contábil**.*

Para o processo de envio de **Juros Sobre Capital Próprio** deve-se incluir um **título no Financeiro** ou um **documento de entrada** no **Compras**, ter uma **natureza de rendimento** de **JSCP** vinculada e realizar a **baixa do título** principal.

**Exemplo:**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/25953072388119)](https://centraldeatendimento.totvs.com/hc/article_attachments/25953072388119)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/25953041608855)](https://centraldeatendimento.totvs.com/hc/article_attachments/25953041608855)

**Extrator em arquivo TXT**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/25953072390807)](https://centraldeatendimento.totvs.com/hc/article_attachments/25953072390807)

**Natureza rendimento X Painel Reinf**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26948060118423)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/25953041610903)](https://centraldeatendimento.totvs.com/hc/article_attachments/25953041610903)

**Saiba mais:**

[Juros sobre Capital Próprio](https://tdn.totvs.com/pages/releaseview.action?pageId=789983468)

[Protheus - EFD REINF](https://tdn.totvs.com/display/public/PROT/EFD-REINF)
