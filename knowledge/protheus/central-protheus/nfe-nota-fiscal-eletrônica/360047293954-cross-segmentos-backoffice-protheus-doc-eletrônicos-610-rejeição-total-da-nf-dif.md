---
article_id: 360047293954
category: NFe - Nota Fiscal Eletrônica
content_hash: a03c75f7848c8cd950e008b1a6699bf6756bf5bd382c00e59f0b9c29c9295d08
fetched_at: '2026-06-28T22:40:05.167576+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 610 Rejeição :
  Total da NF difere do somatório dos Valores compõe o valor Total da NF para nota
  de Reidi'
type: support-article
updated_at: '2024-09-16T21:58:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047293954-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-610-Rejei%C3%A7%C3%A3o-Total-da-NF-difere-do-somat%C3%B3rio-dos-Valores-comp%C3%B5e-o-valor-Total-da-NF-para-nota-de-Reidi
---

**Dúvida**Como corrigir a rejeição abaixo:

Rejeição: 610 Total da NF difere do somatório dos Valores compõe o valor Total da NF para nota de Reidi ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

O valor da TAG **vNF** deve bater com os valores levados no bloco **ICMSTOT** subtraindo e somando de acordo com o esperado pela regra de sua **totalizadora.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26415433979159)

* **Na NT 4.00 há novas TAGS na Totalizadora:**
* (+) vFCPST (id:W06a)
* (+) vIPIDevol (id: W12a)

Caso o valor da **VNF** tenha tenha somado ou deduzido as **TAGs vICMS, vPIS ou vCOFINS** e o **CFOP** seja diferente de **iniciado por 3** causa a rejeição 610.

* **Exemplo somando, porém pode ser ser subtraindo também o XML** **gerou conforme abaixo:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068970794)

1- Caso seja uma importação com **destinatário EX** do exterior  será necessário alterar no TES no campo **F4\_CF "Cod. Fiscal" para** o CFOP**iniciado por 3.**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26350936673303)**

2- Após isso, **exclua a nota** e gere novamente.

3- Caso não seja **uma importação** conforme o link abaixo:

<http://tdn.totvs.com/display/public/PROT/IMP0036_Deduzir_Pis_e_Cofins_da_Nota_Fiscal_Reide>

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070068453)

A nota de Reidi existe no sistema, mas não é aceita pela Sefaz na sua operação.  
  
Se precisar somar ou deduzir o Pis, Cofins e ICMS da nota deve gerar um desconto na nota ou já lançar o valor do produto com desconto. Pois esses impostos não fazem parte da totalizadora da NFe.  
  
Caso haja dúvidas como deve ser realizada essa nota, **solicite que o fiscal de sua empresa faça uma consulta formal na Sefaz.**  
  
4- Altere os campos na TES para que a nota seja autorizada **Agrega Valor** F4\_AGREG = S, **Agr. Pis** F4\_AGRPIS= N **Agr. Cofins** F4\_AGRCOF= N  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070064233)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070064513)

5 -Após isso, **exclua a nota e gere novamente.**
