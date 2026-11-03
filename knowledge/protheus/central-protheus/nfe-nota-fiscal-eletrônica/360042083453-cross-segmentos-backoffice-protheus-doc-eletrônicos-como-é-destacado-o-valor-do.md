---
article_id: 360042083453
category: NFe - Nota Fiscal Eletrônica
content_hash: a52a32a74f9365756f5b3abac4ca4916a708d8dd389dc20d1e7e96e939ef240d
fetched_at: '2026-06-28T22:40:01.646299+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como é destacado
  o valor do ICMS desonerado no Danfe ?'
type: support-article
updated_at: '2021-07-16T18:59:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042083453--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-%C3%A9-destacado-o-valor-do-ICMS-desonerado-no-Danfe
---

**Dúvida**Como é destacado o valor do ICMS desonerado no Danfe ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Desde a versão **3.10 da NFe** na qual foi criada a **TAG Vicmsdeson** o valor da desoneração do Suframa de ICMS deixou de ser destacado **na TAG Vdesc** e passou a **ser gerado na Vicmsdeson** e com isso, deixou de ser gerado no campo desconto do Danfe que é um espelho do XML.

* **XML gerado:**

**![](https://totvssuporte.zendesk.com/attachments/token/cgei53KTwaru917WgO5cfoNnH/?name=inline2052551793.png)​**

* **Danfe:**

**![](https://totvssuporte.zendesk.com/attachments/token/XtTneOe7uMUWuD24gFJzfDgZU/?name=inline-10876663.png)**

* Conforme a nota técnica **2013.005\_v\_1.22 página 11:**

![](https://totvssuporte.zendesk.com/attachments/token/b7w8fli8HExWBZYg5hmzEqNoc/?name=inline-1644093849.png)​  
  
  
**Orientação para impressão de DANFE:**  
  
O conteúdo do campo vICMSDeson, enquanto não for previsto no leiaute do DANFE, deverá ser copiado no campo de Informações Complementares de Interesse do Contribuinte (infCpl) para que a informação conste impressa no DANFE.  
  
Caso seja necessária sua impressão no DANFE, outros campos que não forem previstos no leiaute também poderão ser copiados no campo de Informações Complementares de Interesse do Contribuinte (infCpl).

* **Caso exista alguma legislação ou NT que informe diferente disso nos envie e informe a página.**
