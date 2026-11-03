---
article_id: 360042650853
category: NFe - Nota Fiscal Eletrônica
content_hash: ad52fe9347fdea234520c00ccd2f1c9dbe364f826d5d7140960376c934ac9110
fetched_at: '2026-06-28T22:40:07.178904+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Rejeição: 610 Total
  da NF difere do somatório dos Valores compõe o valor Total da NF para ICMS-ST'
type: support-article
updated_at: '2024-09-16T21:58:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042650853-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Rejei%C3%A7%C3%A3o-610-Total-da-NF-difere-do-somat%C3%B3rio-dos-Valores-comp%C3%B5e-o-valor-Total-da-NF-para-ICMS-ST
---

**Dúvida**

Como solucionar a rejeição abaixo:

Rejeição: 610 Total da NF difere do somatório dos Valores compõe o valor Total da NF ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

O valor da TAG **vNF** deve bater com os valores levados no bloco **ICMSTOT** subtraindo e somando de acordo com o esperado pela regra de sua totalizadora.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26415399025175)

* **Na NT 4.00 há novas TAGS na Totalizadora:**
* (+) vFCPST (id:W06a)
* (+) vIPIDevol (id: W12a)

Caso o valor que não tenha destacado no XML seja o valor do **ICMS-ST** que foi calculado no sistema:

* Exemplo o XML gerou conforme abaixo:  
    
  ![](https://totvssuporte.zendesk.com/attachments/token/dLn9ukzlGjWTGL1PCJeiHOiEY/?name=inline-955191547.png)​  
    
    
    
  Porém,  só é destacado o **ICMS-ST** se utilizar a **situação tributária do ICMS 10, 30, 70 ou 90:**  
    
  Altere a situação tributária no TES no campo  **Sit. trib. ICMS** **(F4\_SITTRIB)**  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/26415414784535)  
    
  E deixe o campo **Agrega solid = Sim (F4\_INCSOL)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056732274)**

* Após isso, exclua a nota e gere novamente  se for utilizar o mesmo pedido digite novamente a TES para que seja alterada a situação tributária no item do produto.

* **Importante:**

Caso seja emitente do **Simples Nacional.**

* Exemplo o XML gerou conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063536214)

Porém,  só é destacado o **ICMS-ST** se utilizar a **situação tributária do ICMS 201, 202, 203 ou 900**  
  
Altere a situação tributária no TES no campo  **F4\_CSOSN "Campo Cod. Sit. SN"**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26415414786839)

* E deixe o campo **Agrega solid = Sim (F4\_INCSOL)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056732274)**

* Após isso, exclua a nota e gere novamente.

* **Saiba Mais:**

Para não calcular o **ICMS-ST** deve **configurar a TES:**  
  
**MKP ICM COMP =** Sim  
**Marg. Solid =** Nunca

* **Importante:**

Lembrando que caso seja **nota de devolução** e não possa destacar o **ICMS-ST em TAG própria** há o parâmetro da documentação abaixo:

[MP - NFE - Destaque de ICMS e/ou ICMS-ST em campo próprio ou em Informações complementares](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020986011)
