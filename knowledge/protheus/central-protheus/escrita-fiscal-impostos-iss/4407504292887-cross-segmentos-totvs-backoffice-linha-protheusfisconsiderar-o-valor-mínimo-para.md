---
article_id: 4407504292887
category: Escrita Fiscal - Impostos - ISS
content_hash: a22b915a4328405f7fa5e087cc96ec2ee0284cfd7b106ddb0dd30592c52acff8
fetched_at: '2026-06-28T22:39:35.279785+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos/ TOTVS Backoffice Linha Protheus/FIS/Considerar o valor mínimo
  para retenção do ISS
type: support-article
updated_at: '2021-08-31T13:11:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407504292887-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Considerar-o-valor-m%C3%ADnimo-para-reten%C3%A7%C3%A3o-do-ISS
---

**Dúvida**Como ajustar o sistema para que considera o valor mínimo de retenção do ISS descrito no parâmetro MV\_VRETISS.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**

Para ser considerado o valor mínimo de retenção do ISS, dever ser ajustado o sistema da seguinte forma:

**Cliente:**

Ajuste o cadastro do Cliente, campo **F.Ret.ISS (A1\_FRETISS)** = 1=Considera valor mínimo (MV\_VRETISS)

                                                                                                      2=Sempre retém

**Fornecedor:**

Para que o valor mínimo seja considerado no Documento de Entrada, dever ser ajusta a TES.

Na aba Outros campo For Ret ISS(F4\_FRETISS) - Informa se a TES considera o parâmetros MV\_VRETISS.

**For Ret ISS**(F4\_FRETISS) = 1 - Cons Vlr Mín.

                                           2 - Sempre Retém

Link contendo informações sobre Retenção do ISS: 

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027870472-MP-FIS-Reten%C3%A7%C3%A3o-de-ISS?source=search>
