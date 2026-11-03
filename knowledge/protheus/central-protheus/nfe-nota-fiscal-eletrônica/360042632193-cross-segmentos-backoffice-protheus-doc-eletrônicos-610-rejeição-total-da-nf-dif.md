---
article_id: 360042632193
category: NFe - Nota Fiscal Eletrônica
content_hash: ca20b4455830b5dcf8e4962995bcff6bf2c7b49af806edfc444b26b6d41cf3f2
fetched_at: '2026-06-28T22:40:05.162065+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 610 Rejeição :
  Total da NF difere do somatório dos Valores compõe o valor Total da NF para IPI'
type: support-article
updated_at: '2024-09-16T21:57:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042632193-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-610-Rejei%C3%A7%C3%A3o-Total-da-NF-difere-do-somat%C3%B3rio-dos-Valores-comp%C3%B5e-o-valor-Total-da-NF-para-IPI
---

**Dúvida**

Como solucionar a rejeição abaixo:

610 Rejeição : Total da NF difere do somatório dos Valores compõe o valor Total da NF para IPI ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.27

Cross Segmentos - TSS - a partir da versão 12

**Solução**

O valor da TAG **vNF** deve bater com os valores levados no bloco **ICMSTOT** subtraindo e somando de acordo com o esperado pela regra de sua totalizadora.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26415413496343)

* **Na NT 4.00 há novas TAGS na Totalizadora:**
* (+) vFCPST (id:W06a)
* (+) vIPIDevol (id: W12a)

Caso o valor que não tenha destacado no XML seja o valor do IPI que foi calculado no sistema:

* Exemplo o XML gerou conforme abaixo:

![](https://totvssuporte.zendesk.com/attachments/token/Slq2MQ7d5q344EBePeU38dhOW/?name=inline634433519.png)​  
​

* No XML  foi utilizado o CST 53:

![](https://totvssuporte.zendesk.com/attachments/token/NH2odccwu6MOoKtacYjqoB626/?name=inline-1464523666.png)​

* Conforme o link abaixo:

[MP-NFE-Destaque de ICMS e IPI em XML e DANFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019535652-MP-NFE-Destaque-de-ICMS-e-IPI-em-XML-e-DANFE?source=search)  
  
Os únicos CSTs de IPI que **destacam o imposto são 00 e 49** para **entrada, 50 e 99 para saída.**  
  
Sendo assim, altere na TES no campo F4\_CTIPI **Cod. trib. IPI**  
  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057026893)​

* **Saiba mais:**

E caso **não possa destacar o IPI em campo próprio** para **nota de devolução** poderá utilizar os parâmetros do link abaixo com um CST tributado conforme informado acima:  
  
[MP - NFE - NT4.00 Destaque do IPI na devolução no XML e DANFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004941852-MP-NFE-NT4-00-Destaque-do-IPI-na-devolu%C3%A7%C3%A3o-no-XML-e-DANFE?source=search)

E caso **não possa destacar o IPI em campo próprio** para **nota normal** poderá utilizar os parâmetros do link abaixo com um CST tributado conforme informado acima:

[MP-NFE- Parâmetro MV\_CFOPREM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020438152)

Após isso, exclua a nota e gere novamente.
