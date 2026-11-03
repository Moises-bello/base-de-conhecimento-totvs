---
article_id: 18949589336471
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: 1be1fb7a2821ef2ccaefd85dfee4bf394357929311401be40e74ebce43b0d552
fetched_at: '2026-06-28T22:36:56.554989+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Compensação da
  NCC
type: support-article
updated_at: '2023-11-09T17:32:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18949589336471-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Compensa%C3%A7%C3%A3o-da-NCC
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18949630845847)*Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como realizar uma nota fiscal de devolução(NCC) no SIGAEEC ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Export Control* – A partir da versão 12.1.2210.

**Solução**

Referente ao processo informado, no módulo **SIGAEEC** não há tratamento para o Nota de Credito Cliente **"NCC"** sendo o título da **"NCC"** gerado pelo **SIGACOM** a partir da nota de devolução, não possuindo relação com o módulo de Exportação.  
 

No exportação, quando é feita a nota de devolução, é gerado o câmbio de abatimento/desconto do evento 101, mas este câmbio não tem relação ou integração com o módulo SIGAFIN.  
   
Para a compensação da "**NCC"** o processo é manual no financeiro, já que este título não tem relação com o **SIGAEEC**.

**Saiba mais**

**[Geração de Nota Fiscal de Devolução](https://tdn.totvs.com/pages/releaseview.action?pageId=220890199)**
