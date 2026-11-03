---
article_id: 360052702853
category: NFe - Nota Fiscal Eletrônica
content_hash: 0538956a3928b6381eb3fba4c6cbb42ca9afe29db57b4237facc53c2f74c4374
fetched_at: '2026-06-28T22:40:01.923251+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Qual o parâmetro
  que define a quantidade de horas para exclusão da nota fiscal eletrônica autorizada
  ?'
type: support-article
updated_at: '2021-10-11T15:43:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052702853--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Qual-o-par%C3%A2metro-que-define-a-quantidade-de-horas-para-exclus%C3%A3o-da-nota-fiscal-eletr%C3%B4nica-autorizada
---

**Dúvida**

Qual o parâmetro que define a quantidade de horas para exclusão da nota fiscal eletrônica autorizada ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1- Configure o parâmetro **MV\_SPEDEXC** com a **quantidade de horas** que será permitida a exclusão da nota de **entrada ou de saída:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084202633/mceclip0.png)

* **Saiba mais:**

Para exclusão de notas de **saída ou entrada com espécie = SPED.**

Será considerado se a nota foi autorizada e se os campos estão preenchidos **F2\_HAUTNFE  ou  F1\_HAUTNFE e o F2\_DAUTNFE ou F1\_DAUTNFE .**
