---
article_id: 22340390955415
category: Financeiro - Contas a Receber
content_hash: f2755a05907870797e76b88021f6371c8e8afb7be949f5bd2e538af7f3ec4b4e
fetched_at: '2026-06-28T22:38:13.805811+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN- FINA460 - Liquidação
  com baixa parcial, sem gerar títulos de impostos
type: support-article
updated_at: '2024-03-26T14:21:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22340390955415-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA460-Liquida%C3%A7%C3%A3o-com-baixa-parcial-sem-gerar-t%C3%ADtulos-de-impostos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22340374987031) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como realizar uma liquidação de um título baixado parcialmente, que contem natureza com retenção de impostos, porém o cliente não recolhe?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Alterar o parâmetro **MV\_VL460NT = 3.**

Dessa forma, ao realizar uma liquidação cujo título pai tenha uma natureza que retenha impostos e um cliente que não, mesmo após ter sofrido baixa parcial, o sistema não irá gerar títulos de impostos.   
  
**Exemplo**

Ao gerar um título com:

- A **Natureza** que retenha **PCC  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22341250448663)**

- **Cliente** sem a **retenção de impostos**:  **![](https://centraldeatendimento.totvs.com/hc/article_attachments/22341250471575)**

- Ao realizar uma **baixa parcial** e uma **liquidação** (com a mesma **natureza financeira**), os **títulos de impostos não são gerados**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/22341324096279)**![](https://centraldeatendimento.totvs.com/hc/article_attachments/22341264149143) **Saiba mais**[FINA460 - Liquidação a receber - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=545236275#FINA460Liquida%C3%A7%C3%A3oareceberP12-04.IMPOSTOS)
