---
article_id: 4403486901271
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 099625526ac7388b011d8567dc723f94e47405ee12777d4ec6c364f355525df5
fetched_at: '2026-06-28T22:39:20.520274+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Tag <vICMSSubstituto>
  - Tratamento ICMS ST Revendedor - CST 60
type: support-article
updated_at: '2021-07-13T17:41:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403486901271-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Tag-vICMSSubstituto-Tratamento-ICMS-ST-Revendedor-CST-60
---

**Dúvida**

Tag <vICMSSubstituto> - Tratamento ICMS ST REVENDEDOR - CST 60

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - a partir da versão 12.1.17  
  
**Solução**

A tag **vICMSSubstituto** quando a operação possuiCST 60, porém, não se é o imediato da cadeia da operaçãoserá gerada com base nas informações inseridas manualmente nos campos **D1\_ICMNDES,D1\_BASNDESeD1\_ALQNDES.**

**Importante!**

Na situação detalhada nesse documento, as informações referente ao ICMS já recolhido anteriormente será preenchido manualmente nos campos **D1\_ICMNDES**, **D1\_BASNDES** e**D1\_ALQNDES**.  
De acordo com essas informações será gerada a tag **vICMSSubstituto** com a seguinte variação:

* Caso o parâmetro **MV\_ULTAQUI**seja igual a **3**:  
  **Base Retido**= D1\_BASNDES / Quantidade de Entrada \* Quantidade de Saída **Valor do Próprio do Substituto**= ((Base Retido \* (MV\_ICMPAD/100)) - D1\_ICMNDES) / Quantidade de Entrada \* Quantidade de Saída
* Caso o parâmetro **MV\_ULTAQUI**seja qualquer outro valor que não **3:  
  Base Retido**= D1\_BASNDES **Valor do Próprio do Substituto**= ((Base Retido \* (MV\_ICMPAD/100)) - D1\_ICMNDES)

**Assuntos relacionados:**

[Orientações Consultoria de Segmentos - 5758909 - Decreto 54.308 - Do Ajuste do Imposto Retido por Substituição Tributária](https://tdn.totvs.com/pages/releaseview.action?pageId=490661819 "Seguir link")

[MP - NFE - ICMS Recolhido anteriormente e ICMS Efetivo para RS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039771093-MP-NFE-ICMS-Recolhido-anteriormente-e-ICMS-Efetivo-para-RS- "Seguir link")

[ICMS ST - Ajuste de Montante de Imposto - Regras para Varejistas e Não Varejistas RS](https://tdn.totvs.com/pages/releaseview.action?pageId=444598643 "Seguir link")

DT - NFE -Tag <vICMSSubstituto> - Tratamento ICMS ST REVENDEDOR - CST 60

<https://tdn.engpro.totvs.com.br/display/public/PROT/10326293+DSERFISE-42+DT+-+NFE+-Tag+%3CvICMSSubstituto%3E+-+Tratamento+ICMS+ST+REVENDEDOR+-+CST+60>
