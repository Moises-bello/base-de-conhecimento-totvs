---
article_id: 360026906731
category: TAF - REINF
content_hash: 185bbcb4b47f521c699e66650321315b5f4e732d706795ca6b4559d62fb2e197
fetched_at: '2026-06-28T22:41:34.693370+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Inscrição Estadual do
  contribuinte T001AA
type: support-article
updated_at: '2023-03-31T16:46:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026906731-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Inscri%C3%A7%C3%A3o-Estadual-do-contribuinte-T001AA
---

**Dúvida**

Como gerar o layout T001AA com a Inscrição Estadual do Contribuinte?

**Ambiente**

TAF - REINF - versão 12.1.17 ou superior

**Solução**

Para que o layout T001AA seja gerado, o parâmetro MV\_SUBTRIB deve ser preenchido.

O parâmetro, MV\_SUBTRIB detalha a inscrição estadual utilizada no complemento cadastral do TAF.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026199731/mceclip0.png)

Inscrição Estadual do contribuinte substituído na unidade da federação do contribuinte substituído.

***[![](https://lh3.googleusercontent.com/-gnKyQ2t60-M/XLDIsvb3M5I/AAAAAAAAALE/v36Hcn5kLtIxhYbolns13Pt2V6IaCuLfQCK8BGAs/s512/2019-04-12.png)](https://lh3.googleusercontent.com/-gnKyQ2t60-M/XLDIsvb3M5I/AAAAAAAAALE/v36Hcn5kLtIxhYbolns13Pt2V6IaCuLfQCK8BGAs/s0/2019-04-12.png)***

Caso o parâmetro MV\_SUBTRIB não seja suficiente para detalhar todas as Inscrições Estaduais da empresa, deverão ser criados parâmetros com nome MV\_SUBTRI e final numérico sequencial para acrescentar as demais inscrições. Exemplo: MV\_SUBTRI2, MV\_SUBTRI3, etc.

Ao preenchê-lo, executar o Extrator Fiscal.
