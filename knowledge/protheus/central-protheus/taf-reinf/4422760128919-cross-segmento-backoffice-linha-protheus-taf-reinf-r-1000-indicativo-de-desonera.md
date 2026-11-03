---
article_id: 4422760128919
category: TAF - REINF
content_hash: e5c4dc102f3a163594771c5cd9ebb93a41d7ecdc7deaa3eb06d3470574265325
fetched_at: '2026-06-28T22:41:33.369821+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - TAF - REINF - R-1000 - Indicativo
  de desoneração da folha de pagamento tag <indDesoneracao>
type: support-article
updated_at: '2023-03-30T16:53:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4422760128919-Cross-Segmento-Backoffice-Linha-Protheus-TAF-REINF-R-1000-Indicativo-de-desonera%C3%A7%C3%A3o-da-folha-de-pagamento-tag-indDesoneracao
---

**Dúvida**

R-1000 - Indicativo de desoneração da folha de pagamento tag **<indDesoneracao>**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) -TAF - a partir da versão 12  
  
**Solução**

O preenchimento da tag **<indDesoneracao>** tem sua origem a partir do Complemento Cadastral (TAFA050) campo **C1E\_INDDES**, localizado na aba ***e-Socail // Reinf // Reinf***

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4422767967383/mceclip6.png)

Após apurar o evento R-1000 a informação pode ser visualizada através da rotina (TAFA494) Informações do Contribuinte

***Eventos Reinf // Tabelas // R-1000 Informações do Contribuinte***

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4422749391767/mceclip3.png)

A informação na tag **<indDesoneracao>** também pode ser visualizada antes da transmissão através da rotina (TAFA494) Informações do Contribuinte na opção Gerar XML Reinf

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4422749456407/mceclip4.png)

***Exemplo no XML***

**Campo T9U\_IDCPRB=0 - Não Aplicável;**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4422749942167/mceclip1.png)

**Campo T9U\_IDCPRB=1- Empresa enquadrada nos artigos 7° a 9° da Lei 12.546/2011.**

**![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4422757194391/mceclip7.png)**

**Validação:**

 Pode ser igual a [1] apenas se a classificação tributária for igual a [02, 03, 99]. Nos demais casos deve ser igual a [0].

**Informações adicionais:**

**Eventos Reinf**

<https://tdn.totvs.com/display/PROT/Eventos+Reinf#R-1000-1836610875>

**EFD-Reinf - Leiautes**

<http://sped.rfb.gov.br/arquivo/show/5943>
