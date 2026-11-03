---
article_id: 4408849738647
category: NFe - Nota Fiscal Eletrônica
content_hash: f83bc0711bd86354bb790074a078e1cf18987f2ad891014305cbbf05b7823762
fetched_at: '2026-06-28T22:40:05.172245+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 610 Rejeição :
  Total da NF difere do somatório dos Valores compõe o valor Total da NF referente
  aos valores das TAGS COFINSST/vCOFINS E  PISST/vPIS'
type: support-article
updated_at: '2025-07-28T18:58:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408849738647-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-610-Rejei%C3%A7%C3%A3o-Total-da-NF-difere-do-somat%C3%B3rio-dos-Valores-comp%C3%B5e-o-valor-Total-da-NF-referente-aos-valores-das-TAGS-COFINSST-vCOFINS-E-PISST-vPIS
---

**Dúvida**Como resolver a rejeição 610 Rejeição : Total da NF difere do somatório dos Valores compõe o valor Total da NF referente aos valores das TAGS COFINSST/vCOFINS E PISST/vPIS  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**Na Nota Técnica 2020.005**passou a ser validado a rejeição 610 referente ao PIS e Cofins - ST.

1- Verifique se o **Protheus e o TSS estão com as atualizações do link abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.005](Cross%20Segmentos%20-%20Backoffice%20Protheus%20-%20Doc.%20Eletr%C3%B4nicos%20-%20Nota%20t%C3%A9cnica%202020.005)

2- Realizar as **configurações do link abaixo:**

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como calcular PIS/COFINS ST no total da NF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408510846871)

3 - Após isso, **exclua a nota** e **gere novamente.**

4- Para agregar ao total da nota o **F4\_APSCFST** igual a 1= Sim no TES.

* **Exemplo do XML:**

![pis_e_cofins_st.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408849339543)

![icmstot.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408861709591)

* **Validação da Sefaz:**

**![610_Rejei__o_2020.005.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408849725975)**
